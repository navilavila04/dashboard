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
    visualizations = st.multiselect("Select Visualization", 
                                     ["Customer by Country", "Customer by City", "Review Scores", "Payment Methods", "Order Status"])
    
    # Payment Type Filter
    payment_types = order_payments['payment_type'].unique().tolist()
    payment_types.insert(0, "All")  # Add "All" option
    selected_payment_type = st.multiselect("Select Payment Type", payment_types, default=payment_types)

    if "All" in selected_payment_type:
        selected_payment_type = payment_types[1:]  # Select all except "All"

    # Review Score Filter
    review_scores = new_order_review['review_score'].unique().tolist()
    review_scores.insert(0, "All")  # Add "All" option
    selected_review_score = st.multiselect("Select Review Score", review_scores, default=review_scores)

    if "All" in selected_review_score:
        selected_review_score = review_scores[1:]  # Select all except "All"

    # Customer State Filter
    customer_states = customer['customer_state'].unique().tolist()
    customer_states.insert(0, "All")  # Add "All" option
    selected_state = st.multiselect("Select Customer State", customer_states, default=customer_states)

    if "All" in selected_state:
        selected_state = customer_states[1:]  # Select all except "All"

    # Customer City Filter
    customer_cities = customer['customer_city'].unique().tolist()
    customer_cities.insert(0, "All")  # Add "All" option
    selected_city = st.multiselect("Select Customer City", customer_cities, default=customer_cities)

    if "All" in selected_city:
        selected_city = customer_cities[1:]  # Select all except "All"

    # Order Status Filter
    order_statuses = orders['order_status'].unique().tolist()
    order_statuses.insert(0, "All")  # Add "All" option
    selected_order_status = st.multiselect("Select Order Status", order_statuses, default=order_statuses)

    if "All" in selected_order_status:
        selected_order_status = order_statuses[1:]  # Select all except "All"

# Filter data based on selections
filtered_orders = orders[orders['order_status'].isin(selected_order_status)]
filtered_payments = order_payments[order_payments['payment_type'].isin(selected_payment_type)]
filtered_reviews = new_order_review[new_order_review['review_score'].isin(selected_review_score)]
filtered_customers = customer[customer['customer_state'].isin(selected_state) & customer['customer_city'].isin(selected_city)]

# E-Commerce Header
st.header('E-Commerce')

# Render visualizations based on user selection
if "Customer by Country" in visualizations:
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

if "Customer by City" in visualizations:
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

if "Review Scores" in visualizations:
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

if "Payment Methods" in visualizations:
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

if "Order Status" in visualizations:
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


   
