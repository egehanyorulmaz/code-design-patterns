from enum import Enum
from typing import Dict, Optional

from pydantic import BaseModel

class OnboardItem(BaseModel):
    necessery_common_item: str
    id_common: int
    op_kwargs: Optional[Dict] = {}

class Example_1_OnboardItem(OnboardItem):
    user_id: str
    name: str

class Example_2_OnboardItem(OnboardItem):
    ip_v: str
    api_version: str

class Example_3_OnboardItem(OnboardItem):
    customer_ids: int
    yaml_path_groom: str
    yaml_path_map: str
    base_url: str


class ExampleTPA(Enum):
    EXAMPLE_1 = ("Example1", Example_1_OnboardItem)
    EXAMPLE_2 = ("Example2", Example_2_OnboardItem)
    EXAMPLE_3 = ("Example3", Example_3_OnboardItem)
    # EXAMPLE_4 = ("Example4", Example_4_OnboardItem)
    # EXAMPLE_5 = ("Example5", Example_5_OnboardItem)
    # EXAMPLE_6 = ("Example6", Example_6_OnboardItem)
    # EXAMPLE_7 = ("Example7", Example_7_OnboardItem)
    # EXAMPLE_8 = ("Example8", Example_8_OnboardItem)
    # ...

    def __init__(self, name, item):
        self._name = name
        self._item = item

    @property
    def name(self):
        return self._name

    @property
    def item_name(self):
        return self._item
