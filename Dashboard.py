import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn
import streamlit as st

# Load data
customer = pd.read_csv('customer_df.csv')
new_order_review = pd.read_csv('new_order_reviews_df.csv')
order_payments = pd.read_csv('order_payments_df.csv')
orders = pd.read_csv('orders_df.csv')

# Sidebar for visualization selection
with st.sidebar:
    st.image('ecomerce.png')
    
    # Select Visualization
    visualizations = st.multiselect("Select Visualization", 
                                     ["Customer by Country", "Customer by City", 
                                      "Review Scores", "Payment Methods", "Order Status"])
    
    # Initialize filters
    selected_payment_type = []
    selected_review_score = []
    selected_state = []
    selected_city = []
    selected_order_status = []

    # Show filters based on selected visualizations
    if "Customer by City" in visualizations:
        payment_types = order_payments['payment_type'].unique()
        selected_payment_type = st.multiselect("Select Payment Type", payment_types, default=payment_types.tolist())
        
        review_scores = new_order_review['review_score'].unique()
        selected_review_score = st.multiselect("Select Review Score", review_scores, default=review_scores.tolist())
        
        customer_states = customer['customer_state'].unique()
        selected_state = st.multiselect("Select Customer State", customer_states, default=customer_states.tolist())
        
        # Filter for top 10 cities
        top_cities = customer.groupby('customer_city').customer_id.nunique().nlargest(10).index.tolist()
        selected_city = st.multiselect("Select Customer City", top_cities, default=top_cities)
        
        order_statuses = orders['order_status'].unique()
        selected_order_status = st.multiselect("Select Order Status", order_statuses, default=order_statuses.tolist())

# Visualization logic based on selections
if "Customer by Country" in visualizations:
    # Code for Customer by Country visualization
    pass

if "Customer by City" in visualizations:
    # Code for Customer by City visualization
    pass

if "Review Scores" in visualizations:
    # Code for Review Scores visualization
    pass

if "Payment Methods" in visualizations:
    # Code for Payment Methods visualization
    pass

if "Order Status" in visualizations:
    # Code for Order Status visualization
    pass


   
