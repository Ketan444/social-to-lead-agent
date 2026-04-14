from pathlib import Path


class ActionHandler:
    def handle(self, validation_result):
        output_dir = Path("outputs")
        output_dir.mkdir(exist_ok=True)

        if validation_result["status"] == "PASS":
            return {
                "action": "save_clean_output",
                "message": "Validation successful"
            }

        error_log = output_dir / "error.log"

        with open(error_log, "w", encoding="utf-8") as f:
            for err in validation_result["errors"]:
                f.write(err + "\n")

        return {
            "action": "log_errors",
            "message": "Validation failed"
        }