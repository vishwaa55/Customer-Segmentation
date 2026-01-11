# preprocessing.py

import pandas as pd

def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans raw Online Retail data and returns
    purchase-only customer-level transactional data.
    """
    print("Preprocessing...")
    # keep only known customers
    df = df[df['CustomerID'].notna()].copy()

    # remove cancellations
    df = df[~df['InvoiceNo'].astype(str).str.startswith('C')]

    # remove returns and invalid prices
    df = df[(df['Quantity'] > 0) & (df['UnitPrice'] > 0)]

    # create monetary feature
    df['TotalPrice'] = df['Quantity'] * df['UnitPrice']

    return df
