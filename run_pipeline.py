"""python run_pipeline.py [--qa-only]: detenerse al primer error."""
import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "src"))
from audrithm.qa import run_qa
from audrithm.experiment import run_experiment, save_results
from audrithm.visualization import save_charts
import pandas as pd


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--qa-only", action="store_true")
    args = parser.parse_args()
    output = ROOT / "results"
    output.mkdir(exist_ok=True)
    qa = run_qa()
    (output / "qa_results.json").write_text(json.dumps(qa, ensure_ascii=False, indent=2), encoding="utf-8")
    print(qa["output"])
    if qa["exit_code"]:
        return qa["exit_code"]
    if not args.qa_only:
        rows, meta = run_experiment()
        save_results(rows, meta, output)
        save_charts(pd.read_csv(output / "experiment_results.csv"), output)
        print(f"{len(rows)} observaciones reales guardadas en {output}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
