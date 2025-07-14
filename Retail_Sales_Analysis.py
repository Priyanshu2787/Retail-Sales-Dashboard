import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import streamlit as st

# Load data
customers = pd.read_csv("data/customers.csv")
products = pd.read_csv("data/products.csv")
sales = pd.read_csv("data/sales.csv")

# Preprocessing
sales['sale_date'] = pd.to_datetime(sales['sale_date'])
df = sales.merge(customers, on='customer_id').merge(products, on='product_id')
df['revenue'] = df['quantity'] * df['price']
df['month'] = df['sale_date'].dt.to_period('M').astype(str)

# Streamlit App
st.title("🛍️ Retail Sales Dashboard")
st.markdown("Explore sales trends, top customers, and product performance.")

# KPIs
total_revenue = df['revenue'].sum()
total_customers = df['customer_id'].nunique()
top_location = df.groupby('location')['revenue'].sum().idxmax()

st.metric("Total Revenue", f"₹{total_revenue:,.0f}")
st.metric("Unique Customers", total_customers)
st.metric("Top Revenue Location", top_location)

st.markdown("### 📈 Monthly Revenue Trend")
monthly_revenue = df.groupby('month')['revenue'].sum().reset_index()
fig1 = px.line(monthly_revenue, x='month', y='revenue', markers=True)
st.plotly_chart(fig1)

st.markdown("### 🥇 Top 5 Products by Revenue")
top_products = df.groupby('product_name')['revenue'].sum().sort_values(ascending=False).head(5).reset_index()
fig2 = px.bar(top_products, x='product_name', y='revenue')
st.plotly_chart(fig2)

st.markdown("### 👑 Top 5 Customers by Spending")
top_customers = df.groupby('customer_name')['revenue'].sum().sort_values(ascending=False).head(5).reset_index()
fig3 = px.bar(top_customers, x='customer_name', y='revenue')
st.plotly_chart(fig3)

st.markdown("### 🏙️ Revenue by City")
city_revenue = df.groupby('location')['revenue'].sum().sort_values(ascending=False).reset_index()
fig4 = px.pie(city_revenue, names='location', values='revenue', title='Revenue Share by City')
st.plotly_chart(fig4)

st.markdown("### 📦 Revenue by Category")
category_revenue = df.groupby('category')['revenue'].sum().reset_index()
fig5 = px.bar(category_revenue, x='category', y='revenue', color='category')
st.plotly_chart(fig5)

st.markdown("----")
st.caption("Built with Python · Pandas · Streamlit · Plotly")
