import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Example dataset
data = pd.DataFrame({
    'Category': ['Rent', 'Groceries', 'Utilities', 'Entertainment', 'Transportation'],
    'Amount': [1800, 845.98, 179.20, 154.67, 62.80]
})

# Sidebar UI
st.sidebar.header("Select Parameters")
spending_category = st.sidebar.selectbox("Spending Region", ["Germany", "US", "Other"])
chart_type = st.sidebar.selectbox("Chart Type", ["Bar Chart", "Pie Chart"])

# Filter Data
# Here we simulate filtering logic. Replace this with actual filtering based on your dataset.
if spending_category == "Germany":
    filtered_data = data  # Example: Use the same data for Germany
elif spending_category == "US":
    filtered_data = data  # Example: Use the same data for US
else:
    filtered_data = data  # Example: Use the same data for Other

# Ensure filtered_data has the required columns
if 'Category' in filtered_data.columns and 'Amount' in filtered_data.columns:
    # Display Chart
    if chart_type == "Bar Chart":
        st.subheader(f"{spending_category} Spending - Bar Chart")
        st.bar_chart(filtered_data.set_index('Category')['Amount'])
    elif chart_type == "Pie Chart":
        st.subheader(f"{spending_category} Spending - Pie Chart")
        fig, ax = plt.subplots()
        ax.pie(filtered_data['Amount'], labels=filtered_data['Category'], autopct='%1.1f%%')
        ax.set_title(f"{spending_category} Spending")
        st.pyplot(fig)
else:
    st.error("Filtered data does not have the required 'Category' and 'Amount' columns.")
