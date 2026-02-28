from src.harness.simulator import SimConfig, simulate_telemetry


def test_fault_timeout():
    out = simulate_telemetry(SimConfig(seed=1), fault="timeout")
    assert out["status"] == "timeout"


def test_fault_noise_still_list():
    out = simulate_telemetry(SimConfig(seed=1), fault="noise")
    assert out["status"] == "ok"
    assert isinstance(out["values"], list)
    assert len(out["values"]) > 0


def test_fault_malformed_detectable():
    out = simulate_telemetry(SimConfig(seed=1), fault="malformed")
    assert out["status"] == "ok"
    assert not isinstance(out["values"], list)
