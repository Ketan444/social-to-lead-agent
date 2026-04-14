import json
from pathlib import Path


class ResultGenerator:
    def generate(self, result):
        output_dir = Path("outputs")
        output_dir.mkdir(exist_ok=True)

        report_path = output_dir / "report.json"

        with open(report_path, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=4)

        return str(report_path)