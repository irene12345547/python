def calculate_due_amount(total_bill, payment):
    if payment > total_bill:
        return "Error: Payment exceeds the total bill amount."
    due_amount = total_bill - payment
    return due_amount
total_bill = float(input("Enter the total bill amount:  "))
payment = float(input("Enter the total bill amount :  "))
due_amount = calculate_due_amount(total_bill,  payment)
print(f"Remaining due amount: {due_amount}")