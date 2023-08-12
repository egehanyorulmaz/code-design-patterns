class DataPipeline:
    def __init__(self):
        self.steps = []

    def add_step(self, step):
        self.steps.append(step)
        return self

    def execute(self):
        data = None
        for step in self.steps:
            data = step(data)
        return data


class DataPipelineBuilder:
    def __init__(self):
        self.pipeline = DataPipeline()

    def add_loading(self, load_function):
        self.pipeline.add_step(load_function)
        return self

    def add_transformation(self, transform_function):
        self.pipeline.add_step(transform_function)
        return self

    def add_filtering(self, filter_function):
        self.pipeline.add_step(filter_function)
        return self

    def add_aggregation(self, aggregate_function):
        self.pipeline.add_step(aggregate_function)
        return self

    def build(self):
        return self.pipeline


# Client code
def load_data(data):
    print("Loading data...")
    return [1, 2, 3, 4, 5]

def transform_data(data):
    print("Transforming data...")
    return [x * 2 for x in data]

def filter_data(data):
    print("Filtering data...")
    return [x for x in data if x > 5]

def aggregate_data(data):
    print("Aggregating data...")
    return sum(data)

builder = DataPipelineBuilder()
pipeline = (builder
            .add_loading(load_data)
            .add_transformation(transform_data)
            .add_filtering(filter_data)
            .add_aggregation(aggregate_data)
            .build())

result = pipeline.execute()
print("Result:", result)  # Output: "Result: 18"
