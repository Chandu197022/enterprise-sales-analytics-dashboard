import pandas as pd

def transform_data(df):

    # Remove duplicates
    df.drop_duplicates(inplace=True)

    # Convert date columns
    df['Order Date'] = pd.to_datetime(df['Order Date'])
    df['Ship Date'] = pd.to_datetime(df['Ship Date'])

    # Shipping Days
    df['Shipping Days'] = (
        df['Ship Date']
        -
        df['Order Date']
    ).dt.days

    # Profit Margin
    df['Profit Margin %'] = (
        df['Profit']
        /
        df['Sales']
    ) * 100

    # Discount Amount
    df['Discount Amount'] = (
        df['Sales']
        *
        df['Discount']
    )

    # Year
    df['Sales Year'] = (
        df['Order Date']
        .dt.year
    )

    # Month
    df['Sales Month'] = (
        df['Order Date']
        .dt.month_name()
    )

    return df