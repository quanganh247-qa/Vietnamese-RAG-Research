"""Chuẩn bị dữ liệu và tổng hợp benchmark Colab cho cấu hình neo C3–E3–R0."""
import argparse
import hashlib
import json
from pathlib import Path
from statistics import mean, median

from ragvi.data import load_viquad, load_zalo_queries, viquad_questions
from ragvi.generate import summarize_generation
from ragvi.metrics import METRIC_KEYS, mean_metrics
from ragvi.retrieval import load_jsonl, read_rows

ANCHOR = 'C3-E3-R0'
CONFIGS = ('closed_book', 'oracle', ANCHOR)
PHASE_B_CONFIGS = {
    'viquad': ('closed_book', 'oracle', 'C3-E3-R0', 'C1-E3-R0', 'C3-E0-R0', 'C3-E5-R0', 'C3-E3-R1'),
    'zalo': ('closed_book', 'oracle', 'C3-E3-R0', 'C4-E3-R0', 'C5-E3-R0', 'C5_nohead-E3-R0',
             'C3-E0-R0', 'C3-E5-R0', 'C3-E3-R1'),
}
DATASETS = ('viquad', 'zalo')
FROZEN = ('dev', 'test')


def viquad_source_questions(rows):
    labeled = {q['qid']: q for q in viquad_questions(rows)}
    questions = []
    for row in rows:
        qid = f"{row['split']}:{row['id']}"
        questions.append(labeled.get(qid, {'qid': qid, 'question': row['question'], 'answerable': None}))
    if len({q['qid'] for q in questions}) != len(rows):
        raise ValueError('ViQuAD có mã câu hỏi trùng trong cùng split.')
    return questions


def verify_frozen(directory, names):
    hashes = json.loads((directory / 'manifest.json').read_text(encoding='utf-8'))['sha256']
    for name in names:
        if hashlib.sha256((directory / name).read_bytes()).hexdigest() != hashes.get(name):
            raise ValueError(f'Mã SHA-256 không khớp: {directory / name}')


def write_jsonl(path, rows):
    with path.open('w', encoding='utf-8', newline='\n') as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + '\n')


def prepare(data, out):
    out.mkdir(parents=True, exist_ok=True)
    source = viquad_source_questions(load_viquad(data / 'processed/viquad'))
    write_jsonl(out / 'viquad_source.jsonl', source)
    questions, gold = load_zalo_queries(data / 'processed/zalo_legal')
    write_jsonl(out / 'zalo_source.jsonl', (
        {'qid': qid, 'question': text, 'answerable': True, 'gold_doc_ids': sorted(gold[qid])}
        for qid, text in questions.items()))
    for dataset, extra in [('viquad', 'corpus.jsonl'), ('zalo', 'removed_doc_ids.json')]:
        frozen = data / 'eval' / dataset
        verify_frozen(frozen, ('dev.jsonl', 'test.jsonl', extra))
        seen = set()
        for split, expected in [('dev', 100), ('test', 400)]:
            qs = load_jsonl(frozen / f'{split}.jsonl')
            ids = {q['qid'] for q in qs}
            if len(ids) != expected or len(qs) != expected or ids & seen:
                raise ValueError(f'Cỡ tập hoặc mã câu hỏi không hợp lệ: {dataset}/{split}')
            seen |= ids
            write_jsonl(out / f'{dataset}_{split}_oracle.jsonl', (q for q in qs if q['answerable']))


def retrieval_summary(rows, questions):
    want = {q['qid'] for q in questions}
    own = [r for r in rows if r['qid'] in want]
    if len(own) != len(want) or {r['qid'] for r in own} != want:
        raise ValueError('Thiếu hoặc trùng kết quả truy xuất.')
    scored = [r for r in own if r['r5'] is not None]
    if len(scored) != sum(q['answerable'] is True for q in questions):
        raise ValueError('Số câu có nhãn truy xuất không khớp.')
    return {'n': len(own), 'n_scored': len(scored), **(mean_metrics(scored) if scored else dict.fromkeys(METRIC_KEYS))}


def end_to_end_summary(questions, answers, judgments, configs=CONFIGS):
    summaries, hallucinations = {}, {}
    for config in configs:
        own = [a for a in answers if a['config'] == config]
        expected = {q['qid'] for q in questions if config != 'oracle' or q['answerable']}
        if len(own) != len(expected) or {a['qid'] for a in own} != expected:
            raise ValueError(f'Thiếu hoặc trùng câu trả lời cho {config}.')
        judged = {j['qid']: j for j in judgments if j['config'] == config}
        eligible = {a['qid'] for a in own if a['answerable']}
        valid = [j for qid, j in judged.items() if qid in eligible and not j.get('error')]
        generation = summarize_generation(own)
        generation.pop('est_gpu_hours_6400', None)
        summaries[config] = {**generation, 'p50_seconds': median(a['seconds'] for a in own) if own else None,
                             'n_judge_missing': len(eligible - judged.keys()),
                             'n_judge_errors': sum(bool(judged[q].get('error')) for q in eligible & judged.keys())}
        for key in ('correctness', 'h_gold', 'h_ctx'):
            values = {j['qid']: j[key] for j in valid if j.get(key) is not None}
            summaries[config].update({key: mean(values.values()) if values else None, f'n_{key}': len(values)})
            if key == 'h_gold':
                hallucinations[config] = values
        wa_vals = [int(bool(j['wrong_article'])) for j in valid if not j.get('refused') and 'wrong_article' in j]
        if wa_vals:
            summaries[config].update({'wrong_article': mean(wa_vals), 'n_wrong_article': len(wa_vals)})
    oracle = hallucinations.get('oracle', {})
    for config in configs:
        if config not in ('closed_book', 'oracle') and oracle:
            paired = hallucinations.get(config, {}).keys() & oracle.keys()
            summaries[config]['rah_against_oracle'] = {
                'n_pairs': len(paired),
                'value': mean(hallucinations[config][q] - oracle[q] for q in sorted(paired)) if paired else None,
            }
    rag = hallucinations.get(ANCHOR, {})
    paired = rag.keys() & oracle.keys()
    return {'configs': summaries, 'rah_against_oracle': {
        'n_pairs': len(paired), 'value': mean(rag[q] - oracle[q] for q in sorted(paired)) if paired else None}}


def report(data, out):
    retrieval, end_to_end = {}, {}
    for dataset in DATASETS:
        source = load_jsonl(out / f'{dataset}_source.jsonl')
        ranks = read_rows(out / f'retrieval_{dataset}_source.jsonl')
        splits = ('train', 'validation', 'test') if dataset == 'viquad' else ('release_test',)
        retrieval[dataset] = {split: retrieval_summary(ranks, [q for q in source if q['qid'].startswith(split + ':')]
                                                       if dataset == 'viquad' else source) for split in splits}
        for split in FROZEN:
            tag = f'{dataset}_{split}'
            qs = load_jsonl(data / 'eval' / dataset / f'{split}.jsonl')
            retrieval[dataset][f'frozen_{split}'] = retrieval_summary(read_rows(out / f'retrieval_{tag}.jsonl'), qs)
            end_to_end[tag] = end_to_end_summary(qs, read_rows(out / f'answers_{tag}.jsonl'),
                                                read_rows(out / f'judge_{tag}.jsonl'))
    result = {'config': ANCHOR, 'judge_calibrated': False, 'retrieval': retrieval, 'end_to_end': end_to_end}
    (out / 'summary.json').write_text(json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False), encoding='utf-8')


def report_phase_b(data, out):
    end_to_end = {}
    for dataset, cfgs in PHASE_B_CONFIGS.items():
        tag = f'{dataset}_test'
        qs = load_jsonl(data / 'eval' / dataset / 'test.jsonl')
        end_to_end[tag] = end_to_end_summary(
            qs, read_rows(out / f'answers_{tag}.jsonl'), read_rows(out / f'judge_{tag}.jsonl'), configs=cfgs)
    result = {'judge_calibrated': True, 'end_to_end': end_to_end}
    (out / 'phase_b_summary.json').write_text(
        json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False), encoding='utf-8')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=['prepare', 'report', 'phase_b'])
    parser.add_argument('data', type=Path)
    parser.add_argument('out', type=Path)
    args = parser.parse_args()
    {'prepare': prepare, 'report': report, 'phase_b': report_phase_b}[args.action](args.data, args.out)
