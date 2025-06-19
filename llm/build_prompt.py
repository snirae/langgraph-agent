from models.data_models import SettingsPrompts


def build_prompt(
    settings_prompts: SettingsPrompts,
    user_message: str,
) -> list[dict[str, str]]:
    system_prompt = (
        f"{settings_prompts.system}\n"
        f"Task Details:\n{settings_prompts.task}\n"
        f"Style Constraints:\n{settings_prompts.style if settings_prompts.style != '' else None}\n"
    )
    messages = [
        {
            "role": "system",
            "content": system_prompt,
        },
        {
            "role": "user",
            "content": user_message,
        },
    ]
    return messages
