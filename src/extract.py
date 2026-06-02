import pandas as pd

def extract_data(filepath):
    """
    Read raw CSV data
    """
    df = pd.read_csv(filepath, encoding="latin1")

    print(f"Rows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")

    return df