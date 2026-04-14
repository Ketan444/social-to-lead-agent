from agent.parser import FileParser
from agent.validator import Validator
from agent.action_handler import ActionHandler
from agent.result_generator import ResultGenerator


class AutomatedTestingWorkflow:
    def __init__(self):
        self.parser = FileParser()
        self.validator = Validator()
        self.handler = ActionHandler()
        self.generator = ResultGenerator()

    def run(self, file_path):
        data = self.parser.parse(file_path)
        validation = self.validator.validate(data)
        action = self.handler.handle(validation)

        # ✅ optimized preview (only 3 rows instead of 5)
        dataset_preview = (
            data.iloc[:3].to_dict("records")
            if hasattr(data, "iloc")
            else str(data)[:200]
        )

        result = {
            "file": file_path,
            "total_rows": data.shape[0] if hasattr(data, "shape") else "unknown",
            "total_columns": data.shape[1] if hasattr(data, "shape") else "unknown",
            "dataset_preview": dataset_preview,
            "validation": validation,
            "action": action
        }

        self.generator.generate(result)
        return result