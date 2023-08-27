from fastapi import HTTPException
from pydantic.error_wrappers import ValidationError

from data_models import ExampleTPA

class OnboardItemValidator:
    def __init__(self, tpa_str: str):
        tpa = [t for t in ExampleTPA if t.shorthand == tpa_str]
        if not tpa:
            raise HTTPException(400, f'{tpa_str} does not exist')

        self.tpa = tpa.pop()

    def validate_and_get_item(self, item):
        try:
            onboard_item = self.tpa.item_name(**item)
            return onboard_item, self.tpa.handler
        except ValidationError as e:
            raise HTTPException(status_code=400, detail=e.errors())
