# components/property_form.py
import streamlit as st

def render_property_info():
    """Render property information section"""
    st.subheader("Property Information")
    col1, col2 = st.columns(2)
    
    with col1:
        property_name = st.text_input("Property Name")
        address = st.text_input("Address")
        purchase_price = st.number_input("Purchase Price ($)", min_value=0.0, value=300000.0)
    
    with col2:
        monthly_rent = st.number_input("Monthly Rent ($)", min_value=0.0, value=2000.0)
        vacancy_rate = st.number_input("Vacancy Rate (%)", min_value=0.0, max_value=100.0, value=5.0)
    
    return {
        'name': property_name,
        'address': address,
        'purchase_price': purchase_price
    }, {
        'monthly_rent': monthly_rent,
        'vacancy_rate': vacancy_rate
    }

def render_financing_info():
    """Render financing information section"""
    st.subheader("Financing Information")
    col1, col2 = st.columns(2)
    
    with col1:
        down_payment_percent = st.number_input("Down Payment (%)", min_value=0.0, max_value=100.0, value=20.0)
        interest_rate = st.number_input("Interest Rate (%)", min_value=0.0, max_value=100.0, value=6.99)
    
    with col2:
        mortgage_years = st.number_input("Mortgage Term (Years)", min_value=1, max_value=40, value=30)
    
    return {
        'down_payment_percent': down_payment_percent,
        'interest_rate': interest_rate,
        'mortgage_years': mortgage_years
    }
