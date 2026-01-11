# rfm_pipeline.py

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

def build_rfm_segments(df: pd.DataFrame, k: int = 3) -> pd.DataFrame:
    """
    Builds RFM features and assigns Low / Mid / High segments.
    """
    print("Building RFm segments...")
    reference_date = df['InvoiceDate'].max()

    rfm = df.groupby('CustomerID').agg(
        Recency=('InvoiceDate', lambda x: (reference_date - x.max()).days),
        Frequency=('InvoiceNo', 'nunique'),
        Monetary=('TotalPrice', 'sum')
    )

    scaler = StandardScaler()
    rfm_scaled = scaler.fit_transform(rfm)

    kmeans = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=10
    )

    rfm['RFM_Cluster'] = kmeans.fit_predict(rfm_scaled)

    label_map = {
        0: 'Low',
        1: 'Mid',
        2: 'High'
    }

    rfm['RFM_Segment'] = rfm['RFM_Cluster'].map(label_map)

    return rfm[['RFM_Segment']]
