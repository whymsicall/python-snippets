# File: calculating_the_factorial_of_a_number
# Description: Calculating the Factorial of a Number
# Assignment Name and Number: #12 of Chapter 4
#
# Name: Landon Svatek
# GitHub: whymsicall
#
# On my honor, Landon Svatek, this programming assignment is my own work
# and I have not provided this code to any other student.


number = int(input("Enter a nonnegative integer: "))
f = 1
if number < 0:
    print("Error, there is no factorial for the negative numbers")
elif number == 0:
    print("the factorial of 0 is 1")
else:
    for i in range(1, number + 1):
        f = f*i
    print("The factorial of", number, 'is', f)
