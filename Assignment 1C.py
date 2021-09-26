try:
    total_cost = 1000000
    annual_salary = float(input("Enter your annual salary:"))
except Exception:
    print("Enter a valid decimal number")
else:
    portion_down_payment = 0.25*total_cost
    semi_annual_raise = 0.07
    r = 0.04

    # Calculates the monthly increase and returns the new monthly salary
    def salary_increment(monthly_pay, current_month, increase):
        if current_month % 6 == 0:
            monthly_pay = (monthly_pay * increase) + monthly_pay
        return monthly_pay

    def get_num_months(cost, salary, pct_saved, pct_increase):
        savings = 0
        months_saved = 0
        monthly_salary = salary / 12
        down_payment = 0.25*cost
        while down_payment - 100 >= savings:
            months_saved = months_saved + 1
            monthly_salary = salary_increment(monthly_salary, months_saved, pct_increase)
            savings = pct_saved * monthly_salary + savings + savings * (r / 12)
#        print("Savings:", savings)
        return months_saved

    months = 36
    start = 0
    end = 1.0000
    steps = 0
    portion_saved = (start + end)/2
    computed_months = 0
    try:
        while computed_months != months:
            steps = steps + 1
            computed_months = get_num_months(total_cost, annual_salary, portion_saved, semi_annual_raise)
            if computed_months > months:
                start = portion_saved
            else:
                end = portion_saved
            if abs(end - start) <= 0.01:
                raise ValueError
#            print("Start:", start, "End:",  end)
            portion_saved = (start + end)/2
        print("Best Savings Rate:", portion_saved)
        print("Steps in bisection search:", steps)
    except ValueError:
        print("It is not possible to print the down payment in three years.")