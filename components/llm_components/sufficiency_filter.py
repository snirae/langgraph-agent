import textwrap

from langchain_core.documents import Document

from components.llm_components.base_llm_component import BaseLLMComponent
from llm.build_prompt import build_prompt
from llm.ollama_llm import Model
from models.data_models import AgentState


class SufficiencyFilter(BaseLLMComponent):
    def __init__(self, model: Model = Model.GEMMA3_1B):
        super().__init__(model, stage="sufficiency")

    def __call__(self, state: AgentState) -> dict[str, list[Document]]:
        filtered_context = self.filter_context(state["query"], state["context"])
        return {"context": filtered_context}

    def filter_context(self, query: str, context: list[Document]) -> list[Document]:
        sufficiency_classifications = []
        for doc in context:
            user_message = textwrap.dedent(
                f"""
                    ### QUESTION
                    {query}
                    ### REFERENCES
                    {doc.page_content}
                """
            )
            messages = build_prompt(self.settings_prompts, user_message)
            llm_response = self.llm.generate(messages).strip()

            is_sufficient = True if "1" in llm_response else False
            sufficiency_classifications.append(is_sufficient)

        filtered_context = [
            doc
            for doc, is_sufficient in zip(context, sufficiency_classifications)
            if is_sufficient
        ]
        return filtered_context
