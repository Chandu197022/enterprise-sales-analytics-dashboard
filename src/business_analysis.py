import pandas as pd

df = pd.read_csv(
    "../data/processed/superstore_cleaned.csv"
)

# Monthly Sales
monthly_sales = (
    df.groupby(['Sales Year', 'Sales Month'])['Sales']
      .sum()
      .reset_index()
)

monthly_sales.to_csv(
    "../data/exports/monthly_sales.csv",
    index=False
)

# Regional Sales
regional_sales = (
    df.groupby('Region')['Sales']
      .sum()
      .reset_index()
)

regional_sales.to_csv(
    "../data/exports/regional_sales.csv",
    index=False
)

# Category Sales
category_sales = (
    df.groupby('Category')['Sales']
      .sum()
      .reset_index()
)

category_sales.to_csv(
    "../data/exports/category_sales.csv",
    index=False
)

print("Business exports created successfully")