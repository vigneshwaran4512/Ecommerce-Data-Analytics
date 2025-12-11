import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🧑‍🤝‍🧑 Customer Insights")

customers = pd.read_csv("data/customers.csv")
orders = pd.read_csv("data/orders.csv")

order_counts = orders.groupby("customer_id")["order_id"].count().reset_index()
order_counts.columns = ["customer_id", "orders_count"]

customer_data = customers.merge(order_counts, on="customer_id", how="left").fillna(0)

fig = px.histogram(customer_data, x="orders_count", title="Customer Order Frequency")
st.plotly_chart(fig, use_container_width=True)

fig2 = px.box(customer_data, x="gender", y="age", title="Age Distribution by Gender")
st.plotly_chart(fig2, use_container_width=True)
