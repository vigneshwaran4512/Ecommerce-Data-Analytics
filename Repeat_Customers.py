import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🧑‍🤝‍🧑 Customer Repeat Purchase Analysis")

orders = pd.read_csv("data/orders.csv")

repeat = orders.groupby("customer_id")["order_id"].count().reset_index()
repeat.columns = ["customer_id", "order_count"]

repeat["type"] = repeat["order_count"].apply(lambda x: "Repeat Customer" if x > 1 else "New Customer")

count_summary = repeat["type"].value_counts().reset_index()
count_summary.columns = ["customer_type", "count"]

fig = px.pie(count_summary, names="customer_type", values="count", title="New vs Repeat Customers")
st.plotly_chart(fig, use_container_width=True)

st.subheader("Top Repeat Customers")
top_customers = repeat.sort_values("order_count", ascending=False).head(10)
st.dataframe(top_customers)
