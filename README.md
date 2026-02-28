# Golden Regression Harness (Golden Files + Fault Injection)

This repo demonstrates:
- deterministic output generation
- golden-file regression tests
- fault injection (timeout/noise/malformed)
- GitHub Actions CI

## Local run
python3 -m venv .venv
source .venv/bin/activate
pip install pytest
pytest

## Update goldens
UPDATE_GOLDENS=1 pytest
