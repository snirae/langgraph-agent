from typing import Generator

from langchain_core.documents import Document

from components.llm_components.base_llm_component import BaseLLMComponent
from llm.build_prompt import build_prompt
from llm.format_tool_outputs import format_tool_outputs
from models.data_models import AgentState
from llm.ollama_llm import Model


class ResponseGenerator(BaseLLMComponent):
    def __init__(self, model: Model = Model.GEMMA3_1B, stream_response: bool = False):
        super().__init__(model, stage="generation", stream_response=stream_response)

    def __call__(self, state: AgentState) -> dict[str, str | Generator]:
        query = state["query"]
        context = state["context"]
        response = self.generate_response(query, context)
        return {"answer": response}

    def generate_response(
        self,
        query: str,
        context: list[Document],
    ) -> str | Generator:
        messages = build_prompt(self.settings_prompts, query)
        formatted_tool_outputs = format_tool_outputs(context)
        messages[-1]["content"] = (
            formatted_tool_outputs + "\n" + messages[-1]["content"]
        )

        if self.stream_response:
            response = self.llm.generate_stream(messages)
        else:
            response = self.llm.generate(messages)
        return response
