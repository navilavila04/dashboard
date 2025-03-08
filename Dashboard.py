import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn
import streamlit as st

# Load data
customer = pd.read_csv('customer_df.csv')
new_order_review = pd.read_csv('new_order_reviews_df.csv')
order_payments = pd.read_csv('order_payments_df.csv')
orders = pd.read_csv('orders_df.csv')

# Sidebar for selecting visualizations
st.sidebar.image('ecomerce.png')

# Select Visualization
visualization_options = st.sidebar.multiselect("Select Visualization", 
    ["Negara Customers", "Kota Customers", "Score Reviews", "Metode Pembayaran", "Status Order"])

# Initialize filters
selected_payment_type = []
selected_review_score = []
selected_state = []
selected_city = []
selected_order_status = []

# Show filters based on selected visualizations
if "Negara Customers" in visualization_options:
    selected_state = st.sidebar.multiselect("Select Customer State", customer['customer_state'].unique())

if "Kota Customers" in visualization_options:
    selected_city = st.sidebar.multiselect("Select Customer City", 
        customer[customer['customer_state'].isin(selected_state)]['customer_city'].value_counts().head(10).index)

if "Score Reviews" in visualization_options:
    selected_review_score = st.sidebar.multiselect("Select Review Score", new_order_review['review_score'].unique())

if "Metode Pembayaran" in visualization_options:
    selected_payment_type = st.sidebar.multiselect("Select Payment Type", order_payments['payment_type'].unique())

if "Status Order" in visualization_options:
    selected_order_status = st.sidebar.multiselect("Select Order Status", orders['order_status'].unique())

# Filter data based on selections
filtered_customers = customer[customer['customer_state'].isin(selected_state)]
filtered_orders = orders[orders['order_status'].isin(selected_order_status)]
filtered_payments = order_payments[order_payments['payment_type'].isin(selected_payment_type)]
filtered_reviews = new_order_review[new_order_review['review_score'].isin(selected_review_score)]

# Render visualizations based on selected options
if "Negara Customers" in visualization_options:
    st.header('Negara Customers')
    bystate_df = filtered_customers.groupby(by="customer_state").customer_id.nunique().reset_index()
    bystate_df.rename(columns={"customer_id": "customer_count"}, inplace=True)

    plt.figure(figsize=(12, 7))
    sn.barplot(x="customer_state", y="customer_count", data=bystate_df.sort_values(by="customer_count", ascending=False), color="#72BCD4")
    plt.title("Jumlah Customers Berdasarkan Negara", loc="center", fontsize=16)
    st.pyplot(plt)

if "Kota Customers" in visualization_options:
    st.header('Kota Customers')
    bycity_df = filtered_customers.groupby(by="customer_city").customer_id.nunique().reset_index()
    bycity_df.rename(columns={"customer_id": "customer_count"}, inplace=True)

    top_10_bystate_df = bycity_df.sort_values(by="customer_count", ascending=False).head(10)

    plt.figure(figsize=(12, 7))
    sn.barplot(x="customer_city", y="customer_count", data=top_10_bystate_df, color="#72BCD4")
    plt.title("Top 10 Jumlah Customers Berdasarkan Kota", loc="center", fontsize=16)
    st.pyplot(plt)

if "Score Reviews" in visualization_options:
    st.header('Score Reviews')
    review = filtered_reviews.groupby(by="review_score").review_id.count().sort_values(ascending=False).reset_index()

    plt.figure(figsize=(7, 5))
    sn.barplot(x="review_score", y="review_id", data=review, color="#72BCD4")
    plt.title("Review Score dari Customers", loc="center", fontsize=16)
    st.pyplot(plt)

if "Metode Pembayaran" in visualization_options:
    st.header('Metode Pembayaran')
    pay_type = filtered_payments.groupby(by="payment_type").order_id.count().sort_values(ascending=False).reset_index()

    plt.figure(figsize=(5, 5))
    sn.barplot(x="payment_type", y="order_id", data=pay_type, color="#72BCD4")
    plt.title("Metode Pembayaran dari Customers", loc="center", fontsize=16)
    st.pyplot(plt)

if "Status Order" in visualization_options:
    st.header('Status Order')
    order_stat = filtered_orders.groupby(by="order_status").order_id.count().sort_values(ascending=False).reset_index()

    plt.figure(figsize=(7, 5))
    sn.barplot(x="order_status", y="order_id", data=order_stat, color="#72BCD4")
    plt.title("Status Order Customers", loc="center", fontsize=16)
    st.pyplot(plt)

   
