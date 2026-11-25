"""Xây dựng Khung Khuyến nghị Đa tiêu chí (Biên Pareto + MCDM 3 kịch bản + Phân tích độ nhạy ±0,1 theo Mục 5.9),
Hồi quy Logistic tách ảnh hưởng trực tiếp/gián tiếp lên H_gold (Mục 5.8), và xuất Hình 4 SVG.

Chạy từ thư mục gốc của kho mã:
    PYTHONPATH=src .venv/bin/python scripts/build_pareto_and_logistic.py
"""
import html
import itertools
import json
import math
from pathlib import Path

import numpy as np

from ragvi.retrieval import read_rows

SCENARIOS = {
    'legal_medical': {'label': 'Pháp luật / Y tế (ưu tiên chống ảo giác)', 'w': (0.60, 0.30, 0.10)},
    'fast_lookup': {'label': 'Tra cứu nhanh (ưu tiên độ trễ thấp)', 'w': (0.20, 0.30, 0.50)},
    'balanced': {'label': 'Cân bằng', 'w': (0.34, 0.33, 0.33)},
}

CONFIG_TO_METHOD = {
    'viquad': {
        'C3-E0-R0': 'bm25[c3][word]',
        'C1-E3-R0': 'dense[c1]',
        'C3-E3-R0': 'dense[c3]',
        'C3-E5-R0': 'hybrid[c3][word]',
        'C3-E3-R1': 'dense[c3]+r1',
        'C4-E5-R1': 'hybrid[c4][word]+r1',
    },
    'zalo': {
        'C5_nohead-E3-R0': 'dense[c5_nohead]',
        'C3-E0-R0': 'bm25[c3][word]',
        'C3-E3-R0': 'dense[c3]',
        'C4-E3-R0': 'dense[c4]',
        'C5-E3-R0': 'dense[c5]',
        'C3-E5-R0': 'hybrid[c3][word]',
        'C3-E3-R1': 'dense[c3]+r1',
        'C5-E5-R1': 'hybrid[c5][word]+r1',
    },
}


def dominates(a, b):
    """True nếu cấu hình `a` trội hơn `b` theo cả 3 tiêu chí (Correctness ↑, H_gold ↓, Latency ↓)."""
    ge_all = (a['correctness'] >= b['correctness']
              and a['h_gold'] <= b['h_gold']
              and a['p50_seconds'] <= b['p50_seconds'])
    gt_any = (a['correctness'] > b['correctness']
              or a['h_gold'] < b['h_gold']
              or a['p50_seconds'] < b['p50_seconds'])
    return ge_all and gt_any


def _minmax_norm(vals, higher_is_better=True):
    lo, hi = min(vals), max(vals)
    if hi - lo < 1e-12:
        return [1.0 for _ in vals]
    if higher_is_better:
        return [(v - lo) / (hi - lo) for v in vals]
    return [(hi - v) / (hi - lo) for v in vals]


def score_mcdm(pareto_items, weights):
    """weights = (w_hallu, w_corr, w_lat), đã chuẩn hoá tổng = 1."""
    wh, wc, wl = weights
    nh = _minmax_norm([x['h_gold'] for x in pareto_items], higher_is_better=False)
    nc = _minmax_norm([x['correctness'] for x in pareto_items], higher_is_better=True)
    nl = _minmax_norm([x['p50_seconds'] for x in pareto_items], higher_is_better=False)
    scored = []
    for item, sh, sc, sl in zip(pareto_items, nh, nc, nl):
        total = wh * sh + wc * sc + wl * sl
        scored.append({
            'config': item['config'],
            'score': round(total, 6),
            'norm_hallu': round(sh, 4),
            'norm_corr': round(sc, 4),
            'norm_lat': round(sl, 4),
        })
    scored.sort(key=lambda r: -r['score'])
    return scored


def sensitivity_check(pareto_items, base_w, delta=0.10):
    """Dao động mỗi trọng số ±0.10 (chuẩn hoá lại tổng = 1), kiểm tra tỷ lệ giữ vững cấu hình hạng #1."""
    base_winner = score_mcdm(pareto_items, base_w)[0]['config']
    winners = {}
    total_grid = 0
    for dh, dc, dl in itertools.product((-delta, 0.0, delta), repeat=3):
        w = (base_w[0] + dh, base_w[1] + dc, base_w[2] + dl)
        if any(x <= 0 for x in w):
            continue
        s = sum(w)
        wn = (w[0] / s, w[1] / s, w[2] / s)
        win = score_mcdm(pareto_items, wn)[0]['config']
        winners[win] = winners.get(win, 0) + 1
        total_grid += 1
    stability = winners.get(base_winner, 0) / max(total_grid, 1)
    return {
        'base_winner': base_winner,
        'grid_points': total_grid,
        'stability': round(stability, 4),
        'winner_counts': winners,
    }


def build_pareto_mcdm():
    pb = json.loads(Path('reports/full_phase_b_summary.json').read_text(encoding='utf-8'))
    out = {'scenarios': SCENARIOS, 'datasets': {}}
    for ds_key, label in [('viquad_full', 'UIT-ViQuAD 2.0 Full'), ('zalo_full', 'Zalo Legal Full')]:
        cfgs = pb['end_to_end'][ds_key]['configs']
        items = [
            {
                'config': cname,
                'correctness': round(d['correctness'], 6),
                'h_gold': round(d['h_gold'], 6),
                'p50_seconds': round(d['p50_seconds'], 4),
                'false_refusal': round(d['false_refusal'], 6),
                'wrong_article': round(d['wrong_article'], 6) if 'wrong_article' in d else None,
            }
            for cname, d in cfgs.items() if cname not in ('closed_book', 'oracle')
        ]
        pareto, dominated = [], []
        for x in items:
            dom_by = [y['config'] for y in items if y['config'] != x['config'] and dominates(y, x)]
            if dom_by:
                dominated.append({'config': x['config'], 'dominated_by': dom_by})
            else:
                pareto.append(x)

        scenario_res = {}
        for skey, sinfo in SCENARIOS.items():
            ranked = score_mcdm(pareto, sinfo['w'])
            sens = sensitivity_check(pareto, sinfo['w'], delta=0.10)
            scenario_res[skey] = {
                'label': sinfo['label'],
                'weights': {'h_gold': sinfo['w'][0], 'correctness': sinfo['w'][1], 'latency': sinfo['w'][2]},
                'ranking': ranked,
                'sensitivity_pm01': sens,
            }
        out['datasets'][ds_key] = {
            'label': label,
            'n_rag_configs': len(items),
            'pareto_frontier': pareto,
            'dominated': dominated,
            'scenarios': scenario_res,
        }
    Path('reports/pareto_mcdm_summary.json').write_text(
        json.dumps(out, ensure_ascii=False, indent=2, allow_nan=False), encoding='utf-8')
    return out


def _fit_logistic_irls(X, y, feature_names, max_iter=50, tol=1e-8):
    """Hồi quy logistic MLE bằng Newton-Raphson (IRLS) chuẩn xác kèm SE, Wald z, p-value và Odds Ratio."""
    n, p = X.shape
    beta = np.zeros(p, dtype=np.float64)
    for _ in range(max_iter):
        eta = np.clip(X @ beta, -30.0, 30.0)
        prob = 1.0 / (1.0 + np.exp(-eta))
        w = np.clip(prob * (1.0 - prob), 1e-12, None)
        grad = X.T @ (y - prob)
        H = X.T @ (X * w[:, None])
        step = np.linalg.solve(H + 1e-9 * np.eye(p), grad)
        beta += step
        if np.max(np.abs(step)) < tol:
            break
    eta = np.clip(X @ beta, -30.0, 30.0)
    prob = 1.0 / (1.0 + np.exp(-eta))
    w = np.clip(prob * (1.0 - prob), 1e-12, None)
    cov = np.linalg.inv(X.T @ (X * w[:, None]) + 1e-9 * np.eye(p))
    se = np.sqrt(np.diag(cov))
    z = beta / se
    pvals = [math.erfc(abs(float(zi)) / math.sqrt(2.0)) for zi in z]
    ll = float(np.sum(y * np.log(np.clip(prob, 1e-15, 1.0)) + (1 - y) * np.log(np.clip(1 - prob, 1e-15, 1.0))))
    p0 = float(np.mean(y))
    ll0 = float(n * (p0 * math.log(p0) + (1 - p0) * math.log(1 - p0)))
    mcfadden_r2 = 1.0 - ll / ll0
    rows = []
    for name, b, s, zi, pv in zip(feature_names, beta, se, z, pvals):
        rows.append({
            'feature': name,
            'coef': round(float(b), 6),
            'se': round(float(s), 6),
            'z': round(float(zi), 4),
            'p_value': round(float(pv), 6),
            'odds_ratio': round(math.exp(float(b)), 4),
        })
    return {'n_obs': int(n), 'h_gold_rate': round(p0, 6), 'mcfadden_r2': round(mcfadden_r2, 6), 'terms': rows}


def build_logistic_regression():
    out = {}
    for ds in ('viquad', 'zalo'):
        ret_rows = read_rows(f'data/retrieval_cache_full/retrieval_{ds}_full_phase_a.jsonl')
        ret_map = {(r['method'], r['qid']): r for r in ret_rows}
        ans_rows = read_rows(f'data/retrieval_cache_full/answers_{ds}_full_test.jsonl')
        ans_map = {(r['config'], r['qid']): r for r in ans_rows}
        jdg_rows = read_rows(f'data/retrieval_cache_full/judge_{ds}_full_test.jsonl')

        X_rows, y_rows = [], []
        names = ['intercept', 'recall_at_5', 'has_reranker', 'is_hybrid']
        if ds == 'zalo':
            names += ['is_c4_article', 'is_c5_struct', 'is_c5_nohead']
        else:
            names += ['is_c1_fixed', 'is_c4_para']

        for j in jdg_rows:
            cfg = j['config']
            if cfg not in CONFIG_TO_METHOD[ds] or j.get('error') or j.get('h_gold') is None:
                continue
            method = CONFIG_TO_METHOD[ds][cfg]
            r = ret_map.get((method, j['qid']))
            if r is None or r.get('r5') is None:
                continue
            r5 = float(r['r5'])
            has_r1 = 1.0 if '-R1' in cfg else 0.0
            is_hyb = 1.0 if '-E5-' in cfg else 0.0
            if ds == 'zalo':
                feats = [
                    1.0, r5, has_r1, is_hyb,
                    1.0 if cfg.startswith('C4-') else 0.0,
                    1.0 if cfg.startswith('C5-') else 0.0,
                    1.0 if cfg.startswith('C5_nohead-') else 0.0,
                ]
            else:
                feats = [
                    1.0, r5, has_r1, is_hyb,
                    1.0 if cfg.startswith('C1-') else 0.0,
                    1.0 if cfg.startswith('C4-') else 0.0,
                ]
            X_rows.append(feats)
            y_rows.append(float(j['h_gold']))

        X = np.asarray(X_rows, dtype=np.float64)
        y = np.asarray(y_rows, dtype=np.float64)
        out[f'{ds}_full'] = _fit_logistic_irls(X, y, names)

    Path('reports/logistic_summary.json').write_text(
        json.dumps(out, ensure_ascii=False, indent=2, allow_nan=False), encoding='utf-8')
    return out


def build_fig4_pareto(pm):
    fig_dir = Path('reports/figures')
    W, H = 1080, 500
    el = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
        'font-family="Inter, -apple-system, BlinkMacSystemFont, sans-serif">',
        f'<rect width="{W}" height="{H}" fill="#ffffff"/>',
        '<text x="540" y="32" text-anchor="middle" font-size="18" font-weight="700" fill="#111827">'
        'Hình 4: Biên Pareto 3 tiêu chí (Correctness ↑, H_gold ↓, Độ trễ p50 ↓) trên Full Datasets</text>',
        '<text x="540" y="52" text-anchor="middle" font-size="12" fill="#4b5563">'
        'Điểm xanh đậm + nối đường đứt nét: Cấu hình nằm trên Biên Pareto | Điểm xám: Bị trội | Số trong ngoặc: p50 (giây)</text>',
    ]
    panels = [
        ('viquad_full', 'UIT-ViQuAD 2.0 Full (6 cấu hình RAG)', 80, 500, (1.36, 1.64), (16.5, 23.5)),
        ('zalo_full', 'Zalo Legal Full (8 cấu hình RAG)', 600, 1020, (1.20, 1.56), (16.5, 23.5)),
    ]
    y_top, y_bot = 100, 420
    ph = y_bot - y_top
    for key, title, xl, xr, (xmin, xmax), (ymin, ymax) in panels:
        ds = pm['datasets'][key]
        pw = xr - xl
        el.append(f'<text x="{(xl + xr)/2}" y="84" text-anchor="middle" font-size="14" font-weight="700" fill="#1e3a8a">{title}</text>')
        el.append(f'<rect x="{xl}" y="{y_top}" width="{pw}" height="{ph}" fill="#f9fafb" stroke="#d1d5db"/>')

        # Grid
        for i in range(5):
            xv = xmin + i * (xmax - xmin) / 4
            xx = xl + (xv - xmin) / (xmax - xmin) * pw
            el.append(f'<line x1="{xx:.1f}" y1="{y_top}" x2="{xx:.1f}" y2="{y_bot}" stroke="#e5e7eb" stroke-dasharray="3,3"/>')
            el.append(f'<text x="{xx:.1f}" y="{y_bot + 18}" text-anchor="middle" font-size="10.5" fill="#6b7280">{xv:.2f}</text>')
            yv = ymin + i * (ymax - ymin) / 4
            yy = y_bot - (yv - ymin) / (ymax - ymin) * ph
            el.append(f'<line x1="{xl}" y1="{yy:.1f}" x2="{xr}" y2="{yy:.1f}" stroke="#e5e7eb" stroke-dasharray="3,3"/>')
            el.append(f'<text x="{xl - 8}" y="{yy + 4:.1f}" text-anchor="end" font-size="10.5" fill="#6b7280">{yv:.1f}%</text>')

        el.append(f'<text x="{(xl + xr)/2}" y="{y_bot + 40}" text-anchor="middle" font-size="11.5" font-weight="600" fill="#374151">Correctness (0–2, cao hơn tốt hơn →)</text>')
        el.append(f'<text x="{xl - 46}" y="{(y_top + y_bot)/2}" text-anchor="middle" font-size="11.5" font-weight="600" fill="#374151" transform="rotate(-90 {xl - 46} {(y_top + y_bot)/2})">← H_gold (%, thấp hơn tốt hơn)</text>')

        # Collect all items
        pb = json.loads(Path('reports/full_phase_b_summary.json').read_text(encoding='utf-8'))
        cfgs = pb['end_to_end'][key]['configs']
        pareto_names = {x['config'] for x in ds['pareto_frontier']}
        pareto_pts = []
        for cname, d in cfgs.items():
            if cname in ('closed_book', 'oracle'):
                continue
            cx = xl + (d['correctness'] - xmin) / (xmax - xmin) * pw
            cy = y_bot - (d['h_gold'] * 100 - ymin) / (ymax - ymin) * ph
            if cname in pareto_names:
                pareto_pts.append((cx, cy, cname, d['p50_seconds']))
            else:
                el.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="6" fill="#9ca3af" stroke="#4b5563" stroke-width="1.5"/>')
                el.append(f'<text x="{cx + 8:.1f}" y="{cy + 4:.1f}" font-size="10" fill="#6b7280">{cname} ({d["p50_seconds"]:.1f}s)</text>')

        pareto_pts.sort(key=lambda t: t[0])
        if len(pareto_pts) >= 2:
            pts_str = ' '.join(f'{x:.1f},{y:.1f}' for x, y, _, _ in pareto_pts)
            el.append(f'<polyline points="{pts_str}" fill="none" stroke="#1d4ed8" stroke-width="1.8" stroke-dasharray="5,4"/>')
        for idx, (cx, cy, cname, lat) in enumerate(pareto_pts):
            r = 8 if cname in ('C4-E5-R1', 'C5-E5-R1') else 6.5
            col = '#059669' if cname in ('C4-E5-R1', 'C5-E5-R1') else '#1d4ed8'
            el.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r}" fill="{col}" stroke="#ffffff" stroke-width="1.5"/>')
            dy = -10 if idx % 2 == 0 else 16
            anchor = 'end' if cx > xr - 95 else 'start'
            dx = -8 if anchor == 'end' else 8
            el.append(f'<text x="{cx + dx:.1f}" y="{cy + dy:.1f}" text-anchor="{anchor}" font-size="10.5" font-weight="700" fill="#111827">{cname} ({lat:.1f}s)</text>')

    el.append('</svg>')
    (fig_dir / 'fig4_pareto_mcdm.svg').write_text('\n'.join(el), encoding='utf-8')


def main():
    pm = build_pareto_mcdm()
    lg = build_logistic_regression()
    build_fig4_pareto(pm)
    print('=== PARETO & MCDM SUMMARY ===')
    for ds_key, d in pm['datasets'].items():
        print(f'\n[{d["label"]}] Pareto ({len(d["pareto_frontier"])}/{d["n_rag_configs"]}): '
              f'{[x["config"] for x in d["pareto_frontier"]]}')
        print(f'  Dominated: {d["dominated"]}')
        for skey, s in d['scenarios'].items():
            top = s['ranking'][0]
            sens = s['sensitivity_pm01']
            print(f'  Scenario {skey:<14}: #1={top["config"]:<16} (score={top["score"]:.4f}) | '
                  f'stability(±0.1)={sens["stability"]*100:.1f}% {sens["winner_counts"]}')
    print('\n=== LOGISTIC REGRESSION (H_gold ~ Recall@5 + ...) ===')
    for ds_key, res in lg.items():
        print(f'\n[{ds_key}] n={res["n_obs"]}, H_gold={res["h_gold_rate"]*100:.2f}%, McFadden R2={res["mcfadden_r2"]:.4f}')
        for t in res['terms']:
            print(f'  {t["feature"]:<16} coef={t["coef"]:+.4f} (SE={t["se"]:.4f}, z={t["z"]:+.2f}, p={t["p_value"]:.4f}, OR={t["odds_ratio"]:.3f})')


if __name__ == '__main__':
    main()
