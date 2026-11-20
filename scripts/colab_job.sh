#!/usr/bin/env bash
# Chỉ chạy trong runtime Colab, từ thư mục gốc của mã đã tải lên.
set -euo pipefail
mode=$1
out=$2
export PYTHONUTF8=1 PYTHONUNBUFFERED=1 HF_HUB_DISABLE_XET=1 OPENBLAS_NUM_THREADS=1
if ! command -v uv >/dev/null; then
  curl -fsSL --retry 3 https://astral.sh/uv/install.sh | env UV_INSTALL_DIR=/content/.local/bin UV_NO_MODIFY_PATH=1 sh
  export PATH="/content/.local/bin:$PATH"
fi

if [[ $mode == eda ]]; then
  uv sync --locked --python 3.12 --no-dev --extra eda
  if [[ ! -d data/processed ]]; then
    uv run --no-sync gdown --no-cookies --timeout 60 --retries 2 --continue -O data \
      "${RAGVI_DRIVE_URL:?Thiếu URL thư mục dữ liệu chia sẻ.}"
  fi
  RAGVI_DATA_DIR="$PWD/data" uv run --no-sync jupyter nbconvert --to notebook --execute \
    --output eda.ipynb --output-dir "$out" --ExecutePreprocessor.timeout=1800 notebooks/06_eda_du_lieu.ipynb
  exit 0
fi

nvidia-smi | tee "$out/gpu.txt"
cap=$(nvidia-smi --query-gpu=compute_cap --format=csv,noheader | head -n1)
[[ $cap =~ ^[0-9]+\.[0-9]+$ ]]
if ! command -v nvcc >/dev/null && [[ -x /usr/local/cuda/bin/nvcc ]]; then
  export PATH="/usr/local/cuda/bin:$PATH"
fi
if ! command -v nvcc >/dev/null; then
  echo 'Runtime GPU thiếu trình biên dịch CUDA (nvcc).' >&2
  exit 1
fi
uv sync --locked --python 3.12 --no-dev --extra rag

py=(uv run --no-sync python -m)
corpus=data/eval/viquad/corpus.jsonl
retrieval=/content/retrieval
if [[ $mode == benchmark ]]; then
  "${py[@]}" ragvi.benchmark prepare data "$out"
  for dataset in viquad zalo; do
    units=$corpus
    if [[ $dataset == zalo ]]; then units=data/processed/zalo_legal; fi
    for split in source dev test; do
      tag=${dataset}_$split
      questions=data/eval/$dataset/$split.jsonl
      if [[ $split == source ]]; then questions=$out/${tag}.jsonl; fi
      removed=()
      if [[ $tag == zalo_test ]]; then removed=(--removed data/eval/zalo/removed_doc_ids.json); fi
      echo "=== Truy xuất $tag ==="
      time "${py[@]}" ragvi.retrieval "$units" "$retrieval" --questions "$questions" \
        --methods dense --chunking c3 --run "$tag" "${removed[@]}"
      cp "$retrieval/retrieval_$tag.jsonl" "$out/"
    done
  done
else
# Pilot cố định: 5 câu có và 5 câu không có đáp án; oracle chỉ chạy nhóm có đáp án (D5).
uv run --no-sync python - "$out" <<'PY'
import json
from pathlib import Path
import sys
from ragvi.retrieval import load_jsonl

out = Path(sys.argv[1])
dev = load_jsonl('data/eval/viquad/dev.jsonl')
yes = [q for q in dev if q['answerable']][:5]
no = [q for q in dev if not q['answerable']][:5]
assert len(yes) == len(no) == 5, 'Tập dev không đủ câu hỏi cho pilot.'
for name, rows in [('questions', yes + no), ('oracle_questions', yes)]:
    (out / f'{name}.jsonl').write_text(''.join(json.dumps(q, ensure_ascii=False) + '\n' for q in rows), encoding='utf-8')
PY
"${py[@]}" ragvi.retrieval "$corpus" "$retrieval" \
  --questions "$out/questions.jsonl" --methods dense --chunking c3 --run viquad_dev_pilot
cp "$retrieval/retrieval_viquad_dev_pilot.jsonl" "$out/retrieval.jsonl"
fi

llama_ref=3837bf0bc02ea5d08f8ee3585fc8c7784a81bce8  # b12248
model_repo=Qwen/Qwen2.5-7B-Instruct-GGUF
model_revision=bb5d59e06d9551d752d08b292a50eb208b07ab1f
model_alias="$model_repo:Q4_K_M"
git init -q /content/llama.cpp
git -C /content/llama.cpp fetch -q --depth 1 https://github.com/ggml-org/llama.cpp.git "$llama_ref"
git -C /content/llama.cpp checkout -q --detach FETCH_HEAD
cmake -S /content/llama.cpp -B /content/llama.cpp/build -DCMAKE_BUILD_TYPE=Release \
  -DGGML_CUDA=ON -DCMAKE_CUDA_ARCHITECTURES="${cap/.}" -DLLAMA_BUILD_TESTS=OFF -DLLAMA_BUILD_EXAMPLES=OFF
cmake --build /content/llama.cpp/build --target llama-server --parallel 2

mkdir -p /content/models
for part in 00001 00002; do
  file="qwen2.5-7b-instruct-q4_k_m-$part-of-00002.gguf"
  curl -fL --retry 3 -o "/content/models/$file" "https://huggingface.co/$model_repo/resolve/$model_revision/$file"
done
printf 'llama.cpp=%s\nmodel=%s\nrevision=%s\n' "$llama_ref" "$model_alias" "$model_revision" > "$out/model.txt"
base=http://127.0.0.1:8080
start_server() {
  local alias=$1 gguf=$2 ctx=$3 log=$4
  shift 4
  /content/llama.cpp/build/bin/llama-server --host 127.0.0.1 --port 8080 --device CUDA0 --n-gpu-layers 99 \
    --ctx-size "$ctx" --parallel 1 --alias "$alias" --model "$gguf" "$@" > "$log" 2>&1 &
  server=$!
  trap 'kill "$server" 2>/dev/null || true' EXIT
  local i
  for ((i=0; i<180; i++)); do
    if curl -fsS "$base/health" >/dev/null 2>&1; then return; fi
    kill -0 "$server" 2>/dev/null || break
    sleep 2
  done
  tail -n 40 "$log" >&2
  return 1
}

ctx=8192
if [[ $mode == benchmark ]]; then ctx=32768; fi
start_server "$model_alias" /content/models/qwen2.5-7b-instruct-q4_k_m-00001-of-00002.gguf "$ctx" "$out/llama-server.log"
model=(--llama-url "$base" --model "$model_alias")
run=("${py[@]}" ragvi.generate)
if [[ $mode == rag ]]; then
  "${run[@]}" "$out/questions.jsonl" "$corpus" "$out/answers.jsonl" --config closed_book "${model[@]}"
  "${run[@]}" "$out/oracle_questions.jsonl" "$corpus" "$out/answers.jsonl" --config oracle "${model[@]}"
  "${run[@]}" "$out/questions.jsonl" "$retrieval/chunks/viquad__c3.jsonl" "$out/answers.jsonl" \
    --config C3-E3-R0 --retrieval "$out/retrieval.jsonl" --method 'dense[c3]' "${model[@]}"
  exit 0
fi

for dataset in viquad zalo; do
  units=$corpus
  chunks=$retrieval/chunks/viquad__c3.jsonl
  if [[ $dataset == zalo ]]; then units=data/processed/zalo_legal; chunks=$retrieval/chunks/zalo_legal__c3.jsonl; fi
  for split in dev test; do
    tag=${dataset}_$split
    qs=data/eval/$dataset/$split.jsonl
    answers=$out/answers_$tag.jsonl
    echo "=== Sinh câu trả lời $tag ==="
    "${run[@]}" "$qs" "$units" "$answers" --config closed_book "${model[@]}"
    "${run[@]}" "$out/${tag}_oracle.jsonl" "$units" "$answers" --config oracle "${model[@]}"
    "${run[@]}" "$qs" "$chunks" "$answers" --config C3-E3-R0 "${model[@]}" \
      --retrieval "$out/retrieval_$tag.jsonl" --method 'dense[c3]'
  done
done

kill "$server"
wait "$server" || true
trap - EXIT
judge_repo=Qwen/Qwen3-8B-GGUF
judge_revision=7c41481f57cb95916b40956ab2f0b139b296d974
judge_alias="$judge_repo:Q4_K_M"
judge_gguf=/content/models/Qwen3-8B-Q4_K_M.gguf
curl -fL --retry 3 -o "$judge_gguf" "https://huggingface.co/$judge_repo/resolve/$judge_revision/${judge_gguf##*/}"
printf 'judge=%s\njudge_revision=%s\n' "$judge_alias" "$judge_revision" >> "$out/model.txt"
start_server "$judge_alias" "$judge_gguf" 8192 "$out/judge-server.log" --jinja --chat-template-kwargs '{"enable_thinking":false}'
for dataset in viquad zalo; do
  units=$corpus
  chunks=$retrieval/chunks/viquad__c3.jsonl
  if [[ $dataset == zalo ]]; then units=data/processed/zalo_legal; chunks=$retrieval/chunks/zalo_legal__c3.jsonl; fi
  for split in dev test; do
    tag=${dataset}_$split
    echo "=== Judge sơ bộ $tag (chưa hiệu chỉnh) ==="
    "${py[@]}" ragvi.judge "$out/answers_$tag.jsonl" "data/eval/$dataset/$split.jsonl" "$units" "$out/judge_$tag.jsonl" \
      --chunks "$chunks" --model "$judge_alias" --llama-url "$base"
  done
done
"${py[@]}" ragvi.benchmark report data "$out"
