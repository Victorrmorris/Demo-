import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configure the Streamlit app
st.set_page_config(page_title="International Spending Insights", layout="wide", initial_sidebar_state="expanded")

# App Title
st.title("🌍 International Spending Insights")
st.markdown("""
Welcome to the **International Spending Insights** app!  
Analyze your spending across regions, track your expenses, and uncover valuable insights to manage your finances effectively.
""")

# Example dataset
data = pd.DataFrame({
    'Category': ['Rent', 'Groceries', 'Utilities', 'Entertainment', 'Transportation'],
    'Amount': [1800, 845.98, 179.20, 154.67, 62.80]
})

# Sidebar UI
st.sidebar.header("Navigation and Chatbot")
spending_category = st.sidebar.selectbox("Spending Region", ["Germany", "US", "Italy", "Norway"])
chart_type = st.sidebar.selectbox("Chart Type", ["Bar Chart", "Pie Chart", "Heatmap"])

# Chatbot Prompt Field in Sidebar
st.sidebar.subheader("Chat with Financial Assistant")
chat_input = st.sidebar.text_area("Ask a question about your finances:", placeholder="e.g., What are my Germany spending habits?")

if st.sidebar.button("Get Insights"):
    if chat_input.strip():
        # Simulated Chatbot Response
        st.sidebar.write("### Chatbot Response:")
        st.sidebar.write(f"**You asked:** {chat_input}")
        st.sidebar.markdown("""
        **Chatbot Suggestion:**  
        Based on your question, here is a short assessment:  
        Housing, including rent, utilities, and internet, formed a significant portion of their spending, complemented by groceries from both the commissary and local supermarkets. Dining out included casual meals at local bakeries and restaurants, with occasional splurges on fine dining for special occasions. Transportation costs covered fuel, public transit, and car maintenance. Recreation and travel featured prominently, with visits to local attractions, weekend trips to neighboring countries, and entertainment like concerts and movies. Other expenses included childcare, school supplies, shopping for seasonal needs, healthcare, and occasional donations or gifts. Seasonal spikes in travel and heating expenses during the holidays and winter months are notable, alongside steady savings contributions to retirement accounts.   
        """)
    else:
        st.sidebar.warning("Please type a question to get insights.")

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
