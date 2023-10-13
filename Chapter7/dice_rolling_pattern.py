# File: dice_rolling_program.py
# Description: Dice Rolling Program
# Assignment Name and Number: #6 of Chapter 7
#
# Name: Landon Svatek
# GitHub: whymsicall
#
# On my honor, Landon Svatek, this programming assignment is my own work
# and I have not provided this code to any other student.
import random

def main():
    num_dice = int(input("How many dice do you want to roll? "))
    result = roll_dice(num_dice)
    print(f"The total for {num_dice} rolls was {result}")

def roll_dice(num_dice):
    rolls = 0
    for i in range(1, num_dice + 1):
        print(f"Roll #{i} = {(roll := random.randint(1,6))}")
        rolls += roll
    return rolls

main()