imonthly = int(input("Enter your monthly income: "))
emonthly = int(input("Enter your total monthly expenses: "))
msave = imonthly - emonthly
ysave = int(msave * 12 + (msave * 12 * 0.05))
print(f"Your monthly savings are ${msave}.")
print(f"Projected savings after one year, with interest, is: %{ysave}.")
