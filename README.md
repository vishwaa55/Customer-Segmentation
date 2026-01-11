# Customer Segmentation Dashboard

An end-to-end customer segmentation system built using transactional retail data to group customers by **business value** and **purchase behavior**, presented through an interactive Streamlit dashboard.

Streamlit link: https://customer-segmentation-4g69enfgjysvvhstmiy9iu.streamlit.app/

The project focuses on **interpretability**, **practical insights**, and **real-world usability**, rather than just model building.

---

## 📌 Project Overview

This project analyzes historical transaction data and classifies customers along two independent dimensions:

1. **Customer Value**  
   How important a customer is based on their purchasing history.

2. **Purchase Style**  
   How a customer typically buys (regular quantities, bulk orders, or irregular patterns).

The final output is a clean, user-friendly dashboard that allows filtering, exploration, and insight generation without requiring any data science background.

---

## 🧠 Segmentation Logic

### 1️⃣ Customer Value Segmentation
Customers are grouped into:
- **Low** – Rare buyers or very low spenders  
- **Mid** – Average customers with moderate activity  
- **High** – Frequent or high-spending customers  

This captures *how valuable* a customer is to the business.

---

### 2️⃣ Purchase Style Segmentation
Customers are grouped into:
- **Regular** – Consistent, normal-sized purchases  
- **Bulk** – Large-quantity or wholesale-style buyers  
- **Anomaly** – Unusual or irregular buying behavior  

This captures *how customers behave* when they purchase.

---

## 🔍 Why Two Pipelines?

Customer **value** and **behavior** answer different business questions.

Separating them allows:
- Better interpretability
- Cleaner analysis
- More flexible filtering
- Real-world decision support

For example:
- **High + Bulk** → Key accounts  
- **Mid + Regular** → Growth opportunities  
- **Low + Anomaly** → Low priority or investigation cases  

---

## ⚙️ Technologies Used

- **Python**
- **Pandas / NumPy** – Data processing
- **Scikit-learn** – Clustering algorithms
- **Streamlit** – Interactive dashboard
- **Excel (.xlsx)** – Input data format

---


### Install Dependencies
```bash
pip install -r requirements.txt
```
## 📂 Dataset Source

The project uses the **Online Retail Dataset**, which contains historical transactional data from a UK-based online retail company.

Link: https://www.kaggle.com/code/yasserh/online-customer-segmentation-clustering-approach/input
