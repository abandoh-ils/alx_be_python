monthly_income = int(input("Enter your monthly income: "))
monthly_expense = int(input("Enter your monthly expense: "))
monthly_savings = monthly_income - monthly_expense

projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

print("Your monthly savings are ${}.".format(monthly_savings))

print("Projected savings after one year, with interest, is: ${}.".format(projected_savings))