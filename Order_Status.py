import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📦 Order Status Overview")

orders = pd.read_csv("data/orders.csv")

status_count = orders["status"].value_counts().reset_index()
status_count.columns = ["status", "count"]

fig = px.pie(status_count, names="status", values="count", title="Order Status Distribution")
st.plotly_chart(fig, use_container_width=True)

st.dataframe(status_count)
