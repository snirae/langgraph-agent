import textwrap

from components.llm_components.base_llm_component import BaseLLMComponent
from llm.build_prompt import build_prompt
from llm.ollama_llm import Model
from models.data_models import ToolOutput, AgentState


class SufficiencyFilter(BaseLLMComponent):
    def __init__(self, model: Model = Model.GEMMA3_1B):
        super().__init__(model, stage="sufficiency")

    def __call__(self, state: AgentState) -> dict[str, list[ToolOutput]]:
        filtered_outputs = self.filter_outputs(state["query"], state["tool_outputs"])
        return {"tool_outputs": filtered_outputs}

    def filter_outputs(
        self, query: str, tool_outputs: list[ToolOutput]
    ) -> list[ToolOutput]:
        sufficiency_classifications = []
        for output in tool_outputs:
            current_classifications = []
            for result in output.results:
                user_message = textwrap.dedent(
                    f"""
                        ### QUESTION
                        {query}
                        ### REFERENCES
                        {result}
                    """
                )
                messages = build_prompt(self.settings_prompts, user_message)
                llm_response = self.llm.generate(messages).strip()

                is_sufficient = True if "1" in llm_response else False
                current_classifications.append(is_sufficient)

            sufficiency_classifications.append(current_classifications)

        filtered_outputs = []
        for tool_output, classifications in zip(
            tool_outputs, sufficiency_classifications
        ):
            filtered_from_tool = [
                result
                for result, is_sufficient in zip(tool_output.results, classifications)
                if is_sufficient
            ]
            filtered_outputs.append(
                ToolOutput(
                    tool_name=tool_output.tool_name,
                    results=filtered_from_tool,
                )
            )

        return filtered_outputs
