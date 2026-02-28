![tests](https://github.com/jigark712/golden-regression-harness/actions/workflows/tests.yml/badge.svg)

# Golden Regression Harness


## Links
- Live HTML Test Report: https://jigark712.github.io/golden-regression-harness/report.html
A Python test harness for integration regression testing using versioned golden baselines. It generates deterministic telemetry, compares outputs against an expected baseline, and includes fault injection cases to validate robustness.

## What it does
- Compares current output against `goldens/baseline.json` to detect regressions
- Exercises negative paths with fault injection (timeout, noise, malformed payload)
- Runs automatically in GitHub Actions

## Project structure
- `src/harness/` — telemetry generator and golden comparison utilities
- `tests/` — regression and fault-injection tests
- `goldens/` — baseline output used for regression checks
- `.github/workflows/` — CI configuration

## Run and test locally
Prereqs: Python 3.10+.

1) Create and activate a virtual environment
   python3 -m venv .venv
   source .venv/bin/activate

2) Install dependencies and the package
   python -m pip install -U pip setuptools wheel pytest
   python -m pip install -e .

3) Run tests
   pytest -q
