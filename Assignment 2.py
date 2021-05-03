total_cost = float(input("Enter the cost of your dream home:"))
annual_salary = float(input("Enter your annual salary:"))
portion_saved = float(input("Enter the percentage of salary saved (as a decimal):"))
portion_down_payment = 0.25*total_cost
r = 0.04
monthly_salary = annual_salary/12
current_savings = 0
months = 0
while current_savings < portion_down_payment:
    current_savings = portion_saved*monthly_salary + current_savings + current_savings*(r/12)
    months = months + 1
print("Number of months:", months)


