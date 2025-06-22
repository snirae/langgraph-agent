from langchain_core.documents import Document


def format_tool_outputs(
    context: list[Document],
) -> str:
    result = "Context retrieved using tools:\n<results>"
    for doc in context:
        result += "\n".join(doc.page_content)
    result += "</results>"

    return result
