# components/expense_input.py
import streamlit as st

def calculate_expense_values(expense_input_type: str, purchase_price: float, annual_rent: float):
    """Calculate default expense values based on input type"""
    if expense_input_type == "Dollar Amount":
        return {
            'property_taxes': float(purchase_price * 0.0125),
            'insurance': float(purchase_price * 0.0025),
            'maintenance': float(purchase_price * 0.005),
            'utilities': 1016.0,
            'property_management': float(annual_rent * 0.08),
            'other_expenses': 0.0
        }
    else:
        return {
            'property_taxes_pct': float(purchase_price * 0.0125 / annual_rent * 100),
            'insurance_pct': float(purchase_price * 0.0025 / annual_rent * 100),
            'maintenance_pct': float(purchase_price * 0.005 / annual_rent * 100),
            'utilities_pct': float(1016 / annual_rent * 100),
            'property_management_pct': 8.0,
            'other_expenses_pct': 0.0
        }

def render_expense_inputs(purchase_price: float, annual_rent: float):
    """Render expense input section"""
    st.subheader("Annual Expenses")
    expense_input_type = st.radio(
        "Expense Input Type",
        ["Dollar Amount", "Percentage of Gross Rent"],
        horizontal=True
    )
    
    default_values = calculate_expense_values(expense_input_type, purchase_price, annual_rent)
    
    col1, col2 = st.columns(2)
    expenses = {}
    
    with col1:
        if expense_input_type == "Dollar Amount":
            expenses['property_taxes'] = st.number_input(
                "Property Taxes ($)", 
                value=default_values['property_taxes'],
                help="Typically 1.25% of purchase price"
            )
            expenses['insurance'] = st.number_input(
                "Insurance ($)", 
                value=default_values['insurance'],
                help="Typically 0.25% of purchase price"
            )
            expenses['maintenance'] = st.number_input(
                "Maintenance ($)", 
                value=default_values['maintenance'],
                help="Typically 0.5% of purchase price"
            )
        else:
            property_taxes_pct = st.number_input(
                "Property Taxes (% of Gross Rent)", 
                value=default_values['property_taxes_pct'],
                help="Enter as percentage of gross rent"
            )
            expenses['property_taxes'] = annual_rent * (property_taxes_pct / 100)
            
            insurance_pct = st.number_input(
                "Insurance (% of Gross Rent)", 
                value=default_values['insurance_pct'],
                help="Enter as percentage of gross rent"
            )
            expenses['insurance'] = annual_rent * (insurance_pct / 100)
            
            maintenance_pct = st.number_input(
                "Maintenance (% of Gross Rent)", 
                value=default_values['maintenance_pct'],
                help="Enter as percentage of gross rent"
            )
            expenses['maintenance'] = annual_rent * (maintenance_pct / 100)
    
    with col2:
        if expense_input_type == "Dollar Amount":
            expenses['utilities'] = st.number_input(
                "Utilities ($)", 
                value=default_values['utilities']
            )
            expenses['property_management'] = st.number_input(
                "Property Management ($)", 
                value=default_values['property_management'],
                help="Typically 8-10% of rental income"
            )
            expenses['other_expenses'] = st.number_input(
                "Other Expenses ($)", 
                value=default_values['other_expenses']
            )
        else:
            utilities_pct = st.number_input(
                "Utilities (% of Gross Rent)", 
                value=default_values['utilities_pct'],
                help="Enter as percentage of gross rent"
            )
            expenses['utilities'] = annual_rent * (utilities_pct / 100)
            
            property_management_pct = st.number_input(
                "Property Management (% of Gross Rent)", 
                value=default_values['property_management_pct'],
                help="Typically 8-10% of rental income"
            )
            expenses['property_management'] = annual_rent * (property_management_pct / 100)
            
            other_expenses_pct = st.number_input(
                "Other Expenses (% of Gross Rent)", 
                value=default_values['other_expenses_pct'],
                help="Enter as percentage of gross rent"
            )
            expenses['other_expenses'] = annual_rent * (other_expenses_pct / 100)
    
    return expenses, expense_input_type
