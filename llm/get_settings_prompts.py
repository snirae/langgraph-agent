import yaml
from pathlib import Path

from models.data_models import SettingsPrompts


def get_settings_prompts(stage: str) -> SettingsPrompts:
    prompts_path = Path(__file__).parent.parent / "prompts"
    common_prompts_path = prompts_path / "common.yaml"
    stage_prompts_path = prompts_path / f"{stage}.yaml"

    with open(common_prompts_path, "r") as f:
        common_prompts = yaml.safe_load(f)

    with open(stage_prompts_path, "r") as f:
        stage_prompts = yaml.safe_load(f)

    unified_prompts = common_prompts | stage_prompts
    return SettingsPrompts(**unified_prompts)
