from models.data_models import ToolOutput


class ToolExecutor:
    def execute(self, tools: list[str], steps: list[str]) -> list[ToolOutput]:
        outputs = []
        for tool, step in zip(tools, steps):
            # Placeholder execution
            result = f"Executed '{tool}' for '{step}'"
            outputs.append(ToolOutput(result=result))
        return outputs
