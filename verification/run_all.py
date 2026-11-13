#!/usr/bin/env python3
"""Run the finite scientific diagnostics from the repository root."""

import json
import os
from pathlib import Path
import platform
import subprocess
import sys

import numpy
import scipy


def main():
    root = Path(__file__).resolve().parents[1]
    environment = dict(os.environ)
    environment.setdefault("OPENBLAS_NUM_THREADS", "1")
    reports = {}
    for name in ("check_spectrum.py", "check_decoder.py", "check_cooling.py"):
        result = subprocess.run(
            [sys.executable, str(root / "verification" / name)],
            cwd=root, env=environment, text=True, capture_output=True, check=True,
        )
        report = json.loads(result.stdout)
        if not report.get("passed"):
            raise RuntimeError(f"{name} did not report a pass")
        reports[name] = report
    print(json.dumps({
        "passed": True,
        "environment": {"python": platform.python_version(),
                        "numpy": numpy.__version__, "scipy": scipy.__version__},
        "checks": reports,
    }, indent=2))


if __name__ == "__main__":
    main()
