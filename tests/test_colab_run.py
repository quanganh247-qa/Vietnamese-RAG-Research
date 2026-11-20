import os
import shutil
import subprocess
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
BASH = shutil.which('bash')


@pytest.mark.skipif(not BASH, reason='Kiểm thử cần Bash')
@pytest.mark.parametrize(('scenario', 'expected', 'success'), [
    ('success', ['new G4', 'new A100', 'new L4', 'new T4', 'upload', 'exec', 'download', 'stop'], True),
    ('auth', ['new G4'], False),
    ('service_unavailable', ['new G4', 'new A100', 'upload', 'exec', 'download', 'stop'], True),
    ('unrelated_503', ['new G4'], False),
    ('job_error', ['new G4', 'upload', 'exec', 'download', 'stop'], False),
    ('stop_error', ['new G4', 'upload', 'exec', 'download', 'stop'], False),
    ('no_gpu', ['new G4', 'new A100', 'new L4', 'new T4'], False),
    ('eda', ['new CPU', 'upload', 'exec', 'download', 'stop'], True),
    ('benchmark', ['new G4', 'upload', 'exec', 'download', 'stop'], True),
])
def test_colab_allocation_fallback_and_cleanup(tmp_path, scenario, expected, success):
    script = ROOT / 'colab_run.sh'
    assert script.is_file(), 'Thiếu colab_run.sh'
    shutil.copyfile(script, tmp_path / script.name)
    for name in ('src/ragvi/__init__.py', 'scripts/colab_job.sh', 'pyproject.toml', 'uv.lock',
                 'data/eval/viquad/dev.jsonl', 'data/eval/viquad/corpus.jsonl', 'notebooks/06_eda_du_lieu.ipynb',
                 'data/eval/viquad/test.jsonl', 'data/eval/viquad/manifest.json', 'data/eval/zalo/manifest.json',
                 'data/eval/zalo/dev.jsonl', 'data/eval/zalo/test.jsonl', 'data/eval/zalo/removed_doc_ids.json',
                 'data/eval/zalo/reserve.jsonl', 'data/processed/viquad/train/data.arrow',
                 'data/processed/zalo_legal/queries/data.arrow'):
        p = tmp_path / name
        p.parent.mkdir(parents=True, exist_ok=True)
        p.touch()
    cli = tmp_path / 'uvx'
    cli.write_text('''#!/usr/bin/env bash
SCENARIO=__SCENARIO__
while [[ $1 != colab ]]; do shift; done
shift
case "$1" in
  new)
    echo "new ${5:-CPU}" >> calls
    if [[ $SCENARIO == auth ]]; then echo 'Unauthorized' >&2; exit 1; fi
    if [[ $SCENARIO == unrelated_503 ]]; then echo 'Service Unavailable' >&2; exit 1; fi
    if [[ $SCENARIO == service_unavailable && $5 == G4 ]]; then
      echo 'ColabRequestError: Failed to issue request POST' >&2
      echo 'https://colab.research.google.com/tun/m/assign?nbh=fixture&variant=GPU&accelerator=G4: Service Unavailable' >&2
      exit 1
    fi
    if [[ $SCENARIO == no_gpu || ( $SCENARIO == success && $5 != T4 ) ]]; then
      if [[ $5 == A100 ]]; then
        echo "[colab] Backend rejected accelerator '$5'." >&2
      else
        echo '[colab] Allocation refused (precondition failed).' >&2
      fi
      exit 1
    fi ;;
  upload)
    echo upload >> calls
    [[ $5 == content/ragvi-project.tar.gz ]] || exit 96
    if [[ $SCENARIO == benchmark ]]; then
      archive=$4
      if command -v cygpath >/dev/null; then archive=$(cygpath -u "$archive"); fi
      tar -tzf "$archive" > bundle
    fi ;;
  exec)
    echo exec >> calls
    if [[ $SCENARIO == eda ]]; then
      [[ " $* " == *' --env RAGVI_DRIVE_URL=https://example.invalid/share '* ]] || exit 95
    fi ;;
  download)
    echo download >> calls
    [[ $4 == content/ragvi-results.tar.gz ]] || exit 96
    mkdir -p fake-artifact
    if [[ $SCENARIO == eda ]]; then artifact=eda.ipynb; else artifact=answers.jsonl; fi
    echo ok > "fake-artifact/$artifact"
    if [[ $SCENARIO == job_error ]]; then echo 7; else echo 0; fi > fake-artifact/exit_code.txt
    tar -czf "$5" -C fake-artifact . ;;
  stop)
    echo stop >> calls
    if [[ $SCENARIO == stop_error ]]; then exit 1; fi ;;
  *) exit 97 ;;
esac
'''.replace('__SCENARIO__', scenario), encoding='ascii', newline='\n')
    cli.chmod(0o755)
    env = {**os.environ, 'PATH': str(tmp_path) + os.pathsep + os.environ['PATH'],
           'RAGVI_DRIVE_URL': 'https://example.invalid/share'}
    mode = scenario if scenario in ('eda', 'benchmark') else 'rag'
    proc = subprocess.run([BASH, script.name, mode], cwd=tmp_path, env=env, capture_output=True, encoding='utf-8')
    assert (proc.returncode == 0) == success, proc.stdout + proc.stderr
    assert (tmp_path / 'calls').read_text().splitlines() == expected
    if success:
        artifact = 'eda.ipynb' if mode == 'eda' else 'answers.jsonl'
        [result] = (tmp_path / 'results' / 'colab').glob(f'{mode}-*/{artifact}')
        assert result.read_text() == 'ok\n'
    if mode == 'benchmark':
        members = (tmp_path / 'bundle').read_text().splitlines()
        assert 'data/processed/viquad/train/data.arrow' in members
        assert 'data/processed/zalo_legal/queries/data.arrow' in members
        assert 'data/eval/zalo/removed_doc_ids.json' in members
        assert 'data/eval/zalo/reserve.jsonl' not in members
