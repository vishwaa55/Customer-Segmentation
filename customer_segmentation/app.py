import streamlit as st
import pandas as pd
from pathlib import Path

# app title
st.title("Customer Grouping Dashboard")

st.markdown(
    """
    This dashboard groups customers based on **how valuable they are**
    and **how they usually purchase products**.
    """
)

# load data
BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / 'data' / "output.csv"

@st.cache_data
def load_data(path):
    return pd.read_csv(path)

df = load_data(DATA_PATH)

df = pd.read_csv(DATA_PATH)

# explain columns in simple terms
st.subheader("What do these groups mean?")

st.markdown(
    """
    **Customer Value**
    - **Low** → Rare buyers or customers who spent very little  
    - **Mid** → Normal customers with moderate purchases  
    - **High** → Very important customers who buy often or spend a lot  

    **Purchase Style**
    - **Regular** → Buys normal quantities consistently  
    - **Bulk** → Buys very large quantities (wholesale / bulk orders)  
    - **Anomaly** → Unusual or irregular buying pattern  
    """
)

# # preview
# st.subheader("Sample Customer Records")
# st.write(df.head())

# sidebar filters
st.sidebar.header("Filter Customers")

rfm_filter = st.sidebar.multiselect(
    "Customer Value",
    options=df['RFM_Segment'].unique(),
    default=df['RFM_Segment'].unique()
)

behavior_filter = st.sidebar.multiselect(
    "Purchase Style",
    options=df['Behavior_Segment'].unique(),
    default=df['Behavior_Segment'].unique()
)

# apply filters
filtered_df = df[
    (df['RFM_Segment'].isin(rfm_filter)) &
    (df['Behavior_Segment'].isin(behavior_filter))
]

# results
st.subheader("Filtered Customer List")
st.markdown(
    "This table shows customers matching the selected value and purchase style."
)
st.write(filtered_df)

# counts
st.subheader("Customer Group Summary")
st.markdown(
    "This shows how many customers fall into each group."
)
st.write(filtered_df[['RFM_Segment', 'Behavior_Segment']].value_counts())

st.subheader("Customer Distribution (%)")
st.write(
    filtered_df[['RFM_Segment', 'Behavior_Segment']]
    .value_counts(normalize=True)
    .mul(100)
    .round(2)
)

col1, col2, col3 = st.columns(3)

col1.metric("Total Customers", len(df))
col2.metric("High Value Customers", (df['RFM_Segment']=='High').sum())
col3.metric("Bulk Buyers", (df['Behavior_Segment']=='Bulk').sum())

st.subheader("Customer Group Breakdown")

cross_table = pd.crosstab(
    df['RFM_Segment'],
    df['Behavior_Segment']
)

st.write(cross_table)
