# File: stadium_seating.py
# Description: Stadium Seating
# Assignment Name and Number: #7 of Chapter 5
#
# Name: Landon Svatek
# GitHub: whymsicall
#
# On my honor, Landon Svatek, this programming assignment is my own work
# and I have not provided this code to any other student.


class_a = int(input("how many tickets sold for Class A: "))
print("------------------------------------------")
class_b = int(input("how many tickets sold for Class B: "))
print("------------------------------------------")
class_c = int(input("how many tickets sold for Class C: "))
print("------------------------------------------")


cl_a = 20
cl_b = 15
cl_c = 10

a_sales = cl_a*class_a
b_sales = cl_b*class_b
c_cales = cl_c*class_c

all_sales = a_sales + b_sales + c_cales

print(" ")
print(" ")
print("------------------------------------------")
print("Class A \t Class B \t Class C")
print(f"${a_sales} \t\t ${b_sales} \t\t ${c_cales}")
print(f"combined sales: {all_sales}")
print("------------------------------------------")
