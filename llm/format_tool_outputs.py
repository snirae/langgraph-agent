from langchain_core.documents import Document


def format_tool_outputs(
    context: list[Document],
) -> str:
    result = "Context retrieved using tools:\n<results>"
    for idx, doc in enumerate(context):
        result += f"\nDocument #{idx}:\n"
        result += doc.page_content
        result += "\n"
    result += "</results>"

    return result
