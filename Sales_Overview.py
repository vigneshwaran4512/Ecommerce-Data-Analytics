import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Sales Overview")

orders = pd.read_csv("data/orders.csv")
order_items = pd.read_csv("data/order_items.csv")
products = pd.read_csv("data/products.csv")

merged = order_items.merge(products, on="product_id").merge(orders, on="order_id")

merged["total"] = merged["quantity"] * merged["unit_price"]

sales_by_month = merged.groupby(merged["order_date"].str[:7])["total"].sum().reset_index()

fig = px.line(sales_by_month, x="order_date", y="total", title="Monthly Sales Trend")
st.plotly_chart(fig, use_container_width=True)

top_products = merged.groupby("product_name")["total"].sum().reset_index().sort_values("total", ascending=False).head(10)

fig = px.bar(top_products, x="product_name", y="total", title="Top 10 Best Selling Products")
st.plotly_chart(fig, use_container_width=True)

