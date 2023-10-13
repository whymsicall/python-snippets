# File: lotto_number_gen.py
# Description: Lottery Number Generator
# Assignment Name and Number: #2 of Chapter 7
#
# Name: Landon Svatek
# GitHub: whymsicall
#
# On my honor, Landon Svatek, this programming assignment is my own work
# and I have not provided this code to any other student.

import random
loop = 7
lotto = []
for i in range(loop):
    lotto.append(random.randrange(0, 10))
print(lotto)