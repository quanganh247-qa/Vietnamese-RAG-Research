"""Dựng tập đánh giá mở rộng Full (Phương án B: 3.096 câu Zalo Legal + 3.814 câu validation ViQuAD).

Giữ nguyên 100 câu dev đã dùng để hiệu chỉnh Judge (κ = 0,8163) ở ngoài tập test để đảm bảo 0% rò rỉ dữ liệu.
"""
import hashlib
import json
from pathlib import Path
import random

from ragvi.data import expand_zalo_doc_ids, gold_groups


def sha256_file(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def write_jsonl(path, rows):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with Path(path).open('w', encoding='utf-8', newline='\n') as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + '\n')


def build_zalo_full():
    raw = json.loads(Path('data/raw/train_question_answer.json').read_text(encoding='utf-8'))
    items = raw['items'] if isinstance(raw, dict) and 'items' in raw else raw
    by_qid = {it['question_id']: it for it in items}
    gold_map = {qid: {f"{a['law_id']}+{a['article_id']}".lower() for a in it['relevant_articles']}
                for qid, it in by_qid.items()}

    dev_qids = {json.loads(line)['qid']
                for line in Path('results/colab/benchmark-Pa3Gy3aM/zalo_dev_oracle.jsonl').read_text(encoding='utf-8').splitlines()
                if line.strip()}
    grps = gold_groups(gold_map)
    rem_grps = [g for g in grps if not (set(g) & dev_qids)]
    assert sum(len(g) for g in rem_grps) == 3096

    # Xáo nhóm bằng seed=0, lấy ~30% (929 câu) làm unanswerable và ~70% (2.167 câu) làm answerable
    rng = random.Random(0)
    rng.shuffle(rem_grps)
    target_unans = round(3096 * 0.30)  # 929
    unans_qids, ans_qids, group_of = [], [], {}
    for idx, g in enumerate(rem_grps):
        for qid in g:
            group_of[qid] = idx
        if len(unans_qids) + len(g) <= target_unans:
            unans_qids.extend(g)
        else:
            ans_qids.extend(g)

    corpus_docs = set()
    with Path('data/retrieval_cache/chunks/zalo_legal__c3.jsonl').open(encoding='utf-8') as f:
        for line in f:
            corpus_docs.add(json.loads(line)[1])

    removed_raw = set().union(*(gold_map[q] for q in unans_qids))
    removed = sorted(expand_zalo_doc_ids(removed_raw, corpus=corpus_docs))
    kept_gold = set().union(*(gold_map[q] for q in ans_qids))
    assert not (kept_gold & set(removed)), 'Rò rỉ điều luật vàng giữa answerable và unanswerable!'

    test_rows = [
        {
            'qid': q,
            'question': by_qid[q]['question'],
            'answerable': True,
            'gold_doc_ids': sorted(gold_map[q]),
            'group': group_of[q],
        }
        for q in ans_qids
    ] + [
        {
            'qid': q,
            'question': by_qid[q]['question'],
            'answerable': False,
            'gold_doc_ids': sorted(gold_map[q]),
            'group': group_of[q],
        }
        for q in unans_qids
    ]
    out_dir = Path('data/eval_full/zalo')
    write_jsonl(out_dir / 'test.jsonl', test_rows)
    write_jsonl(out_dir / 'test_oracle.jsonl', [r for r in test_rows if r['answerable']])
    (out_dir / 'removed_doc_ids.json').write_text(json.dumps(removed, ensure_ascii=False, indent=0), encoding='utf-8')
    manifest = {
        'dataset': 'zalo_legal_full',
        'source': 'zac2021-ltr-data/train_question_answer.json (3196 unique - 100 dev = 3096 test)',
        'seed': 0,
        'n_test': len(test_rows),
        'n_answerable': len(ans_qids),
        'n_unanswerable': len(unans_qids),
        'n_groups': len(rem_grps),
        'n_removed_docs': len(removed),
        'sha256': {
            'test.jsonl': sha256_file(out_dir / 'test.jsonl'),
            'removed_doc_ids.json': sha256_file(out_dir / 'removed_doc_ids.json'),
        },
    }
    (out_dir / 'manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print('Zalo full:', json.dumps(manifest, ensure_ascii=False))


def build_viquad_full():
    dev_titles = {json.loads(line)['title']
                  for line in Path('results/colab/benchmark-Pa3Gy3aM/viquad_dev_oracle.jsonl').read_text(encoding='utf-8').splitlines()
                  if line.strip()}
    val_rows = [json.loads(line)
                for line in Path('results/colab/benchmark-Pa3Gy3aM/viquad_source.jsonl').read_text(encoding='utf-8').splitlines()
                if line.strip() and json.loads(line)['qid'].startswith('validation:')]
    val_titles = {r['title'] for r in val_rows}
    assert not (dev_titles & val_titles), 'Trùng title giữa dev và validation!'

    out_dir = Path('data/eval_full/viquad')
    write_jsonl(out_dir / 'test.jsonl', val_rows)
    write_jsonl(out_dir / 'test_oracle.jsonl', [r for r in val_rows if r['answerable']])
    manifest = {
        'dataset': 'viquad_validation_full',
        'source': 'UIT-ViQuAD 2.0 validation split (3814 labeled questions, 0 title overlap with dev)',
        'seed': 0,
        'n_test': len(val_rows),
        'n_answerable': sum(bool(r['answerable']) for r in val_rows),
        'n_unanswerable': sum(not r['answerable'] for r in val_rows),
        'n_titles': len(val_titles),
        'sha256': {
            'test.jsonl': sha256_file(out_dir / 'test.jsonl'),
        },
    }
    (out_dir / 'manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print('ViQuAD full:', json.dumps(manifest, ensure_ascii=False))


if __name__ == '__main__':
    build_zalo_full()
    build_viquad_full()
