from abc import ABC, abstractmethod
import os

from validation.data_models import *

class TriggerHandler(ABC):
    """ Method to handle triggers.
    It explains developer to override construct_payload method for each new example.
    Each Incoming sends a hit to the airflow-api to trigger its corresponding Airflow DAG."

    :param _type_ ABC: _description_
    """
    def __init__(self, onboard_item, dag_name):
        self.onboard_item = onboard_item
        self.dag_name = dag_name
        common_3 = "hardcoded_value"

        self.default_parameters = {
            # Internal common conf
            "common_1_key": self.onboard_item.common1,
            "common_2_key": self.onboard_item.common2,
            "common_3_key": common_3,
            "common_4_key": self.onboard_item.common4,
            "common_5_key": self.onboard_item.common5,

            # AWS related configs
            "aws_common_value_example_1": os.environ["example1"],
            "aws_common_value_example_2": os.environ["example2"],
            "aws_common_value_example_3": os.environ["example3"],
            "aws_common_value_example_4": os.environ["example4"],
            "aws_common_value_example_5": os.environ["example5"],
            "aws_common_value_example_6": os.environ["example6"],
        }

    @abstractmethod
    def construct_payload(self):
        pass

    def handle_trigger(self):
        # Each class will trigger the "self.dag_name" DAG
        payload = self.construct_payload()

        # Triggers Airflow, No need to implement this logic
        response = AirflowClient().trigger_dag(payload=payload, dag_name=self.dag_name)
        return response


class Example1TriggerHandler(TriggerHandler):
    def construct_payload(self):
        tpa_payload = {
            "specific_key_1": "specific_value_1",
            "specific_key_2": "specific_value_2",
            "specific_key_3": "specific_value_3",
            "specific_key_4": "specific_value_4",
            "specific_key_5": "specific_value_5",
            "specific_key_6": "specific_value_6",
            "specific_key_7": "specific_value_7",
            "specific_key_8": "specific_value_8",
            "specific_key_9": "specific_value_9",
            "specific_key_10": "specific_value_10",
        }

        return {"conf": {**self.default_parameters, **tpa_payload}}


class Example2TriggerHandler(TriggerHandler):
    def construct_payload(self):
        tpa_payload = {
            "specific_key_1": "specific_value_1",
            "specific_key_2": "specific_value_2",
            "specific_key_3": "specific_value_3",
            "specific_key_4": "specific_value_4",
            "specific_key_5": "specific_value_5",
            "specific_key_6": "specific_value_6",
            "specific_key_7": "specific_value_7",
            "specific_key_8": "specific_value_8",
        }

        return {"conf": {**self.default_parameters, **tpa_payload}}

class ExampleTriggerFactory:
    @staticmethod
    def get_handler(onboard_item):
        if isinstance(onboard_item, Example_1_OnboardItem):
            return Example1TriggerHandler(onboard_item, "Example1-dag-name")
        elif isinstance(onboard_item, Example_2_OnboardItem):
            return Example2TriggerHandler(onboard_item, "Example2-dag-name")
        # elif isinstance(onboard_item, Example_3_OnboardItem):
        #     return Example3TriggerHandler(onboard_item, "Example3-dag-name")
        # ... Add other onboard items