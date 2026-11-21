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
uv sync --locked --python 3.12 --no-dev --extra rag --extra eda
if [[ ! -d data/processed && -n "${RAGVI_DRIVE_URL:-}" ]]; then
  uv run --no-sync gdown --no-cookies --timeout 60 --retries 2 --continue -O data "$RAGVI_DRIVE_URL"
fi

py=(uv run --no-sync python -m)
corpus=data/eval/viquad/corpus.jsonl
retrieval=/content/retrieval
mkdir -p "$retrieval/chunks"
if [[ -d data/retrieval_cache ]]; then
  cp data/retrieval_cache/retrieval_*.jsonl "$retrieval/" 2>/dev/null || true
  cp data/retrieval_cache/chunks/*.jsonl "$retrieval/chunks/" 2>/dev/null || true
  cp data/retrieval_cache/answers_*.jsonl data/retrieval_cache/judge_*.jsonl "$out/" 2>/dev/null || true
fi
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
  if [[ ! -f data/retrieval_cache/chunks/zalo_legal__c3.jsonl ]]; then
    mkdir -p "$out/chunks"
    cp "$retrieval/chunks/"*.jsonl "$out/chunks/" 2>/dev/null || true
  fi
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
model_repo=unsloth/Qwen3.5-9B-GGUF
model_revision=1daf391c47cef14242f238b819fbe6fd500d624b
model_alias="$model_repo:Q4_K_M"
model_gguf=/content/models/Qwen3.5-9B-Q4_K_M.gguf
llama_bin_cache=data/retrieval_cache/llama-bin-${cap/.}.tar.gz
if [[ -f $llama_bin_cache ]]; then
  mkdir -p /content/llama.cpp/build/bin
  tar -xzf "$llama_bin_cache" -C /content/llama.cpp/build/bin
else
  git init -q /content/llama.cpp
  git -C /content/llama.cpp fetch -q --depth 1 https://github.com/ggml-org/llama.cpp.git "$llama_ref"
  git -C /content/llama.cpp checkout -q --detach FETCH_HEAD
  if [[ -f /content/llama.cpp/scripts/ui-assets.cmake ]]; then
    sed -i 's/message(FATAL_ERROR/message(WARNING/g' /content/llama.cpp/scripts/ui-assets.cmake
  fi
  cmake -S /content/llama.cpp -B /content/llama.cpp/build -DCMAKE_BUILD_TYPE=Release \
    -DGGML_CUDA=ON -DCMAKE_CUDA_ARCHITECTURES="${cap/.}" -DCMAKE_CUDA_FLAGS="--threads 4" \
    -DLLAMA_BUILD_TESTS=OFF -DLLAMA_BUILD_EXAMPLES=OFF
  cmake --build /content/llama.cpp/build --target llama-server --parallel "$(nproc)"
  tar -czf "$out/llama-bin-${cap/.}.tar.gz" -C /content/llama.cpp/build/bin .
fi

mkdir -p /content/models
curl -fL --retry 3 -o "$model_gguf" "https://huggingface.co/$model_repo/resolve/$model_revision/${model_gguf##*/}"
printf 'llama.cpp=%s\nmodel=%s\nrevision=%s\njudge=%s\njudge_revision=%s\n' \
  "$llama_ref" "$model_alias" "$model_revision" "$model_alias" "$model_revision" > "$out/model.txt"
base=http://127.0.0.1:18080
start_server() {
  local alias=$1 gguf=$2 ctx=$3 slots=$4 log=$5
  shift 5
  LD_LIBRARY_PATH=/content/llama.cpp/build/bin:${LD_LIBRARY_PATH:-} \
    /content/llama.cpp/build/bin/llama-server --host 127.0.0.1 --port 18080 --device CUDA0 --n-gpu-layers 99 \
    --ctx-size "$ctx" --parallel "$slots" --cont-batching --batch-size 2048 --ubatch-size 512 \
    --alias "$alias" --model "$gguf" "$@" > "$log" 2>&1 &
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

vram_mib=$(nvidia-smi --query-gpu=memory.total --format=csv,noheader,nounits | head -n1 | tr -d ' ')
slots=6
if [[ "${vram_mib:-0}" -ge 20000 ]]; then slots=12; fi
ctx=$((4096 * slots))
start_server "$model_alias" "$model_gguf" "$ctx" "$slots" "$out/llama-server.log" \
  --jinja --chat-template-kwargs '{"enable_thinking":false}'
model=(--llama-url "$base" --model "$model_alias" --workers "$slots")
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
    echo "=== Sinh câu trả lời $tag (parallel slots=$slots) ==="
    "${run[@]}" "$qs" "$units" "$answers" --config closed_book "${model[@]}"
    "${run[@]}" "$out/${tag}_oracle.jsonl" "$units" "$answers" --config oracle "${model[@]}"
    "${run[@]}" "$qs" "$chunks" "$answers" --config C3-E3-R0 "${model[@]}" \
      --retrieval "$out/retrieval_$tag.jsonl" --method 'dense[c3]'
  done
done

for dataset in viquad zalo; do
  units=$corpus
  chunks=$retrieval/chunks/viquad__c3.jsonl
  if [[ $dataset == zalo ]]; then units=data/processed/zalo_legal; chunks=$retrieval/chunks/zalo_legal__c3.jsonl; fi
  for split in dev test; do
    tag=${dataset}_$split
    echo "=== Judge sơ bộ $tag (chưa hiệu chỉnh, parallel slots=$slots) ==="
    "${py[@]}" ragvi.judge "$out/answers_$tag.jsonl" "data/eval/$dataset/$split.jsonl" "$units" "$out/judge_$tag.jsonl" \
      --chunks "$chunks" "${model[@]}"
  done
done
"${py[@]}" ragvi.benchmark report data "$out"
