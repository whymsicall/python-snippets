# File: calories_from_fat_and_carbohydrates.py
# Description: Calories Burned From Fat And Carbohydrates
# Assignment Name and Number: #6 of Chapter 5
#
# Name: Landon Svatek
# GitHub: whymsicall
#
# On my honor, Landon Svatek, this programming assignment is my own work
# and I have not provided this code to any other student.


fg = int(input("enter number of fat grams you consumed today: "))
cg = int(input("enter number of carbohydrate grams you consumed today: "))

fc = fg*9
cc = cg*4

print(f"You have consumed {fc} fat calories today")
print(f"You have consumed {cg} of carb calories today")