import pandas as pd

# Example dataset
data = pd.DataFrame({
    'Category': ['Rent', 'Groceries', 'Utilities', 'Entertainment', 'Transportation'],
    'Amount': [1800, 845.98, 179.20, 154.67, 62.80]
})

# Filter data (if applicable)
filtered_data = data  # Replace this with actual filtering logic

# Ensure filtered_data has the required columns
if 'Category' in filtered_data.columns and 'Amount' in filtered_data.columns:
    st.bar_chart(filtered_data.set_index('Category')['Amount'])
else:
    st.error("Filtered data does not have the required 'Category' and 'Amount' columns.")

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
