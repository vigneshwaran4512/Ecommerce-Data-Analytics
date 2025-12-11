import streamlit as st
import pandas as pd
import plotly.express as px

st.title("💰 Profit Analysis")

products = pd.read_csv("data/products.csv")
order_items = pd.read_csv("data/order_items.csv")

order_items["revenue"] = order_items["quantity"] * order_items["unit_price"]

merged = order_items.merge(products, on="product_id")
merged["cost_total"] = merged["quantity"] * merged["cost"]
merged["profit"] = merged["revenue"] - merged["cost_total"]

category_profit = merged.groupby("category")[["revenue","cost_total","profit"]].sum().reset_index()

fig = px.bar(category_profit, x="category", y="profit", title="Profit by Category")
st.plotly_chart(fig, use_container_width=True)

top_profit = merged.groupby("product_name")["profit"].sum().reset_index().sort_values("profit", ascending=False).head(10)
fig2 = px.bar(top_profit, x="product_name", y="profit", title="Top 10 Most Profitable Products")
st.plotly_chart(fig2, use_container_width=True)
