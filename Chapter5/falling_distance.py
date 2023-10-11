# File: falling_distance.py
# Description: Falling Distance
# Assignment Name and Number: #13 of Chapter 5
#
# Name: Landon Svatek
# GitHub: whymsicall
#
# On my honor, Landon Svatek, this programming assignment is my own work
# and I have not provided this code to any other student.

def main():
    for t in range(1,11):
        print("Distance fall is: ", fallingDistance(t))

G = 9.8

def fallingDistance(time):
    distance = (1 / 2) * G * (time ** 2)
    return distance

if __name__ == "__main__":
    main()