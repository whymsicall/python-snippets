# File: magic_8_ball.py
# Description: Magic 8 Ball
# Assignment Name and Number: #13 of Chapter 7
#
# Name: Landon Svatek
# GitHub: whymsicall
#
# On my honor, Landon Svatek, this programming assignment is my own work
# and I have not provided this code to any other student.

import random
import time
question = input("Ask the magic 8 ball a question (press enter to quit): ")  
while question:
    if question == "quit":
        break
    print("Let's see what your future holds")
    print("Let me check real quick")
    for i in range(random.randrange(3,10)):
        print(end=" ")
        time.sleep(1)
    print("\nYour answer is")
    print("Your future is: " +(random.choice(open("responses.txt","r").read().splitlines())) + " .")
    question = input("Ask the magic 8 ball a question (press enter to quit): ")

print("See ya")