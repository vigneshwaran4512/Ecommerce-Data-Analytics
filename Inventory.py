import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📦 Inventory Dashboard")

products = pd.read_csv("data/products.csv")

low_stock = products[products["stock"] < 50]
fast_moving = products.sort_values("stock", ascending=True).head(10)

st.subheader("🔴 Low Stock Alert (< 50 units)")
st.dataframe(low_stock)

fig = px.bar(low_stock, x="product_name", y="stock", title="Low Stock Products")
st.plotly_chart(fig, use_container_width=True)

st.subheader("⚡ Fast Moving (Lowest Stock First)")
st.dataframe(fast_moving)
