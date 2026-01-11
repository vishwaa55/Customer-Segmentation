import pandas as pd
from pathlib import Path

from preprocessing import preprocess_data
from rfm_pipeline import build_rfm_segments
from behavior_pipeline import build_behavior_segments


def main():
    BASE_DIR = Path(__file__).resolve().parent.parent
    DATA_PATH = BASE_DIR / 'data' / 'OnlineRetail.xlsx'

    df = pd.read_excel(DATA_PATH)
    print("Data uploaded")
    df_purchases = preprocess_data(df)
    print("Data preprocessed")
    rfm_segments = build_rfm_segments(df_purchases, k=3)
    print("RFM pipeline built")
    behavior_segments = build_behavior_segments(df_purchases)
    print("Behavior pipeline built")

    customer_segments = (
        rfm_segments
        .join(behavior_segments, how='left')
        .reset_index()
    )
    print("Merged two pipelines.\n")

    # save output for frontend / reference
    OUTPUT_PATH = BASE_DIR / 'data' / 'output.csv'
    customer_segments.to_csv(OUTPUT_PATH, index=False)

    print(f"Saved output to {OUTPUT_PATH}")

    print(customer_segments.head())


if __name__ == "__main__":
    main()
