from models.data_models import Plan
from typing import List


class ToolSelector:
    def select_tools(self, plan: Plan) -> List[str]:
        # Placeholder logic for demo purposes
        return ["some_tool"] * len(plan.steps)
