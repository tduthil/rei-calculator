# pages/1_Calculator.py
import streamlit as st
from utils.calculations import calculate_returns
from utils.state_management import save_property_analysis
from components.property_form import render_property_info, render_financing_info
from components.expense_input import render_expense_inputs
from components.analysis_display import display_investment_summary, display_detailed_analysis

st.title("Property Calculator")

with st.form("property_form"):
    # Render property information section
    property_info, rental_info = render_property_info()
    
    # Render financing section
    financing_info = render_financing_info()
    
    # Calculate annual rent for expense calculations
    annual_rent = rental_info['monthly_rent'] * 12
    
    # Render expense section
    expense_info, expense_input_type = render_expense_inputs(
        property_info['purchase_price'],
        annual_rent
    )
    
    # Submit button
    submitted = st.form_submit_button("Calculate and Save Analysis")
    
    if submitted:
        # Calculate returns
        results = calculate_returns(
            property_info,
            rental_info,
            financing_info,
            expense_info
        )
        
        # Save analysis
        save_property_analysis({
            'property_info': property_info,
            'rental_info': rental_info,
            'financing_info': financing_info,
            'expense_info': expense_info,
            'results': results
        })
        
        # Display results
        display_investment_summary(results)
        display_detailed_analysis(
            property_info,
            rental_info,
            results,
            expense_input_type
        )