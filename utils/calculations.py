# utils/calculations.py
def calculate_mortgage_payment(loan_amount: float, rate: float, years: int) -> float:
    """Calculate monthly mortgage payment"""
    monthly_rate = rate / 1200
    num_payments = years * 12
    return loan_amount * (monthly_rate * (1 + monthly_rate)**num_payments) / ((1 + monthly_rate)**num_payments - 1)

def calculate_returns(property_info: dict, rental_info: dict, financing_info: dict, expense_info: dict) -> dict:
    """Calculate property returns"""
    # Basic calculations
    loan_amount = property_info['purchase_price'] * (1 - financing_info['down_payment_percent'] / 100)
    monthly_mortgage = calculate_mortgage_payment(
        loan_amount,
        financing_info['interest_rate'],
        financing_info['mortgage_years']
    )
    
    # Monthly income calculations
    monthly_gross_rent = rental_info['monthly_rent']
    monthly_vacancy_loss = monthly_gross_rent * (rental_info['vacancy_rate'] / 100)
    monthly_effective_income = monthly_gross_rent - monthly_vacancy_loss
    
    # Monthly expense calculations
    monthly_expenses = {
        expense: amount / 12 
        for expense, amount in expense_info.items()
    }
    monthly_total_expenses = sum(monthly_expenses.values())
    
    # Monthly cash flow
    monthly_noi = monthly_effective_income - monthly_total_expenses
    monthly_cash_flow = monthly_noi - monthly_mortgage
    
    # Annual calculations
    annual_gross_rent = monthly_gross_rent * 12
    annual_vacancy_loss = monthly_vacancy_loss * 12
    annual_effective_income = monthly_effective_income * 12
    annual_expenses = expense_info
    annual_total_expenses = sum(annual_expenses.values())
    annual_noi = annual_effective_income - annual_total_expenses
    annual_mortgage = monthly_mortgage * 12
    annual_cash_flow = monthly_cash_flow * 12
    
    # Returns
    down_payment = property_info['purchase_price'] * (financing_info['down_payment_percent'] / 100)
    cash_on_cash_return = (annual_cash_flow / down_payment) * 100 if down_payment > 0 else 0
    
    return {
        'monthly_mortgage': monthly_mortgage,
        'monthly_gross_rent': monthly_gross_rent,
        'monthly_vacancy_loss': monthly_vacancy_loss,
        'monthly_effective_income': monthly_effective_income,
        'monthly_expenses': monthly_expenses,
        'monthly_total_expenses': monthly_total_expenses,
        'monthly_noi': monthly_noi,
        'monthly_cash_flow': monthly_cash_flow,
        
        'annual_gross_rent': annual_gross_rent,
        'vacancy_loss': annual_vacancy_loss,
        'effective_gross_income': annual_effective_income,
        'annual_expenses': annual_expenses,
        'total_annual_expenses': annual_total_expenses,
        'noi': annual_noi,
        'cash_flow': annual_cash_flow,
        'cash_on_cash_return': cash_on_cash_return
    }