import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Example spending data
data = {'Category': ['Rent', 'Groceries', 'Entertainment', 'Utilities', 'Transportation'],
        'Amount': [1800, 850, 300, 200, 100]}
transactions_df = pd.DataFrame(data)

# Sidebar UI
st.sidebar.header("Select Parameters")
spending_category = st.sidebar.selectbox("Spending Region", ["Germany", "US", "Other"])
chart_type = st.sidebar.selectbox("Chart Type", ["Bar Chart", "Pie Chart"])

# Filter Data
if spending_category == "Germany":
    filtered_data = transactions_df

# Display Chart
if chart_type == "Bar Chart":
    st.subheader(f"{spending_category} Spending - Bar Chart")
    st.bar_chart(filtered_data.set_index('Category')['Amount'])
elif chart_type == "Pie Chart":
    st.subheader(f"{spending_category} Spending - Pie Chart")
    fig, ax = plt.subplots()
    ax.pie(filtered_data['Amount'], labels=filtered_data['Category'], autopct='%1.1f%%')
    st.pyplot(fig)
