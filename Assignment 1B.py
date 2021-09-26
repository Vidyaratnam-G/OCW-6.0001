try:
    total_cost = float(input("Enter the cost of your dream home:"))
    annual_salary = float(input("Enter your annual salary:"))
    portion_saved = float(input("Enter the percentage of salary saved (as a decimal):"))
    semi_annual_raise = float(input("Enter the semi annual raise (as a decimal):"))
except Exception:
    print("Enter a valid decimal number")
else:
    portion_down_payment = 0.25*total_cost
    r = 0.04
    monthly_salary = annual_salary/12
    current_savings = 0
    months = 0

    # Calculates the monthly increase and returns the new monthly salary
    def salary_increment(monthly_pay, current_month, increase):
        if current_month % 6 == 0:
            monthly_pay = (monthly_pay * increase) + monthly_pay
        return monthly_pay


    while current_savings < portion_down_payment:
        months = months + 1
        monthly_salary = salary_increment(monthly_salary, months, semi_annual_raise)
        current_savings = portion_saved * monthly_salary + current_savings + current_savings * (r / 12)

    print("Number of months:", months)