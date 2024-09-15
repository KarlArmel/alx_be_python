userMonthlyIncome = input("Enter your monthly income:")
userTotalMonthlyExpenses = input("Enter your total monthly expenses:")

monthlySavings = int(userMonthlyIncome) - int(userTotalMonthlyExpenses)
projectedSavings = monthlySavings * 12 + (monthlySavings * 12 * 0.05)

print('Your monthly savings are $',monthlySavings)
print('Projected savings after one year, with interest,is: $',projectedSavings)