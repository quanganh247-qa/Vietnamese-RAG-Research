"""Tổng hợp thống kê Full Dataset (Phase A 60 cấu hình, Phase B 18 cấu hình, Cluster Bootstrap 95% CI,
kiểm định hoán vị ghép cặp hiệu chỉnh Holm-Bonferroni) và xuất 3 hình SVG công bố.

Chạy từ thư mục gốc của kho mã:
    PYTHONPATH=src .venv/bin/python scripts/build_full_reports.py
"""
import collections
import html
import json
from pathlib import Path
from statistics import mean, median

from ragvi.benchmark import end_to_end_summary
from ragvi.metrics import METRIC_KEYS, cluster_bootstrap_ci, holm_adjust, mean_metrics, paired_perm
from ragvi.retrieval import load_jsonl, read_rows

FULL_PHASE_B_CONFIGS = {
    'viquad': ('closed_book', 'oracle', 'C3-E0-R0', 'C1-E3-R0', 'C3-E3-R0', 'C3-E5-R0', 'C3-E3-R1', 'C4-E5-R1'),
    'zalo': ('closed_book', 'oracle', 'C5_nohead-E3-R0', 'C3-E0-R0', 'C3-E3-R0', 'C4-E3-R0',
             'C5-E3-R0', 'C3-E5-R0', 'C3-E3-R1', 'C5-E5-R1'),
}


def _cluster_of(q, ds):
    if ds == 'viquad':
        return str(q.get('title', q['qid']))
    return str(q.get('group', q['qid']))


def _ci_dict(values_by_qid, cluster_map, n_boot=2000, seed=0):
    if not values_by_qid:
        return None
    qids = sorted(values_by_qid)
    vals = [float(values_by_qid[q]) for q in qids]
    clusters = [cluster_map[q] for q in qids]
    lo, hi = cluster_bootstrap_ci(vals, clusters, n_boot=n_boot, seed=seed)
    return {'mean': round(mean(vals), 6), 'ci95': [round(lo, 6), round(hi, 6)], 'n': len(vals)}


def build_phase_a_summary():
    out = {'datasets': {}, 'comparisons': {}}
    for ds in ('viquad', 'zalo'):
        qs = load_jsonl(f'data/eval_full/{ds}/test.jsonl')
        cluster_map = {q['qid']: _cluster_of(q, ds) for q in qs}
        ans_qids = {q['qid'] for q in qs if q['answerable']}
        rows = read_rows(f'data/retrieval_cache_full/retrieval_{ds}_full_phase_a.jsonl')
        by_method = collections.defaultdict(dict)
        for r in rows:
            by_method[r['method']][r['qid']] = r

        methods_out = {}
        for method in sorted(by_method):
            mrows = by_method[method]
            scored = [mrows[q] for q in sorted(ans_qids) if q in mrows and mrows[q].get('r5') is not None]
            agg = mean_metrics(scored)
            cis = {
                k: _ci_dict({r['qid']: r[k] for r in scored}, cluster_map, n_boot=2000, seed=0)
                for k in METRIC_KEYS
            }
            methods_out[method] = {
                'n_total': len(mrows),
                'n_scored': len(scored),
                **{k: round(agg[k], 6) for k in METRIC_KEYS},
                'ci95': {k: cis[k]['ci95'] for k in METRIC_KEYS},
            }
        out['datasets'][ds] = {
            'n_questions': len(qs),
            'n_answerable': len(ans_qids),
            'n_clusters': len({cluster_map[q] for q in ans_qids}),
            'n_methods': len(methods_out),
            'methods': methods_out,
        }

        pairs = (
            [
                ('hybrid[c4][word]+r1', 'hybrid[c3][word]+r1', 'Best C4 vs C3'),
                ('hybrid[c3][word]', 'bm25[c3][word]', 'Hybrid vs BM25 (C3)'),
                ('dense[c3]+r1', 'dense[c3]', 'Rerank R1 vs R0 (C3 Dense)'),
                ('dense[c3]', 'dense[c1]', 'C3 vs C1 (Dense)'),
            ] if ds == 'viquad' else [
                ('dense[c5]', 'dense[c5_nohead]', 'H1b: C5 vs C5_nohead (Dense R0)'),
                ('dense[c5]+r1', 'dense[c5_nohead]+r1', 'H1b: C5 vs C5_nohead (Dense R1)'),
                ('hybrid[c5][word]+r1', 'hybrid[c5_nohead][word]+r1', 'H1b: C5 vs C5_nohead (Hybrid R1)'),
                ('dense[c5]', 'dense[c3]', 'H1: C5 vs C3 (Dense R0)'),
                ('hybrid[c5][word]+r1', 'hybrid[c3][word]+r1', 'H1: C5 vs C3 (Hybrid R1)'),
                ('hybrid[c5][word]', 'bm25[c5][word]', 'H2: Hybrid vs BM25 (C5)'),
                ('dense[c3]+r1', 'dense[c3]', 'H3: Rerank R1 vs R0 (C3 Dense)'),
            ]
        )
        raw_ps, comp_rows = [], []
        for idx, (m_a, m_b, label) in enumerate(pairs):
            common = sorted(q for q in ans_qids if q in by_method[m_a] and q in by_method[m_b])
            a_vals = [float(by_method[m_a][q]['ndcg5']) for q in common]
            b_vals = [float(by_method[m_b][q]['ndcg5']) for q in common]
            diffs = [x - y for x, y in zip(a_vals, b_vals)]
            clusters = [cluster_map[q] for q in common]
            lo, hi = cluster_bootstrap_ci(diffs, clusters, n_boot=2000, seed=idx)
            p_raw = paired_perm(a_vals, b_vals, n=10000, seed=idx)
            raw_ps.append(p_raw)
            comp_rows.append({
                'label': label, 'method_a': m_a, 'method_b': m_b, 'metric': 'ndcg5',
                'n': len(common), 'mean_a': round(mean(a_vals), 6), 'mean_b': round(mean(b_vals), 6),
                'diff': round(mean(diffs), 6), 'diff_ci95': [round(lo, 6), round(hi, 6)],
                'p_raw': round(p_raw, 6),
            })
        adj = holm_adjust(raw_ps)
        for row, p_h in zip(comp_rows, adj):
            row['p_holm'] = round(p_h, 6)
        out['comparisons'][ds] = comp_rows

    Path('reports/full_phase_a_summary.json').write_text(
        json.dumps(out, ensure_ascii=False, indent=2, allow_nan=False), encoding='utf-8')
    return out


def build_phase_b_summary():
    out = {'judge_calibrated': True, 'end_to_end': {}, 'comparisons': {}}
    for ds, cfgs in FULL_PHASE_B_CONFIGS.items():
        qs = load_jsonl(f'data/eval_full/{ds}/test.jsonl')
        cluster_map = {q['qid']: _cluster_of(q, ds) for q in qs}
        answers = read_rows(f'data/retrieval_cache_full/answers_{ds}_full_test.jsonl')
        judgments = read_rows(f'data/retrieval_cache_full/judge_{ds}_full_test.jsonl')

        base = end_to_end_summary(qs, answers, judgments, configs=cfgs)
        by_cfg_j = {c: {} for c in cfgs}
        for j in judgments:
            if j['config'] in by_cfg_j and not j.get('error'):
                by_cfg_j[j['config']][j['qid']] = j
        by_cfg_a = {c: {} for c in cfgs}
        for a in answers:
            if a['config'] in by_cfg_a:
                by_cfg_a[a['config']][a['qid']] = a

        ora_hg = {q: j['h_gold'] for q, j in by_cfg_j['oracle'].items() if j.get('h_gold') is not None}

        for cfg in cfgs:
            jmap = by_cfg_j[cfg]
            amap = by_cfg_a[cfg]
            corr_map = {q: j['correctness'] for q, j in jmap.items() if j.get('correctness') is not None}
            hg_map = {q: j['h_gold'] for q, j in jmap.items() if j.get('h_gold') is not None}
            hc_map = {q: j['h_ctx'] for q, j in jmap.items() if j.get('h_ctx') is not None}
            fr_map = {q: int(bool(a.get('refused'))) for q, a in amap.items() if a.get('answerable')}
            cr_map = {q: int(bool(a.get('refused'))) for q, a in amap.items() if not a.get('answerable')}
            wa_map = {q: int(bool(j['wrong_article'])) for q, j in jmap.items()
                      if not j.get('refused') and 'wrong_article' in j}

            cis = {
                'correctness': _ci_dict(corr_map, cluster_map)['ci95'] if corr_map else None,
                'h_gold': _ci_dict(hg_map, cluster_map)['ci95'] if hg_map else None,
                'h_ctx': _ci_dict(hc_map, cluster_map)['ci95'] if hc_map else None,
                'false_refusal': _ci_dict(fr_map, cluster_map)['ci95'] if fr_map else None,
                'correct_refusal': _ci_dict(cr_map, cluster_map)['ci95'] if cr_map else None,
            }
            if wa_map:
                cis['wrong_article'] = _ci_dict(wa_map, cluster_map)['ci95']
            base['configs'][cfg]['ci95'] = cis

            if cfg not in ('closed_book', 'oracle'):
                paired_q = sorted(hg_map.keys() & ora_hg.keys())
                rah_diffs = {q: hg_map[q] - ora_hg[q] for q in paired_q}
                rah_ci = _ci_dict(rah_diffs, cluster_map)
                hg_mean = base['configs'][cfg]['h_gold']
                ora_mean = base['configs']['oracle']['h_gold']
                rah_unpaired = hg_mean - ora_mean
                base['configs'][cfg]['rah_against_oracle'] = {
                    'n_pairs': len(paired_q),
                    'paired_diff': rah_ci['mean'],
                    'paired_ci95': rah_ci['ci95'],
                    'unpaired_diff': round(rah_unpaired, 6),
                    'rah_share_of_h_gold': round(rah_unpaired / hg_mean, 6) if hg_mean else None,
                }

        out['end_to_end'][f'{ds}_full'] = {
            'n_questions': len(qs),
            'n_answerable': sum(1 for q in qs if q['answerable']),
            'n_unanswerable': sum(1 for q in qs if not q['answerable']),
            'n_clusters': len({cluster_map[q['qid']] for q in qs}),
            **base,
        }

        pairs = (
            [
                ('C4-E5-R1', 'C3-E3-R0', 'Best C4-E5-R1 vs Anchor C3-E3-R0'),
                ('C3-E3-R0', 'C1-E3-R0', 'H1: C3 vs C1'),
                ('C3-E3-R0', 'C3-E0-R0', 'H2: Dense vs BM25'),
                ('C3-E5-R0', 'C3-E3-R0', 'H2: Hybrid vs Dense'),
                ('C3-E3-R1', 'C3-E3-R0', 'H3: Rerank R1 vs R0'),
                ('C4-E5-R1', 'oracle', 'Best C4-E5-R1 vs Oracle'),
            ] if ds == 'viquad' else [
                ('C5-E3-R0', 'C5_nohead-E3-R0', 'H1b: ViStructChunk C5 vs C5_nohead'),
                ('C5-E3-R0', 'C3-E3-R0', 'H1: C5 vs C3'),
                ('C4-E3-R0', 'C3-E3-R0', 'H1: C4 vs C3'),
                ('C3-E3-R0', 'C3-E0-R0', 'H2: Dense vs BM25'),
                ('C3-E5-R0', 'C3-E3-R0', 'H2: Hybrid vs Dense'),
                ('C3-E3-R1', 'C3-E3-R0', 'H3: Rerank R1 vs R0'),
                ('C5-E5-R1', 'C3-E3-R0', 'Best C5-E5-R1 vs Anchor C3-E3-R0'),
                ('C5-E5-R1', 'oracle', 'Best C5-E5-R1 vs Oracle'),
            ]
        )
        comp_rows = []
        for metric in ('correctness', 'h_gold'):
            raw_ps, mrows = [], []
            for idx, (ca, cb, label) in enumerate(pairs):
                ja, jb = by_cfg_j[ca], by_cfg_j[cb]
                common = sorted(
                    q for q in ja.keys() & jb.keys()
                    if ja[q].get(metric) is not None and jb[q].get(metric) is not None
                )
                a_vals = [float(ja[q][metric]) for q in common]
                b_vals = [float(jb[q][metric]) for q in common]
                diffs = [x - y for x, y in zip(a_vals, b_vals)]
                clusters = [cluster_map[q] for q in common]
                lo, hi = cluster_bootstrap_ci(diffs, clusters, n_boot=2000, seed=idx)
                p_raw = paired_perm(a_vals, b_vals, n=10000, seed=idx)
                raw_ps.append(p_raw)
                mrows.append({
                    'label': label, 'config_a': ca, 'config_b': cb, 'metric': metric,
                    'n_pairs': len(common), 'mean_a': round(mean(a_vals), 6), 'mean_b': round(mean(b_vals), 6),
                    'diff': round(mean(diffs), 6), 'diff_ci95': [round(lo, 6), round(hi, 6)],
                    'p_raw': round(p_raw, 6),
                })
            for row, p_h in zip(mrows, holm_adjust(raw_ps)):
                row['p_holm'] = round(p_h, 6)
            comp_rows.extend(mrows)
        out['comparisons'][f'{ds}_full'] = comp_rows

    Path('reports/full_phase_b_summary.json').write_text(
        json.dumps(out, ensure_ascii=False, indent=2, allow_nan=False), encoding='utf-8')
    return out


def _color_heat(val, vmin, vmax):
    t = max(0.0, min(1.0, (val - vmin) / max(vmax - vmin, 1e-9)))
    # Cream (#f7fbff) -> Teal/Blue (#08519c)
    r = int(247 + (8 - 247) * t)
    g = int(251 + (81 - 251) * t)
    b = int(255 + (156 - 255) * t)
    fg = '#ffffff' if t > 0.58 else '#1f2937'
    return f'rgb({r},{g},{b})', fg


def build_fig1_heatmap(pa):
    fig_dir = Path('reports/figures')
    fig_dir.mkdir(parents=True, exist_ok=True)
    W, H = 1080, 620
    el = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
        'font-family="Inter, -apple-system, BlinkMacSystemFont, sans-serif">',
        f'<rect width="{W}" height="{H}" fill="#ffffff"/>',
        '<text x="540" y="34" text-anchor="middle" font-size="18" font-weight="700" fill="#111827">'
        'Hình 1: Bản đồ nhiệt nDCG@5 Giai đoạn A trên Toàn bộ dữ liệu (60 cấu hình)</text>',
        '<text x="540" y="55" text-anchor="middle" font-size="12" fill="#4b5563">'
        'UIT-ViQuAD 2.0 Validation (n = 2.653 câu có đáp án) &amp; Zalo Legal Full (n = 2.167 câu có đáp án)</text>',
    ]

    # Left panel: ViQuAD (3 chunks x 10 retriever+rerank)
    vq_m = pa['datasets']['viquad']['methods']
    vq_rows = [
        ('BM25 (R0)', lambda c: f'bm25[{c}][word]'),
        ('BM25 + R1', lambda c: f'bm25[{c}][word]+r1'),
        ('E2 VN-v2 (R0)', lambda c: f'dense[{c}][AITeamVN/Vietnamese_Embedding_v2]'),
        ('E2 VN-v2 + R1', lambda c: f'dense[{c}][AITeamVN/Vietnamese_Embedding_v2]+r1'),
        ('E3 bge-m3 (R0)', lambda c: f'dense[{c}]'),
        ('E3 bge-m3 + R1', lambda c: f'dense[{c}]+r1'),
        ('E4 mE5 (R0)', lambda c: f'dense[{c}][intfloat/multilingual-e5-large]'),
        ('E4 mE5 + R1', lambda c: f'dense[{c}][intfloat/multilingual-e5-large]+r1'),
        ('Hybrid (R0)', lambda c: f'hybrid[{c}][word]'),
        ('Hybrid + R1', lambda c: f'hybrid[{c}][word]+r1'),
    ]
    vq_cols = [('c1', 'C1 Fixed'), ('c3', 'C3 Sent'), ('c4', 'C4 Para')]
    el.append('<text x="275" y="88" text-anchor="middle" font-size="14" font-weight="700" fill="#1e3a8a">'
              'UIT-ViQuAD 2.0 Full (30 cấu hình)</text>')
    x0, y0, cw, ch = 155, 114, 92, 42
    for j, (_, clab) in enumerate(vq_cols):
        el.append(f'<text x="{x0 + j*cw + cw/2}" y="{y0 - 8}" text-anchor="middle" font-size="12" font-weight="600" fill="#374151">{clab}</text>')
    for i, (rlab, fn) in enumerate(vq_rows):
        el.append(f'<text x="{x0 - 8}" y="{y0 + i*ch + 26}" text-anchor="end" font-size="11.5" fill="#374151">{html.escape(rlab)}</text>')
        for j, (ck, _) in enumerate(vq_cols):
            val = vq_m[fn(ck)]['ndcg5']
            bg, fg = _color_heat(val, 0.72, 0.93)
            el.append(f'<rect x="{x0 + j*cw}" y="{y0 + i*ch}" width="{cw-2}" height="{ch-2}" rx="4" fill="{bg}"/>')
            el.append(f'<text x="{x0 + j*cw + (cw-2)/2}" y="{y0 + i*ch + 25}" text-anchor="middle" font-size="12" font-weight="600" fill="{fg}">{val:.4f}</text>')

    # Right panel: Zalo (5 chunks x 6 retriever+rerank)
    zl_m = pa['datasets']['zalo']['methods']
    zl_rows = [
        ('BM25 (R0)', lambda c: f'bm25[{c}][word]'),
        ('BM25 + R1', lambda c: f'bm25[{c}][word]+r1'),
        ('E3 bge-m3 (R0)', lambda c: f'dense[{c}]'),
        ('E3 bge-m3 + R1', lambda c: f'dense[{c}]+r1'),
        ('Hybrid (R0)', lambda c: f'hybrid[{c}][word]'),
        ('Hybrid + R1', lambda c: f'hybrid[{c}][word]+r1'),
    ]
    zl_cols = [('c1', 'C1'), ('c3', 'C3'), ('c4', 'C4'), ('c5', 'C5 (ViStruct)'), ('c5_nohead', 'C5 nohead')]
    el.append('<text x="790" y="88" text-anchor="middle" font-size="14" font-weight="700" fill="#1e3a8a">'
              'Zalo Legal Full (30 cấu hình)</text>')
    zx0, zy0, zcw, zch = 585, 114, 92, 54
    for j, (_, clab) in enumerate(zl_cols):
        el.append(f'<text x="{zx0 + j*zcw + zcw/2}" y="{zy0 - 8}" text-anchor="middle" font-size="11.5" font-weight="600" fill="#374151">{clab}</text>')
    for i, (rlab, fn) in enumerate(zl_rows):
        el.append(f'<text x="{zx0 - 8}" y="{zy0 + i*zch + 31}" text-anchor="end" font-size="11.5" fill="#374151">{html.escape(rlab)}</text>')
        for j, (ck, _) in enumerate(zl_cols):
            val = zl_m[fn(ck)]['ndcg5']
            bg, fg = _color_heat(val, 0.60, 0.84)
            el.append(f'<rect x="{zx0 + j*zcw}" y="{zy0 + i*zch}" width="{zcw-2}" height="{zch-2}" rx="4" fill="{bg}"/>')
            el.append(f'<text x="{zx0 + j*zcw + (zcw-2)/2}" y="{zy0 + i*zch + 31}" text-anchor="middle" font-size="12" font-weight="600" fill="{fg}">{val:.4f}</text>')

    # Highlight box for C5 vs C5_nohead note
    el.append('<rect x="585" y="458" width="460" height="76" rx="8" fill="#eff6ff" stroke="#93c5fd"/>')
    el.append('<text x="600" y="482" font-size="12" font-weight="700" fill="#1e40af">Điểm nhấn Ablation ViStructChunk (Zalo Full, n = 2.167):</text>')
    el.append('<text x="600" y="502" font-size="11.5" fill="#1e3a8a">• C5 (có tiêu đề phân cấp) đạt đỉnh nDCG@5 = 0.8369 (Recall@5 = 90.50%).</text>')
    el.append('<text x="600" y="520" font-size="11.5" fill="#1e3a8a">• Bỏ tiêu đề (C5_nohead) tụt mạnh −0.0940 nDCG@5 (p_Holm &lt; 0.001).</text>')
    el.append('</svg>')
    (fig_dir / 'fig1_full_phase_a_heatmap.svg').write_text('\n'.join(el), encoding='utf-8')


def build_fig2_phase_b_ci(pb):
    fig_dir = Path('reports/figures')
    W, H = 1080, 560
    el = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
        'font-family="Inter, -apple-system, BlinkMacSystemFont, sans-serif">',
        f'<rect width="{W}" height="{H}" fill="#ffffff"/>',
        '<text x="540" y="32" text-anchor="middle" font-size="18" font-weight="700" fill="#111827">'
        'Hình 2: Độ đúng (Correctness 0–2) và Ảo giác (H_gold) kèm khoảng tin cậy 95% Cluster Bootstrap</text>',
        '<text x="540" y="52" text-anchor="middle" font-size="12" fill="#4b5563">'
        'Toàn bộ 18 cấu hình Giai đoạn B: UIT-ViQuAD 2.0 Full (n = 2.653) &amp; Zalo Legal Full (n = 2.167)</text>',
    ]

    panels = [
        ('viquad_full', 'UIT-ViQuAD 2.0 Full (8 cấu hình)', 140, 495,
         ['closed_book', 'C3-E0-R0', 'C1-E3-R0', 'C3-E3-R0', 'C3-E5-R0', 'C3-E3-R1', 'C4-E5-R1', 'oracle']),
        ('zalo_full', 'Zalo Legal Full (10 cấu hình)', 675, 1030,
         ['closed_book', 'C5_nohead-E3-R0', 'C3-E0-R0', 'C3-E3-R0', 'C5-E3-R0', 'C4-E3-R0', 'C3-E5-R0', 'C3-E3-R1', 'C5-E5-R1', 'oracle']),
    ]
    for key, title, x_left, x_right, order in panels:
        cfgs = pb['end_to_end'][key]['configs']
        pw = x_right - x_left
        el.append(f'<text x="{(x_left + x_right)/2}" y="84" text-anchor="middle" font-size="14" font-weight="700" fill="#1e3a8a">{title}</text>')
        # X-axis grid 0.0 to 2.0
        for tick in (0.0, 0.5, 1.0, 1.5, 2.0):
            tx = x_left + (tick / 2.0) * pw
            el.append(f'<line x1="{tx}" y1="100" x2="{tx}" y2="495" stroke="#e5e7eb" stroke-dasharray="3,3"/>')
            el.append(f'<text x="{tx}" y="514" text-anchor="middle" font-size="11" fill="#6b7280">{tick:.1f}</text>')
        el.append(f'<text x="{(x_left + x_right)/2}" y="535" text-anchor="middle" font-size="11.5" font-weight="600" fill="#374151">Correctness (0–2, cao hơn tốt hơn)</text>')

        step = 385 / len(order)
        for i, cname in enumerate(order):
            row = cfgs[cname]
            val = row['correctness']
            lo, hi = row['ci95']['correctness']
            hg = row['h_gold']
            y = 112 + i * step
            bar_h = min(24, step - 10)
            color = '#9ca3af' if cname == 'closed_book' else ('#059669' if cname == 'oracle' else ('#1d4ed8' if cname in ('C4-E5-R1', 'C5-E5-R1', 'C5-E3-R0') else '#3b82f6'))
            bw = (val / 2.0) * pw
            el.append(f'<text x="{x_left - 8}" y="{y + bar_h/2 + 4}" text-anchor="end" font-size="11" font-weight="{"700" if cname in ("C4-E5-R1","C5-E5-R1","C5-E3-R0","oracle") else "400"}" fill="#1f2937">{cname}</text>')
            el.append(f'<rect x="{x_left}" y="{y}" width="{bw:.1f}" height="{bar_h:.1f}" rx="3" fill="{color}" opacity="0.88"/>')
            # CI whisker
            lx, hx = x_left + (lo / 2.0) * pw, x_left + (hi / 2.0) * pw
            cy = y + bar_h / 2
            el.append(f'<line x1="{lx:.1f}" y1="{cy:.1f}" x2="{hx:.1f}" y2="{cy:.1f}" stroke="#111827" stroke-width="1.8"/>')
            el.append(f'<line x1="{lx:.1f}" y1="{cy-4:.1f}" x2="{lx:.1f}" y2="{cy+4:.1f}" stroke="#111827" stroke-width="1.8"/>')
            el.append(f'<line x1="{hx:.1f}" y1="{cy-4:.1f}" x2="{hx:.1f}" y2="{cy+4:.1f}" stroke="#111827" stroke-width="1.8"/>')
            el.append(f'<text x="{hx + 6:.1f}" y="{cy + 4:.1f}" font-size="10.5" fill="#111827">{val:.3f} (H={hg*100:.1f}%)</text>')

    el.append('</svg>')
    (fig_dir / 'fig2_full_phase_b_h_gold_ci.svg').write_text('\n'.join(el), encoding='utf-8')


def build_fig3_rah(pb):
    fig_dir = Path('reports/figures')
    W, H = 1040, 480
    el = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
        'font-family="Inter, -apple-system, BlinkMacSystemFont, sans-serif">',
        f'<rect width="{W}" height="{H}" fill="#ffffff"/>',
        '<text x="520" y="34" text-anchor="middle" font-size="18" font-weight="700" fill="#111827">'
        'Hình 3: Phân rã Ảo giác H_gold = Sàn Oracle (Nội tại LLM) + RAH (Quy cho Truy xuất) theo Miền</text>',
        '<text x="520" y="55" text-anchor="middle" font-size="12" fill="#4b5563">'
        'Trên văn bản pháp luật (Zalo), RAH chiếm 88%–91% tổng ảo giác; trên Wikipedia (ViQuAD), RAH chỉ chiếm 39%–51%</text>',
        # Legend
        '<rect x="300" y="70" width="14" height="14" rx="2" fill="#64748b"/>',
        '<text x="320" y="81" font-size="12" fill="#374151">Ảo giác nền Oracle (nội tại LLM)</text>',
        '<rect x="545" y="70" width="14" height="14" rx="2" fill="#dc2626"/>',
        '<text x="565" y="81" font-size="12" fill="#374151">RAH = H_gold − Oracle (quy cho truy xuất)</text>',
    ]

    panels = [
        ('viquad_full', 'UIT-ViQuAD 2.0 Full (Oracle = 11.01%)', 70, 470,
         ['C3-E0-R0', 'C1-E3-R0', 'C3-E3-R0', 'C3-E5-R0', 'C3-E3-R1', 'C4-E5-R1']),
        ('zalo_full', 'Zalo Legal Full (Oracle = 2.06%)', 540, 1000,
         ['C5_nohead-E3-R0', 'C3-E0-R0', 'C3-E3-R0', 'C4-E3-R0', 'C5-E3-R0', 'C3-E5-R0', 'C3-E3-R1', 'C5-E5-R1']),
    ]
    ymax = 0.28
    y_bot, y_top = 385, 130
    ph = y_bot - y_top
    for key, title, xl, xr, cfgs in panels:
        data = pb['end_to_end'][key]['configs']
        ora = data['oracle']['h_gold']
        el.append(f'<text x="{(xl + xr)/2}" y="112" text-anchor="middle" font-size="13.5" font-weight="700" fill="#1e3a8a">{title}</text>')
        for pct in (0, 5, 10, 15, 20, 25):
            yy = y_bot - (pct / 100.0 / ymax) * ph
            el.append(f'<line x1="{xl}" y1="{yy:.1f}" x2="{xr}" y2="{yy:.1f}" stroke="#e5e7eb" stroke-dasharray="3,3"/>')
            el.append(f'<text x="{xl - 6}" y="{yy + 4:.1f}" text-anchor="end" font-size="10.5" fill="#6b7280">{pct}%</text>')
        bw = min(44, (xr - xl - 20) / len(cfgs) - 10)
        step = (xr - xl) / len(cfgs)
        for i, cname in enumerate(cfgs):
            hg = data[cname]['h_gold']
            rah = max(0.0, hg - ora)
            share = rah / hg * 100
            cx = xl + (i + 0.5) * step
            h_ora = (ora / ymax) * ph
            h_rah = (rah / ymax) * ph
            el.append(f'<rect x="{cx - bw/2:.1f}" y="{y_bot - h_ora:.1f}" width="{bw:.1f}" height="{h_ora:.1f}" fill="#64748b"/>')
            el.append(f'<rect x="{cx - bw/2:.1f}" y="{y_bot - h_ora - h_rah:.1f}" width="{bw:.1f}" height="{h_rah:.1f}" fill="#dc2626" opacity="0.88"/>')
            el.append(f'<text x="{cx:.1f}" y="{y_bot - h_ora - h_rah - 6:.1f}" text-anchor="middle" font-size="10.5" font-weight="700" fill="#991b1b">{share:.0f}%</text>')
            short = cname.replace('-E3-R0', '').replace('C5_nohead', 'C5_nh')
            el.append(f'<text x="{cx:.1f}" y="{y_bot + 16}" text-anchor="middle" font-size="10.5" fill="#1f2937">{short}</text>')
            el.append(f'<text x="{cx:.1f}" y="{y_bot + 30}" text-anchor="middle" font-size="9.5" fill="#6b7280">({hg*100:.1f}%)</text>')

    el.append('<text x="520" y="455" text-anchor="middle" font-size="11" fill="#4b5563">'
              'Ghi chú: Con số màu đỏ trên đỉnh cột là tỷ phần RAH / H_gold (%); số trong ngoặc dưới trục X là tổng H_gold.</text>')
    el.append('</svg>')
    (fig_dir / 'fig3_full_rah_by_domain.svg').write_text('\n'.join(el), encoding='utf-8')


def main():
    pa = build_phase_a_summary()
    pb = build_phase_b_summary()
    build_fig1_heatmap(pa)
    build_fig2_phase_b_ci(pb)
    build_fig3_rah(pb)
    print('=== DONE: reports/full_phase_a_summary.json, reports/full_phase_b_summary.json, and 3 SVG figures ===')
    for ds in ('viquad_full', 'zalo_full'):
        print(f'\n--- {ds} Hypothesis Tests (Correctness, Holm-adjusted) ---')
        for row in pb['comparisons'][ds]:
            if row['metric'] == 'correctness':
                print(f"  {row['label']:<36} diff={row['diff']:+.4f} CI=[{row['diff_ci95'][0]:+.4f}, {row['diff_ci95'][1]:+.4f}] p_Holm={row['p_holm']:.4f}")


if __name__ == '__main__':
    main()
