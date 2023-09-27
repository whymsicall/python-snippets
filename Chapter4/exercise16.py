# File: <exercise16>
# Description: <Program that uses nested loops to make a pattern>
# Assignment Name and Number: #16 of Chapter 4
#
# Name: <Landon Svatek>
# GitHub: <whymsicall>
#
# On my honor, <Landon Svatek>, this programming assignment is my own work
# and I have not provided this code to any other student.

import turtle

num_squares = 3
t = turtle.Turtle()
t.pendown()
side = side_unit = 30

while True:
    try:
        num_squares = int(input('input the number of squares: '))
    except ValueError:
        print("please enter an integer")
    if num_squares > 3:
        break

for sq in range(1, num_squares + 1):
    t.left(90)
    t.forward(side)
    t.left(90)
    t.forward(side)
    t.left(90)
    t.forward(side)
    t.left(90)
    side = side_unit + 3 * sq  

    t.goto(0,0)                

turtle.done()