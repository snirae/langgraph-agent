from pydantic import BaseModel


class Query(BaseModel):
    content: str

class Plan(BaseModel):
    steps: list[str]

class ToolOutput(BaseModel):
    result: str
