import streamlit as st
import pandas as pd
import plotly.express as px
from model import train_model

# Load dataset
df = pd.read_csv("superstore.csv", encoding='latin1')

st.set_page_config(page_title="BizIntel Dashboard", layout="wide")

# Title
st.title("📊 BizIntel: Business Insights Dashboard")

# Raw data toggle
if st.checkbox("Show Raw Data"):
    st.subheader("Raw Data")
    st.write(df)

# Metrics
st.subheader("📈 Basic Business Metrics")
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
avg_discount = df["Discount"].mean()

col1, col2, col3 = st.columns(3)
col1.metric("Total Sales", f"${total_sales:,.2f}")
col2.metric("Total Profit", f"${total_profit:,.2f}")
col3.metric("Avg Discount", f"{avg_discount*100:.2f}%")


# 💡 FILTERS
st.sidebar.header("📂 Filters")
region = st.sidebar.selectbox("Select Region", df["Region"].unique())
filtered_df = df[df["Region"] == region]

st.subheader(f"📍 Region Selected: {region}")

# 📊 CHART 1: Sales by Category
sales_by_category = filtered_df.groupby("Category")["Sales"].sum().reset_index()
fig1 = px.bar(sales_by_category, x="Category", y="Sales", color="Category", title="Sales by Category")
st.plotly_chart(fig1, use_container_width=True)

# 📊 CHART 2: Profit by Sub-Category
profit_by_subcat = filtered_df.groupby("Sub-Category")["Profit"].sum().sort_values(ascending=False).reset_index()
fig2 = px.bar(profit_by_subcat, x="Sub-Category", y="Profit", color="Profit", title="Profit by Sub-Category")
st.plotly_chart(fig2, use_container_width=True)

# 📊 CHART 3: Top 10 Products by Sales
top_products = filtered_df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(10).reset_index()
fig3 = px.bar(top_products, x="Product Name", y="Sales", color="Sales", title="Top 10 Products")
st.plotly_chart(fig3, use_container_width=True)

# 🔮 Predict Future Sales
st.header("🔮 Predict Sales")

model = train_model()

st.subheader("Enter values to predict Sales:")
col1, col2, col3 = st.columns(3)

profit = col1.number_input("Profit (₹)", value=100.0)
discount = col2.number_input("Discount (0.0 to 1.0)", value=0.1, min_value=0.0, max_value=1.0, step=0.01)
quantity = col3.number_input("Quantity", value=1, step=1)

if st.button("Predict"):
    input_data = [[profit, discount, quantity]]
    prediction = model.predict(input_data)[0]
    st.success(f"📦 Predicted Sales: ₹{prediction:,.2f}")
