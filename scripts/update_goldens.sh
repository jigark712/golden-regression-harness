#!/usr/bin/env bash
set -euo pipefail
UPDATE_GOLDENS=1 python3 -m pytest
echo "✅ Updated golden files."
