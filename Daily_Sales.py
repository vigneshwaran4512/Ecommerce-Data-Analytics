import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📅 Daily Sales Dashboard")

orders = pd.read_csv("data/orders.csv")
order_items = pd.read_csv("data/order_items.csv")

order_items["total"] = order_items["quantity"] * order_items["unit_price"]

merged = order_items.merge(orders, on="order_id")
merged["order_date"] = pd.to_datetime(merged["order_date"])
merged["date"] = merged["order_date"].dt.date

daily = merged.groupby("date")["total"].sum().reset_index()

fig = px.line(daily, x="date", y="total", title="Daily Revenue Trend")
st.plotly_chart(fig, use_container_width=True)

st.dataframe(daily.tail(10))
