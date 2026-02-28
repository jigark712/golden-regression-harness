![tests](https://github.com/jigark712/golden-regression-harness/actions/workflows/tests.yml/badge.svg)

# Golden Regression Harness (Golden Files + Fault Injection)

A production-style Python testing harness that detects integration regressions by comparing outputs against versioned golden baselines. Includes fault injection scenarios to validate error handling, and runs in GitHub Actions with an uploaded HTML test report artifact.

## Overview
This project demonstrates:
- deterministic telemetry generation (seeded output)
- golden baseline regression testing (goldens/baseline.json)
- negative-path testing via fault injection (timeout/noise/malformed)
- CI automation in GitHub Actions (pytest + HTML report + artifacts)

## Repository structure
- src/harness/  telemetry generator and golden comparison utilities
- tests/        golden regression test and fault injection tests
- goldens/      versioned baseline outputs (baseline.json)
- .github/      CI workflow files
- docs/         optional published HTML report for GitHub Pages

## Run locally
python3 -m venv .venv
source .venv/bin/activate
pip install -U pip setuptools wheel pytest
pip install -e .
pytest -q

## Update golden baselines
UPDATE_GOLDENS=1 pytest -q

## Generate an HTML report locally
pip install pytest-html
pytest -q --html=report.html --self-contained-html
open report.html

## View the HTML report from CI
Actions -> latest run -> Artifacts -> download test-report-and-goldens -> open report.html

## Publish the HTML report via GitHub Pages (optional)
Generate docs/report.html and commit it, then enable Pages: Settings -> Pages -> main branch -> /docs

Live URL (after enabling Pages):
https://jigark712.github.io/golden-regression-harness/report.html
