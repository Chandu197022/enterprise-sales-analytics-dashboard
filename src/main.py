from extract import extract_data
from transform import transform_data
from load import load_data

RAW_FILE = (
    "../data/raw/"
    "Sample - Superstore.csv"
)

PROCESSED_FILE = (
    "../data/processed/"
    "superstore_cleaned.csv"
)

df = extract_data(RAW_FILE)

df = transform_data(df)

load_data(
    df,
    PROCESSED_FILE
)

print(
    "ETL Pipeline Completed Successfully"
)