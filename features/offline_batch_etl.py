
import pandas as pd

def load_data(filepath):
    df = pd.read_csv(filepath)
    df['hour_bin'] = pd.to_datetime('now').hour
    return df
