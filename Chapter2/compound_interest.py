# File: compound_interest.py
# Description: Compound Interest
# Assignment Name and Number: #14 of Chapter 2
#
# Name: Landon Svatek
# GitHub: whymsicall
#
# On my honor, Landon Svatek, this programming assignment is my own work
# and I have not provided this code to any other student.

P = float(input("Enter principal amount that was originally deposited into the account: "))
R = float(input("Enter the annual interest rate: "))
N = int(input("Enter the number of times per year that the interest is compounded: "))
T = float(input("Enter the number of years the account will be left to earn interest: "))

amount = P * (1 + (R * .01) / N) ** (N * T)

print("The amount of money will be in the account after", T, "years:", round(amount,2))
