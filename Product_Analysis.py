import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🛍️ Product Analysis")

products = pd.read_csv("data/products.csv")
order_items = pd.read_csv("data/order_items.csv")

order_items["revenue"] = order_items["quantity"] * order_items["unit_price"]

product_performance = order_items.groupby("product_id")["revenue"].sum().reset_index()
product_performance = product_performance.merge(products, on="product_id")

fig = px.bar(product_performance, x="product_name", y="revenue", title="Revenue by Product")
st.plotly_chart(fig, use_container_width=True)

fig2 = px.pie(product_performance, names="category", values="revenue", title="Category Wise Sales Share")
st.plotly_chart(fig2, use_container_width=True)
