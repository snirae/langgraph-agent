from models.data_models import ToolOutput


def format_tool_outputs(
    tool_outputs: list[ToolOutput],
) -> str:
    result = "Context retrieved using tools:\n<results>"
    for tool_output in tool_outputs:
        result += "\n".join(tool_output.results)
    result += "</results>"

    return result
