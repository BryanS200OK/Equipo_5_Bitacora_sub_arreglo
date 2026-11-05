"""Suite fija; no se aceptan comandos ni rutas provenientes de la interfaz."""
import json
import os
import subprocess
import sys
import tempfile
import time
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path
from .experiment import ROOT, commit_id, source_hash


def run_qa():
    started = time.perf_counter()
    with tempfile.TemporaryDirectory() as temp:
        xml = Path(temp) / "qa.xml"
        env = os.environ.copy()
        env["PYTHONPATH"] = os.pathsep.join([str(ROOT / "src"), *[p for p in sys.path if p]])
        env["PYTEST_DISABLE_PLUGIN_AUTOLOAD"] = "1"
        try:
            proc = subprocess.run([sys.executable, "-m", "pytest", "tests", "-q", f"--junitxml={xml}"], cwd=ROOT,
                                  env=env, capture_output=True, text=True, timeout=45)
            suites = list(ET.parse(xml).getroot().iter("testsuite")) if xml.exists() else []
            counts = {key: sum(int(s.attrib.get(key, 0)) for s in suites) for key in ("tests", "failures", "errors", "skipped")}
            return dict(**counts, passed=counts["tests"]-counts["failures"]-counts["errors"]-counts["skipped"],
                        exit_code=proc.returncode, output=(proc.stdout + proc.stderr)[-24000:],
                        duration_s=time.perf_counter()-started, date=datetime.now(timezone.utc).isoformat(),
                        commit=commit_id(), source_sha256=source_hash())
        except subprocess.TimeoutExpired:
            return dict(tests=0, passed=0, failures=0, errors=1, skipped=0, exit_code=124,
                        output="Timeout de la suite fija (45 s).", duration_s=time.perf_counter()-started,
                        date=datetime.now(timezone.utc).isoformat(), commit=commit_id(), source_sha256=source_hash())
