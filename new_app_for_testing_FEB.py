import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Example dataset
data = pd.DataFrame({
    'Category': ['Rent', 'Groceries', 'Utilities', 'Entertainment', 'Transportation'],
    'Amount': [1800, 845.98, 179.20, 154.67, 62.80]
})

# Sidebar UI
st.sidebar.header("Select Parameters")
spending_category = st.sidebar.selectbox("Spending Region", ["Germany", "US", "Norway", "Italy"])
chart_type = st.sidebar.selectbox("Chart Type", ["Bar Chart", "Pie Chart", "Heatmap"])

# Filter data (example logic; replace with your actual filtering)
filtered_data = data  # Example static filtering for now

# Display Charts
if chart_type == "Bar Chart":
    st.subheader(f"{spending_category} Spending - Bar Chart")
    if 'Category' in filtered_data.columns and 'Amount' in filtered_data.columns:
        st.bar_chart(filtered_data.set_index('Category')['Amount'])
    else:
        st.error("Filtered data does not have the required 'Category' and 'Amount' columns.")

elif chart_type == "Pie Chart":
    st.subheader(f"{spending_category} Spending - Pie Chart")
    if 'Category' in filtered_data.columns and 'Amount' in filtered_data.columns:
        fig, ax = plt.subplots()
        ax.pie(filtered_data['Amount'], labels=filtered_data['Category'], autopct='%1.1f%%')
        st.pyplot(fig)
    else:
        st.error("Filtered data does not have the required 'Category' and 'Amount' columns.")

elif chart_type == "Heatmap":
    st.subheader(f"{spending_category} Spending - Heatmap")
    # Example transformation for a heatmap; replace with your actual data logic
    heatmap_data = pd.DataFrame({
        'Week': ['Week 1', 'Week 2', 'Week 3', 'Week 4'],
        'Rent': [450, 460, 470, 480],
        'Groceries': [200, 180, 220, 210],
        'Utilities': [50, 55, 60, 65],
        'Entertainment': [100, 120, 80, 90],
        'Transportation': [30, 40, 35, 45]
    }).set_index('Week')

    fig, ax = plt.subplots(figsize=(8, 4))
    sns.heatmap(heatmap_data, annot=True, fmt=".1f", cmap="coolwarm", cbar=True, ax=ax)
    st.pyplot(fig)
