#!/usr/bin/env bash
# Máy người dùng: Git Bash hoặc Bash + uv. Không dùng WSL hay SSH.
set -euo pipefail
cd "$(dirname "$0")"

mode=${1:-rag}
if [[ -n "${2:-}" ]]; then RAGVI_DRIVE_URL="$2"; fi
case "$mode" in
  -h|--help) echo 'Cách dùng: bash colab_run.sh [rag|benchmark|phase_a|phase_b|eda]'; exit 0 ;;
  rag|benchmark|phase_a|phase_b|eda) ;;
  *) echo 'Chọn rag (mặc định), benchmark, phase_a, phase_b hoặc eda.' >&2; exit 2 ;;
esac
job_env=(--env "RAGVI_JOB_MODE=$mode")
if [[ $mode == eda ]]; then
  : "${RAGVI_DRIVE_URL:?Đặt RAGVI_DRIVE_URL thành URL thư mục dữ liệu chia sẻ.}"
fi
if [[ -n "${RAGVI_DRIVE_URL:-}" ]]; then
  job_env+=(--env "RAGVI_DRIVE_URL=$RAGVI_DRIVE_URL")
fi
export PATH="$PATH:$HOME/.local/bin"
if ! command -v uvx >/dev/null; then
  echo 'Cần cài uv và thêm uvx vào PATH: https://docs.astral.sh/uv/getting-started/installation/' >&2
  exit 1
fi

export PYTHONUTF8=1 PYTHONIOENCODING=utf-8
cli=(uvx --python 3.12 --from google-colab-cli==0.8.0 colab)
tmp=$(mktemp -d)
session="ragvi-$mode-$$-$RANDOM"
allocated=0
cleanup() {
  local rc=$?
  if (( allocated )) && ! "${cli[@]}" stop -s "$session"; then
    echo "Không dừng được runtime. Chạy: ${cli[*]} stop -s $session" >&2
    rc=1
  fi
  rm -rf -- "$tmp"
  exit "$rc"
}
trap cleanup EXIT
trap 'exit 130' INT
trap 'exit 143' TERM

files=(pyproject.toml uv.lock src/ragvi scripts/colab_job.sh)
case "$mode" in
  rag)
    if [[ -f data/eval/viquad/dev.jsonl ]]; then
      files+=(data/eval/viquad/{dev,corpus}.jsonl)
    else
      : "${RAGVI_DRIVE_URL:?Thư mục data/ cục bộ trống; hãy đặt RAGVI_DRIVE_URL thành URL thư mục dữ liệu Drive chia sẻ.}"
    fi ;;
  benchmark|phase_a|phase_b)
    if [[ -d data/retrieval_cache ]]; then
      files+=(data/retrieval_cache)
    fi
    if [[ -d data/processed/viquad ]]; then
      files+=(data/processed/{viquad,zalo_legal} data/eval/viquad/{dev,test,corpus}.jsonl
        data/eval/zalo/{dev,test}.jsonl data/eval/{viquad,zalo}/manifest.json data/eval/zalo/removed_doc_ids.json)
    else
      : "${RAGVI_DRIVE_URL:?Thư mục data/ cục bộ trống; hãy đặt RAGVI_DRIVE_URL thành URL thư mục dữ liệu Drive chia sẻ.}"
    fi ;;
  eda) files+=(notebooks/06_eda_du_lieu.ipynb) ;;
esac
# Chỉ tải lên đầu vào cần thiết; chia gói > 15 MB thành các phần nhỏ để không vượt giới hạn PUT của Colab proxy.
extra_excludes=()
if [[ $mode == phase_a ]]; then
  extra_excludes+=(
    --exclude='data/retrieval_cache/llama-bin-*.tar.gz'
    --exclude='data/retrieval_cache/retrieval_viquad_source.jsonl'
    --exclude='data/retrieval_cache/retrieval_zalo_source.jsonl'
    --exclude='data/retrieval_cache/answers_*.jsonl'
    --exclude='data/retrieval_cache/judge_*.jsonl'
  )
elif [[ $mode == phase_b ]]; then
  extra_excludes+=(
    --exclude='data/retrieval_cache/retrieval_viquad_source.jsonl'
    --exclude='data/retrieval_cache/retrieval_zalo_source.jsonl'
    --exclude='data/retrieval_cache/retrieval_viquad_dev.jsonl'
    --exclude='data/retrieval_cache/retrieval_zalo_dev.jsonl'
    --exclude='data/retrieval_cache/retrieval_viquad_test.jsonl'
    --exclude='data/retrieval_cache/retrieval_zalo_test.jsonl'
    --exclude='data/retrieval_cache/answers_viquad_dev.jsonl'
    --exclude='data/retrieval_cache/answers_zalo_dev.jsonl'
    --exclude='data/retrieval_cache/judge_viquad_dev.jsonl'
    --exclude='data/retrieval_cache/judge_zalo_dev.jsonl'
  )
fi
tar -czf "$tmp/project.tar.gz" --exclude='__pycache__' --exclude='zalo_legal__c3.jsonl' "${extra_excludes[@]}" "${files[@]}"
archive="$tmp/project.tar.gz"
if command -v cygpath >/dev/null; then archive=$(cygpath -m "$archive"); fi

if [[ $mode != eda ]]; then
  for gpu in G4 A100 L4 T4; do
    if "${cli[@]}" new -s "$session" --gpu "$gpu" 2>&1 | tee "$tmp/allocation.log"; then
      allocated=1
      break
    fi
    # Google đôi khi trả 503 ở POST cấp máy thay vì báo từ chối accelerator.
    if ! grep -Eq '\[colab\] (Allocation refused|Backend rejected accelerator)' "$tmp/allocation.log" &&
       ! { grep -Fq 'Failed to issue request POST' "$tmp/allocation.log" &&
           grep -Fq '/tun/m/assign?' "$tmp/allocation.log" &&
           grep -Eq ': (Bad Gateway|Service Unavailable|Gateway Timeout)' "$tmp/allocation.log"; }; then
      exit 1
    fi
  done
  if (( !allocated )); then
    echo 'Colab không cấp được G4, A100, L4 hoặc T4.' >&2
    exit 1
  fi
else
  "${cli[@]}" new -s "$session"
  allocated=1
fi

if [[ $(wc -c < "$tmp/project.tar.gz") -gt 15728640 ]]; then
  split -b 15m "$tmp/project.tar.gz" "$tmp/ragvi-part."
  for part in "$tmp"/ragvi-part.*; do
    part_path=$part
    if command -v cygpath >/dev/null; then part_path=$(cygpath -m "$part_path"); fi
    "${cli[@]}" upload -s "$session" "$part_path" "content/${part##*/}"
  done
else
  "${cli[@]}" upload -s "$session" "$archive" content/ragvi-project.tar.gz
fi
job_rc=0
"${cli[@]}" exec -s "$session" --timeout 0 "${job_env[@]}" <<'PY' || job_rc=$?
import os
from pathlib import Path
import shutil
import subprocess
import tarfile

project = Path('/content/ragvi-project')
out = Path('/content/ragvi-output')
out.mkdir()
parts = sorted(Path('/content').glob('ragvi-part.*'))
if parts:
    with open('/content/ragvi-project.tar.gz', 'wb') as dst:
        for part in parts:
            dst.write(part.read_bytes())
            part.unlink()
with tarfile.open('/content/ragvi-project.tar.gz') as bundle:
    bundle.extractall(project, filter='data')
with subprocess.Popen(['bash', 'scripts/colab_job.sh', os.environ['RAGVI_JOB_MODE'], str(out)],
                      cwd=project, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                      text=True, encoding='utf-8', errors='replace') as proc, (out / 'job.log').open('w', encoding='utf-8') as log:
    for line in proc.stdout:
        log.write(line)
        print(line, end='', flush=True)
    rc = proc.wait()
(out / 'exit_code.txt').write_text(str(rc), encoding='ascii')
shutil.make_archive('/content/ragvi-results', 'gztar', out)
PY

mkdir -p results/colab
out=$(mktemp -d "results/colab/$mode-XXXXXXXX")
if ! "${cli[@]}" download -s "$session" content/ragvi-results.tar.gz "$out/results.tar.gz"; then
  echo "Không lấy được kết quả Colab (mã thực thi CLI: $job_rc)." >&2
  exit 1
fi
tar -xzf "$out/results.tar.gz" -C "$out"
rm -- "$out/results.tar.gz"
echo "Kết quả và log: $out/"
if [[ $job_rc != 0 || ! -f "$out/exit_code.txt" || $(<"$out/exit_code.txt") != 0 ]]; then
  echo "Lượt chạy Colab lỗi. Xem $out/job.log." >&2
  exit 1
fi
