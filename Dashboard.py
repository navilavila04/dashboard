import pandas as pd
import matplotlib as plt
import seaborn as sn
import streamlit as st

customer=pd.read_csv('D:\\Dashboard\\dashboard\customer_df.csv')
new_order_review=pd.read_csv('D:\\Dashboard\\dashboard\\new_order_reviews_df.csv')
order_payments=pd.read_csv('D:\\Dashboard\\dashboard\\order_payments_df.csv')
orders=pd.read_csv('D:\\Dashboard\\dashboard\\orders_df.csv')


with st.sidebar:
    st.image('D:\\Dashboard\\dashboard\\ecomerce.png')

st.header('E-Commerce')

st.subheader('Negara Customer')

bystate_df = customer.groupby(by="customer_state").customer_id.nunique().reset_index()
bystate_df.rename(columns={"customer_id": "customer_count"}, inplace=True)

plt.pyplot.figure(figsize=(12, 7))

colors = ["#72BCD4"] + ["#D3D3D3"] * (len(bystate_df) - 1)

sn.barplot(
    x="customer_state",
    y="customer_count",
    hue="customer_state",
    data=bystate_df.sort_values(by="customer_count", ascending=False),
    palette=colors
)

plt.pyplot.title("Jumlah Customers Berdasarkan Negara", loc="center", fontsize=16)
plt.pyplot.xlabel("")  
plt.pyplot.ylabel("")

st.pyplot (plt.pyplot)

st.subheader('Kota Customer')

bystate_df = customer.groupby(by="customer_city").customer_id.nunique().reset_index()
bystate_df.rename(columns={"customer_id": "customer_count"}, inplace=True)

top_10_bystate_df = bystate_df.sort_values(by="customer_count", ascending=False).head(10)

plt.pyplot.figure(figsize=(12, 7))

colors = ["#72BCD4"] + ["#D3D3D3"] * (len(top_10_bystate_df) - 1)

sn.barplot(
    x="customer_city",
    y="customer_count",
    hue="customer_city",
    data=top_10_bystate_df,
    palette=colors
)

plt.pyplot.title("Top 10 Jumlah Customers Berdasarkan Kota", loc="center", fontsize=16)

plt.pyplot.xticks(rotation=55)
plt.pyplot.xlabel("")  
plt.pyplot.ylabel("")

st.pyplot(plt.pyplot)

st.subheader('Score Reviews')

review = new_order_review.groupby(by="review_score").review_id.count().sort_values(ascending=False).reset_index()


plt.pyplot.figure(figsize=(7, 5))
sn.barplot(
    x="review_score",
    y="review_id",
    data=review,
    color="#72BCD4" ) 

plt.pyplot.title("Review Score dari Customers", loc="center", fontsize=16)
plt.pyplot.xlabel(" ")
plt.pyplot.ylabel(" ")
st.pyplot(plt.pyplot)


st.subheader('Metode Pembayaran')

pay_type = order_payments.groupby(by="payment_type").order_id.count().sort_values(ascending=False).reset_index()


plt.pyplot.figure(figsize=(5, 5))

sn.barplot(
    x="payment_type",
    y="order_id",
    data=pay_type,
    color="#72BCD4"  
)


plt.pyplot.title("Metode Pembayaran dari Customers", loc="center", fontsize=16)
plt.pyplot.xticks(rotation=55)
plt.pyplot.xlabel("")
plt.pyplot.ylabel("")


st.pyplot(plt.pyplot)

st.subheader('Status Order')

order_stat = orders.groupby(by="order_status").order_id.count().sort_values(ascending=False).reset_index()


plt.pyplot.figure(figsize=(7, 5))


sn.barplot(
    x="order_status",
    y="order_id",
    data=order_stat,
    color="#72BCD4"  
)


plt.pyplot.title("Status Order Customers", loc="center", fontsize=16)


plt.pyplot.xticks(rotation=55)
plt.pyplot.xlabel("")
plt.pyplot.ylabel("")

st.pyplot(plt.pyplot)
