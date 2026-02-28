import os
from harness.compare import deep_equal, load_json, write_json
from harness.simulator import SimConfig, simulate_telemetry

GOLDEN_PATH = "goldens/baseline.json"


def test_golden_regression():
    out = simulate_telemetry(SimConfig(seed=42, n=40))

    if os.getenv("UPDATE_GOLDENS") == "1":
        write_json(GOLDEN_PATH, out)
        assert True
        return

    expected = load_json(GOLDEN_PATH)
    ok, msg = deep_equal(out, expected)
    assert ok, msg
