import pandas as pd
from .config import DATASETS

def load_data():
    data = {}
    for name, path in DATASETS.items():
        data[name] = pd.read_csv(path)
    return data

def show_shapes(data):
    for name, df in data.items():
        print(f"{name:22} -> {df.shape[0]:5} rows x {df.shape[1]:2} columns")
