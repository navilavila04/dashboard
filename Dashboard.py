import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn
import streamlit as st

# Load data
customer = pd.read_csv('customer_df.csv')
new_order_review = pd.read_csv('new_order_reviews_df.csv')
order_payments = pd.read_csv('order_payments_df.csv')
orders = pd.read_csv('orders_df.csv')

# Sidebar for filters
with st.sidebar:
    st.image('ecomerce.png')
    
    # Select Visualization
    visualization_options = [
        "Customer by Country",
        "Customer by City (Top 10)",
        "Score Reviews",
        "Payment Methods",
        "Order Status"
    ]
    selected_visualizations = st.multiselect("Select Visualizations", visualization_options)

    # Initialize filters
    payment_types = order_payments['payment_type'].unique()
    review_scores = new_order_review['review_score'].unique()
    customer_states = customer['customer_state'].unique()
    
    # Show filters based on selected visualizations
    if "Customer by Country" in selected_visualizations:
        selected_state = st.multiselect("Select Customer State", customer_states, default=customer_states.tolist())
    
    if "Customer by City (Top 10)" in selected_visualizations:
        selected_state_city = st.multiselect("Select Customer State for City", customer_states, default=customer_states.tolist())
    
    if "Score Reviews" in selected_visualizations:
        selected_review_score = st.multiselect("Select Review Score", review_scores, default=review_scores.tolist())
    
    if "Payment Methods" in selected_visualizations:
        selected_payment_type = st.multiselect("Select Payment Type", payment_types, default=payment_types.tolist())
    
    if "Order Status" in selected_visualizations:
        order_statuses = orders['order_status'].unique()
        selected_order_status = st.multiselect("Select Order Status", order_statuses, default=order_statuses.tolist())

# Filter data based on selections
filtered_customers = customer[customer['customer_state'].isin(selected_state)]
filtered_orders = orders[orders['order_status'].isin(selected_order_status)]
filtered_payments = order_payments[order_payments['payment_type'].isin(selected_payment_type)]
filtered_reviews = new_order_review[new_order_review['review_score'].isin(selected_review_score)]

# E-Commerce Header
st.header('E-Commerce')

# Visualization for selected options
if "Customer by Country" in selected_visualizations:
    st.subheader('Negara Customer')
    bystate_df = filtered_customers.groupby(by="customer_state").customer_id.nunique().reset_index()
    bystate_df.rename(columns={"customer_id": "customer_count"}, inplace=True)

    plt.figure(figsize=(12, 7))
    colors = ["#72BCD4"] + ["#D3D3D3"] * (len(bystate_df) - 1)

    sn.barplot(
        x="customer_state",
        y="customer_count",
        hue="customer_state",
        data=bystate_df.sort_values(by="customer_count", ascending=False),
        palette=colors
    )

    plt.title("Jumlah Customers Berdasarkan Negara", loc="center", fontsize=16)
    plt.xlabel("")  
    plt.ylabel("")
    st.pyplot(plt)

if "Customer by City (Top 10)" in selected_visualizations:
    st.subheader('Kota Customer')
    bystate_df = filtered_customers.groupby(by="customer_city").customer_id.nunique().reset_index()
    bystate_df.rename(columns={"customer_id": "customer_count"}, inplace=True)

    top_10_bystate_df = bystate_df.sort_values(by="customer_count", ascending=False).head(10)

    plt.figure(figsize=(12, 7))
    colors = ["#72BCD4"] + ["#D3D3D3"] * (len(top_10_bystate_df) - 1)

    sn.barplot(
        x="customer_city",
        y="customer_count",
        hue="customer_city",
        data=top_10_bystate_df,
        palette=colors
    )

    plt.title("Top 10 Jumlah Customers Berdasarkan Kota", loc="center", fontsize=16)
    plt.xticks(rotation=55)
    plt.xlabel("")  
    plt.ylabel("")
    st.pyplot(plt)

if "Score Reviews" in selected_visualizations:
    st.subheader('Score Reviews')
    review = filtered_reviews.groupby(by="review_score").review_id.count().sort_values(ascending=False).reset_index()

    plt.figure(figsize=(7, 5))
    sn.barplot(
        x="review_score",
        y="review_id",
        data=review,
        color="#72BCD4"
    )

    plt.title("Review Score dari Customers", loc="center", fontsize=16)
    plt.xlabel(" ")
    plt.ylabel(" ")
    st.pyplot(plt)

if "Payment Methods" in selected_visualizations:
    st.subheader('Metode Pembayaran')
    pay_type = filtered_payments.groupby(by="payment_type").order_id.count().sort_values(ascending=False).reset_index()

    plt.figure(figsize=(5, 5))
    sn.barplot(
        x="payment_type",
        y="order_id",
        data=pay_type,
        color="#72BCD4"
    )

    plt.title("Metode Pembayaran dari Customers", loc="center", fontsize=16)
    plt.xticks(rotation=55)
    plt.xlabel("")
    plt.ylabel("")
    st.pyplot(plt)

if "Order Status" in selected_visualizations:
    st.subheader('Status Order')
    order_stat = filtered_orders.groupby(by="order_status").order_id.count().sort_values(ascending=False).reset_index()

    plt.figure(figsize=(7, 5))
    sn.barplot(
        x="order_status",
        y="order_id",
        data=order_stat,
        color="#72BCD4"
    )

    plt.title("Status Order Customers", loc="center", fontsize=16)
    plt.xticks(rotation=55)
    plt.xlabel("")
    plt.ylabel("")
    st.pyplot(plt)


   
