from typing import TypedDict

from pydantic import BaseModel


class ToolOutput(BaseModel):
    tool_name: str
    result: list[str]


class SettingsPrompts(BaseModel):
    system: str = ""
    task: str = ""
    style: str = ""


class AgentState(TypedDict):
    query: str
    tool_outputs: list[ToolOutput]
    answer: str
