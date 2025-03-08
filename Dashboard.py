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
    ["Customer by Country", "Customer by City", "Review Scores", "Payment Methods", "Order Status"])

# Initialize filters
payment_types = order_payments['payment_type'].unique().tolist()
review_scores = new_order_review['review_score'].unique().tolist()
customer_states = customer['customer_state'].unique().tolist()
customer_cities = customer['customer_city'].unique().tolist()
order_statuses = orders['order_status'].unique().tolist()

# Function to add "All" option
def add_all_option(options):
    return ["All"] + options

# Select filters
selected_payment_types = st.sidebar.multiselect("Select Payment Type", 
    add_all_option(payment_types), default=add_all_option(payment_types))
selected_review_scores = st.sidebar.multiselect("Select Review Score", 
    add_all_option(review_scores), default=add_all_option(review_scores))
selected_customer_states = st.sidebar.multiselect("Select Customer State", 
    add_all_option(customer_states), default=add_all_option(customer_states))
selected_customer_cities = st.sidebar.multiselect("Select Customer City", 
    add_all_option(customer_cities), default=add_all_option(customer_cities))
selected_order_statuses = st.sidebar.multiselect("Select Order Status", 
    add_all_option(order_statuses), default=add_all_option(order_statuses))

# Function to handle "All" selection
def handle_all_selection(selected, options):
    if "All" in selected:
        return options
    return selected

# Filter data based on selections
filtered_orders = orders[orders['order_status'].isin(handle_all_selection(selected_order_statuses, order_statuses))]
filtered_payments = order_payments[order_payments['payment_type'].isin(handle_all_selection(selected_payment_types, payment_types))]
filtered_reviews = new_order_review[new_order_review['review_score'].isin(handle_all_selection(selected_review_scores, review_scores))]
filtered_customers = customer[customer['customer_state'].isin(handle_all_selection(selected_customer_states, customer_states)) & 
                              customer['customer_city'].isin(handle_all_selection(selected_customer_cities, customer_cities))]

# Display selected visualizations
if "Customer by Country" in visualization_options:
    st.subheader('Negara Customer')
    bystate_df = filtered_customers.groupby(by="customer_state").customer_id.nunique().reset_index()
    bystate_df.rename(columns={"customer_id": "customer_count"}, inplace=True)

    plt.figure(figsize=(12, 7))
    sn.barplot(x="customer_state", y="customer_count", data=bystate_df.sort_values(by="customer_count", ascending=False), palette="Blues")
    plt.title("Jumlah Customers Berdasarkan Negara", loc="center", fontsize=16)
    st.pyplot(plt)

if "Customer by City" in visualization_options:
    st.subheader('Kota Customer')
    bystate_df = filtered_customers.groupby(by="customer_city").customer_id.nunique().reset_index()
    bystate_df.rename(columns={"customer_id": "customer_count"}, inplace=True)

    top_10_bystate_df = bystate_df.sort_values(by="customer_count", ascending=False).head(10)

    plt.figure(figsize=(12, 7))
    sn.barplot(x="customer_city", y="customer_count", data=top_10_bystate_df, palette="Blues")
    plt.title("Top 10 Jumlah Customers Berdasarkan Kota", loc="center", fontsize=16)
    plt.xticks(rotation=55)
    st.pyplot(plt)

if "Review Scores" in visualization_options:
    st.subheader('Score Reviews')
    review = filtered_reviews.groupby(by="review_score").review_id.count().sort_values(ascending=False).reset_index()

    plt.figure(figsize=(7, 5))
    sn.barplot(x="review_score", y="review_id", data=review, color="#72BCD4")
    plt.title("Review Score dari Customers", loc="center", fontsize=16)
    st.pyplot(plt)

if "Payment Methods" in visualization_options:
    st.subheader('Metode Pembayaran')
    pay_type = filtered_payments.groupby(by="payment_type").order_id.count().sort_values(ascending=False).reset_index()

    plt.figure(figsize=(5, 5))
    sn.barplot(x="payment_type", y="order_id", data=pay_type, color="#72BCD4")
    plt.title("Metode Pembayaran dari Customers", loc="center", fontsize=16)
    st.pyplot(plt)

if "Order Status" in visualization_options:
    st.subheader('Status Order')
    order_stat = filtered_orders.groupby(by="order_status").order_id.count().sort_values(ascending=False).reset_index()

    plt.figure(figsize=(7, 5))
    sn.barplot(x="order_status", y="order_id", data=order_stat, color="#72BCD4")
    plt.title("Status Order Customers", loc="center", fontsize=16)
    st.pyplot(plt)

   
