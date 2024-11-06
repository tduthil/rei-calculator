# components/analysis_display.py
import streamlit as st

def display_investment_summary(results: dict):
    """Display investment summary metrics"""
    st.subheader("Investment Summary")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Monthly Cash Flow", f"${results['cash_flow']/12:,.2f}")
    with col2:
        st.metric("Annual NOI", f"${results['noi']:,.2f}")
    with col3:
        st.metric("Cash on Cash Return", f"{results['cash_on_cash_return']:.2f}%")

def display_detailed_analysis(property_info: dict, rental_info: dict, results: dict, expense_input_type: str):
    """Display detailed property analysis"""
    with st.expander("View Detailed Analysis"):
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Property Overview")
            st.write(f"Address: {property_info['address']}")
            st.write(f"Purchase Price: ${property_info['purchase_price']:,.2f}")
            st.write(f"Monthly Rent: ${rental_info['monthly_rent']:,.2f}")
            st.write(f"Annual Gross Rent: ${rental_info['monthly_rent'] * 12:,.2f}")
            
            st.subheader("Income Breakdown")
            st.write(f"Gross Monthly Rent: ${results['monthly_gross_rent']:,.2f}")
            st.write(f"Monthly Vacancy Loss: ${results['vacancy_loss']/12:,.2f}")
            st.write(f"Effective Monthly Income: ${results['effective_gross_income']/12:,.2f}")
            st.write(f"Monthly Mortgage Payment: ${results['monthly_mortgage']:,.2f}")
        
        with col2:
            st.subheader("Annual Expenses")
            annual_rent = rental_info['monthly_rent'] * 12
            
            for expense, amount in results['annual_expenses'].items():
                if expense_input_type == "Dollar Amount":
                    st.write(f"{expense.replace('_', ' ').title()}: ${amount:,.2f}")
                else:
                    percentage = (amount / annual_rent * 100) if annual_rent > 0 else 0
                    st.write(f"{expense.replace('_', ' ').title()}: {percentage:.1f}% (${amount:,.2f})")
            
            st.write("---")
            total_expenses = results['total_annual_expenses']
            if expense_input_type == "Dollar Amount":
                st.write(f"Total Annual Expenses: ${total_expenses:,.2f}")
            else:
                total_percentage = (total_expenses / annual_rent * 100) if annual_rent > 0 else 0
                st.write(f"Total Annual Expenses: {total_percentage:.1f}% (${total_expenses:,.2f})")