# behavior_pipeline.py

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN

def build_behavior_segments(df: pd.DataFrame) -> pd.DataFrame:
    """
    Builds behavior-based segments: Regular / Bulk / Anomaly
    using DBSCAN.
    """
    print("Building behavior segment...")
    # invoice-level aggregation
    invoice_level = df.groupby(
        ['CustomerID', 'InvoiceNo', 'InvoiceDate']
    ).agg(
        invoice_quantity=('Quantity', 'sum')
    ).reset_index()

    behavior = invoice_level.groupby('CustomerID').agg(
        avg_qty=('invoice_quantity', 'mean'),
        std_qty=('invoice_quantity', 'std'),
        max_qty=('invoice_quantity', 'max'),
        avg_gap_days=('InvoiceDate', lambda x: x.sort_values().diff().dt.days.mean())
    )

    # handle NaNs
    behavior['std_qty'] = behavior['std_qty'].fillna(0)
    behavior['avg_gap_days'] = behavior['avg_gap_days'].fillna(
        behavior['avg_gap_days'].max()
    )

    # scale
    scaler = StandardScaler()
    behavior_scaled = scaler.fit_transform(behavior)

    # DBSCAN
    dbscan = DBSCAN(
        eps=0.5,
        min_samples=5
    )

    behavior['Behavior_Cluster'] = dbscan.fit_predict(behavior_scaled)

    # map clusters to business labels
    def map_behavior(c):
        if c == 0:
            return 'Regular'
        elif c == -1:
            return 'Anomaly'
        else:
            return 'Bulk'

    behavior['Behavior_Segment'] = behavior['Behavior_Cluster'].apply(map_behavior)

    return behavior[['Behavior_Segment']]
