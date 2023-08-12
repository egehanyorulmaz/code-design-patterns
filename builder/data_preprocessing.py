from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import pandas as pd


class Dataset:
    def __init__(self, data):
        self.data = data
        self.is_normalized = False
        self.is_encoded = False
        self.is_split = False

    def apply(self, processor):
        self.data = processor(self.data)
        return self

    def get_data(self):
        return self.data


class DatasetBuilder:
    def __init__(self, data):
        self.dataset = Dataset(data)

    def one_hot_encode(self, columns):
        if not self.dataset.is_encoded:
            self.dataset.data = pd.get_dummies(self.dataset.data, columns=columns)
            self.dataset.is_encoded = True
        return self

    def normalize(self):
        if self.dataset.is_encoded and not self.dataset.is_normalized:
            scaler = StandardScaler()
            data_scaled = scaler.fit_transform(self.dataset.data.iloc[:, :-1])
            scaled_df = pd.DataFrame(data_scaled, columns=self.dataset.data.columns[:-1])
            scaled_df['label'] = self.dataset.data['label']
            self.dataset.data = scaled_df
            self.dataset.is_normalized = True
        return self

    def split_data(self, test_size):
        if not self.dataset.is_split:
            X_train, X_test, y_train, y_test = train_test_split(self.dataset.data.iloc[:, :-1],
                                                                self.dataset.data.iloc[:, -1],
                                                                test_size=test_size)
            self.dataset.data = (X_train, X_test, y_train, y_test)
            self.dataset.is_split = True
        return self

    def build(self):
        if self.dataset.is_encoded and self.dataset.is_normalized and self.dataset.is_split:
            return self.dataset.get_data()
        else:
            raise Exception("Data must be one-hot encoded, normalized, and split before building")


# Assuming 'data' is your pandas DataFrame
data = pd.DataFrame({
    'feature1': [1, 2, 3, 4],
    'feature2': [5, 6, 7, 8],
    'label': [0, 1, 0, 1]
})

builder = DatasetBuilder(data)
prepared_data = (builder
                 .one_hot_encode(columns=['feature1'])
                 .normalize()
                 .split_data(test_size=0.2)
                 .build())

print(prepared_data)  # Output will be the preprocessed and split dataset
