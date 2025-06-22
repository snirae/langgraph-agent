from typing import TypedDict

from langchain_core.documents import Document
from pydantic import BaseModel


class SettingsPrompts(BaseModel):
    system: str = ""
    task: str = ""
    style: str = ""


class AgentState(TypedDict):
    query: str
    context: list[Document]
    answer: str
