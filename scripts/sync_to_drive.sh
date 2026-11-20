#!/bin/bash
# Đồng bộ mã (src/, tests/) từ máy lên thư mục dự án trên Google Drive để Colab dùng.
#
#   scripts/sync_to_drive.sh        đồng bộ
#   scripts/sync_to_drive.sh -n     chỉ xem trước, không ghi gì
#
# Cần Google Drive for desktop đã đăng nhập. Nếu thư mục dự án trên Drive không nằm ở
# "My Drive/Vietnamese-RAG-Research", đặt DRIVE_DIR=<đường dẫn thư mục dự án trên Drive>.
#
# Chỉ đồng bộ một chiều máy -> Drive, và chỉ hai thư mục src/ và tests/. File bị xóa trên máy
# cũng bị xóa trong hai thư mục đó trên Drive. Không đụng tới data/ và notebooks/ trên Drive.
set -euo pipefail
cd "$(dirname "$0")/.."

if [[ -z "${DRIVE_DIR:-}" ]]; then
  for dir in "$HOME"/Library/CloudStorage/GoogleDrive-*/{"My Drive","Drive của tôi"}/Vietnamese-RAG-Research; do
    if [[ -d "$dir" ]]; then DRIVE_DIR="$dir"; break; fi
  done
fi
if [[ ! -d "${DRIVE_DIR:-}" ]]; then
  echo "Không tìm thấy thư mục dự án trên Google Drive." >&2
  echo "Cài Google Drive for desktop và đăng nhập, hoặc chạy: DRIVE_DIR=<đường dẫn> $0" >&2
  exit 1
fi

rsync -av --delete --exclude '__pycache__/' --exclude '.DS_Store' "$@" src tests "$DRIVE_DIR/"
echo "Thư mục đích: $DRIVE_DIR"
