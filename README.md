![tests](https://github.com/jigark712/golden-regression-harness/actions/workflows/tests.yml/badge.svg)

# Golden Regression Harness (Golden Files + Fault Injection)

A production-style testing harness that:
- generates deterministic "device-like" telemetry
- validates outputs with golden baselines (regression testing)
- supports fault injection (timeout/noise/malformed)
- runs in GitHub Actions and uploads an HTML test report + artifacts

## Run locally
python3 -m venv .venv
source .venv/bin/activate
pip install -U pip setuptools wheel pytest
pip install -e .
pytest -q

## Update goldens
UPDATE_GOLDENS=1 pytest -q
