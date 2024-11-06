# Home.py
import streamlit as st
from utils.state_management import initialize_state

# Set page config
st.set_page_config(
    page_title="Rental Property Calculator",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state
initialize_state()

# Main page content
st.title("Rental Property Calculator")
st.write("""
Welcome to the Rental Property Calculator! This tool helps you analyze rental property investments 
by calculating key metrics such as cash flow, NOI, and return on investment.

### Features:
- Calculate monthly and annual returns
- Track expenses as dollar amounts or percentages
- Save and compare multiple properties
- Detailed investment analysis
- Easy expense management

### Getting Started:
1. Navigate to the Calculator page
2. Enter property details and expenses
3. View the analysis
4. Save properties to compare later

Use the sidebar to navigate between pages.
""")



