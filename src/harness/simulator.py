import json
import random
import time
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass(frozen=True)
class SimConfig:
    seed: int = 42
    n: int = 40
    base: float = 25.0


def simulate_telemetry(config: SimConfig, fault: Optional[str] = None) -> Dict[str, Any]:
    """
    Deterministic telemetry generator to mimic a device/instrument stream.
    Fault modes simulate real-world failure cases for negative-path testing.
    """
    rnd = random.Random(config.seed)

    if fault == "timeout":
        time.sleep(0.05)
        return {"status": "timeout", "values": []}

    values: List[float] = []
    for i in range(config.n):
        jitter = rnd.uniform(-0.25, 0.25)
        drift = 0.02 * i
        values.append(round(config.base + drift + jitter, 3))

    if fault == "noise":
        values = [round(v + rnd.uniform(-1.5, 1.5), 3) for v in values]

    if fault == "malformed":
        # Simulate a corrupted payload
        return {"status": "ok", "values": "not-a-list"}

    return {"status": "ok", "values": values}


def to_pretty_json(obj: Dict[str, Any]) -> str:
    return json.dumps(obj, indent=2, sort_keys=True) + "\n"
