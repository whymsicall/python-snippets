# File: restaurant_selector.py
# Description: Restaurant Selector
# Assignment Name and Number: #18 of Chapter 3
#
# Name: Landon Svatek
# GitHub: whymsicall
#
# On my honor, Landon Svatek, this programming assignment is my own work
# and I have not provided this code to any other student.

vegetarian = input("are any members of your party vegetarian: ")
vegan = input("are any members of your party vegan: ")
gluten_free = input("are any members of your party gluten free: ")

if vegetarian == 'yes' and vegan == 'yes' and gluten_free == 'yes':
    print("Corner cafe and The Chef's Kitchen are your options")
elif vegetarian == 'yes' and vegan == 'no' and gluten_free == 'yes':
    print("Main Street Pizza Company, Corner Cafe, and The Chef's Kitchen are your options")
elif vegetarian == 'no' and vegan == 'no' and gluten_free == 'no':
    print("Joe's Gourmet Diner, Main Street Pizza Company, Corner Cafe, Mama's Fine Italian, and The Chef's Kitchen are your options")
elif vegetarian == 'yes' and vegan == 'no' and gluten_free == 'no':
    print("Main Street Pizza Company, Corner Cafe, Mama's Fine Italian, and The Chef's Kitchen are your options")
elif vegetarian == 'no' and vegan == 'no' and gluten_free == 'yes':
    print("Main Street Pizza Company, Corner Cafe, and The Chef's Kitchen are your options")
elif vegetarian == 'no' and vegan == 'yes' and gluten_free == 'no':
    print("Corner Cafe and The Chef's Kitchen are your options")
elif vegetarian == 'yes' and vegan == 'yes' and gluten_free == 'no':
    print("Corner Cafe and The Chef's Kitchen are your options")
elif vegetarian == 'no' and vegan == 'yes' and gluten_free == 'yes':
    print("Corner Cafe and The Chef's Kitchen are your options")