P = float(input("Enter principal amount that was originally deposited into the account: "))
R = float(input("Enter the annual interest rate: "))
N = int(input("Enter the number of times per year that the interest is compounded: "))
T = float(input("Enter the number of years the account will be left to earn interest: "))

amount = P * (1 + (R * .01) / N) ** (N * T)

print("The amount of money will be in the account after", T, "years:", round(amount,2))
