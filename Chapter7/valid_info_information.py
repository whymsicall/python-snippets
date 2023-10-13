# File: valid_number_information.py
# Description: Valid Number Information
# Assignment Name and Number: #1 of Chapter 7
#
# Name: Landon Svatek
# GitHub: whymsicall
#
# On my honor, Landon Svatek, this programming assignment is my own work
# and I have not provided this code to any other student.

numbers = [74, 19, 105, 20, -2, 67, 77, 124, -45, 38]
valid_numbers = []
total = 0
count = 0

for n in numbers:
    if 0 <= n <= 100:
        valid_numbers.append(n)
        total += n
        count += 1
if count > 0:
    average = total / count
else:
    0

print("original numbers:", numbers)
print("total of numbers:", total)
print("average of numbers:", average)