import pandas as pd

df = pd.read_csv(
    "../data/processed/superstore_cleaned.csv"
)

print(df.head())

print(df.info())

print(df.describe())