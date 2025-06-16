from models.data_models import ToolOutput


class OutputFilter:
    def filter_outputs(self, outputs: list[ToolOutput]) -> list[ToolOutput]:
        return [output for output in outputs if "error" not in output.result.lower()]
