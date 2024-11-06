# pages/2_Saved_Properties.py
import streamlit as st
import pandas as pd
from utils.state_management import get_saved_properties, clear_saved_properties

st.title("Saved Properties")

saved_properties = get_saved_properties()

if not saved_properties:
    st.write("No saved properties yet. Use the calculator to analyze properties.")
else:
    # Create comparison table with safe data access
    comparison_data = []
    for prop in saved_properties:
        # Safe dictionary access with default values
        property_info = prop.get('property_info', {})
        rental_info = prop.get('rental_info', {})
        results = prop.get('results', {})
        
        # Get monthly rent either from rental_info or results
        monthly_rent = rental_info.get('monthly_rent', 
                                     results.get('monthly_gross_rent', 0))
        
        comparison_data.append({
            'Property': property_info.get('name', 'Unknown'),
            'Purchase Price': f"${property_info.get('purchase_price', 0):,.2f}",
            'Monthly Rent': f"${monthly_rent:,.2f}",
            'Monthly Cash Flow': f"${results.get('cash_flow', 0)/12:,.2f}",
            'Annual NOI': f"${results.get('noi', 0):,.2f}",
            'Cash on Cash Return': f"{results.get('cash_on_cash_return', 0):.2f}%"
        })
    
    df = pd.DataFrame(comparison_data)
    st.table(df)
    
    # Property details
    if saved_properties:
        selected_property = st.selectbox(
            "Select property for detailed view",
            options=[prop.get('property_info', {}).get('name', 'Unknown') 
                    for prop in saved_properties]
        )
        
        if selected_property:
            prop = next(p for p in saved_properties 
                      if p.get('property_info', {}).get('name') == selected_property)
            
            with st.expander("Detailed Analysis"):
                property_info = prop.get('property_info', {})
                rental_info = prop.get('rental_info', {})
                results = prop.get('results', {})
                expense_info = prop.get('expense_info', results.get('annual_expenses', {}))
                
                # Create two columns for the detailed analysis
                col1, col2 = st.columns(2)
                
                with col1:
                    st.subheader("Property Overview")
                    st.write(f"Address: {property_info.get('address', 'N/A')}")
                    st.write(f"Purchase Price: ${property_info.get('purchase_price', 0):,.2f}")
                    monthly_rent = rental_info.get('monthly_rent', 
                                                 results.get('monthly_gross_rent', 0))
                    st.write(f"Monthly Rent: ${monthly_rent:,.2f}")
                    st.write(f"Annual Gross Rent: ${monthly_rent * 12:,.2f}")
                    
                    st.subheader("Financial Metrics")
                    st.write(f"Monthly Cash Flow: ${results.get('cash_flow', 0)/12:,.2f}")
                    st.write(f"Annual NOI: ${results.get('noi', 0):,.2f}")
                    st.write(f"Cash on Cash Return: {results.get('cash_on_cash_return', 0):.2f}%")
                    
                with col2:
                    st.subheader("Annual Expenses")
                    annual_rent = monthly_rent * 12
                    # Add toggle for expense display format
                    expense_display = st.radio(
                        "Display expenses as:",
                        ["Dollar Amount", "Percentage of Gross Rent"],
                        horizontal=True
                    )
                    
                    for expense, amount in expense_info.items():
                        if expense_display == "Dollar Amount":
                            st.write(f"{expense.replace('_', ' ').title()}: ${amount:,.2f}")
                        else:
                            percentage = (amount / annual_rent * 100) if annual_rent > 0 else 0
                            st.write(f"{expense.replace('_', ' ').title()}: {percentage:.1f}% (${amount:,.2f})")
                    
                    st.write("---")
                    total_expenses = sum(expense_info.values())
                    if expense_display == "Dollar Amount":
                        st.write(f"Total Annual Expenses: ${total_expenses:,.2f}")
                    else:
                        total_percentage = (total_expenses / annual_rent * 100) if annual_rent > 0 else 0
                        st.write(f"Total Annual Expenses: {total_percentage:.1f}% (${total_expenses:,.2f})")

    # Add option to clear saved properties
    if st.button("Clear All Saved Properties"):
        clear_saved_properties()