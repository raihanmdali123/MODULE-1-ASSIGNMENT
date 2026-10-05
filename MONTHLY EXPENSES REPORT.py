#MODULE 1
#PERSONAL EXPENSE CALCULATOR
name=input(" Enter your name: ")
monthly_income=float(input("Enter your salary: "))
rent=float(input("Enter Your Rent: "))
food_expenses=float(input("Enter your food expense: "))
travel_expense=float(input("Enter your travel expense: "))
entertainment_expenses=float(input("Enter your Entertainment expenses: "))
Other_expenses=float(input("Enter your other expenses: "))

Total_expenses=(rent+food_expenses+travel_expense+entertainment_expenses+Other_expenses)
remaining_money=monthly_income-Total_expenses
saving_percentage=(Total_expenses/monthly_income)*100

Daily_average_expenses=Total_expenses/30
weekly_average_expenses=Total_expenses/4
A_saving_target=(input("Enter your saving target: "))

print(f"""My name is:{name}\n
My salary is:{monthly_income}\n
My Total expenses:{Total_expenses}\n
My remaining money is:{remaining_money}\n
My saving percentage is:{saving_percentage}\n
My daily average expenses is:{Daily_average_expenses}\n
My weekly average expenses is:{weekly_average_expenses}\n
My saving target is:{A_saving_target}\n""")


