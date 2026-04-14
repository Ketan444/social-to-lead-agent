import json
from pathlib import Path


class Validator:
    def __init__(self, rule_path="rules/validation_rules.json"):
        self.rule_path = Path(rule_path)
        self.rules = self.load_rules()   # load once

    def load_rules(self):
        with open(self.rule_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def validate(self, data):
        errors = []

        if hasattr(data, "columns"):
            cols = set(data.columns)   # O(1) lookup

            missing = [
                col for col in self.rules["required_columns"]
                if col not in cols
            ]

            if missing:
                errors.append(f"Missing columns: {', '.join(missing)}")

            # single dataframe scan
            null_count = int(data.isnull().values.sum())

            if self.rules["check_nulls"] and null_count > 0:
                errors.append(f"Null values found: {null_count}")

        return {
            "status": "PASS" if not errors else "FAIL",
            "errors": errors
        }