from components.base_component import BaseComponent
from models.data_models import ToolOutput, AgentState


class OutputFilter(BaseComponent):
    def __call__(self, state: AgentState) -> dict[str, list[ToolOutput]]:
        filtered_outputs = self.filter_outputs(state["tool_outputs"])
        return {"tool_outputs": filtered_outputs}

    def filter_outputs(self, outputs: list[ToolOutput]) -> list[ToolOutput]:
        return outputs
