import os
import json
from pathlib import Path

ROOT = Path("data/raw")


def inspect_folder(folder):
    print(f"\n{'=' * 50}")
    print(f"DATASET: {folder}")
    print("=" * 50)

    for file in Path(folder).rglob("*"):
        if file.is_file():
            print(f"{file.name:40s} " f"{file.stat().st_size / 1024:.2f} KB")

            if file.suffix == ".json":
                try:
                    with open(file, encoding="utf-8") as f:
                        data = json.load(f)

                    print("  Type:", type(data).__name__)

                    if isinstance(data, dict):
                        print("  Keys:", list(data.keys()))

                    elif isinstance(data, list):
                        print("  Records:", len(data))
                        if data:
                            print("  First record:", data[0])

                except Exception as e:
                    print("  Error:", e)


for dataset in ["viquad", "zalo_legal"]:
    folder = ROOT / dataset

    if folder.exists():
        inspect_folder(folder)
    else:
        print(f"Missing folder: {folder}")
