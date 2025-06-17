from components.llm_components.base_llm_component import BaseLLMComponent
from llm.build_prompt import build_prompt
from llm.format_tool_outputs import format_tool_outputs
from models.data_models import ToolOutput, AgentState
from llm.ollama_llm import Model


class ResponseGenerator(BaseLLMComponent):
    def __init__(self, model: Model = Model.GEMMA3_1B):
        super().__init__(model, stage="generation")

    def __call__(self, state: AgentState) -> dict[str, str]:
        query = state["query"]
        tool_outputs = state["tool_outputs"]
        response = self.generate_response(query, tool_outputs)
        return {"answer": response}

    def generate_response(
        self,
        query: str,
        tool_outputs: list[ToolOutput],
    ) -> str:
        messages = build_prompt(self.settings_prompts, query)
        formatted_tool_outputs = format_tool_outputs(tool_outputs)
        messages[-1]["content"] = (
            formatted_tool_outputs + "\n" + messages[-1]["content"]
        )

        response = self.llm.generate(messages)
        return response
