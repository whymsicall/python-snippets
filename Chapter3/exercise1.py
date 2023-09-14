Z = "zero"
P = "positive"
N = "negative"
O = "odd"
E = "even"

integer = int(input("Enter a random number: "))

if integer > 0:
    print(f"{integer} is a {P} number")
elif integer < 0:
    print(f"{integer} is a {N} number")
elif integer == 0:
    print(f"{integer} is a {Z} number")

if (integer % 2) == 0:
    print(f"{integer} is {E}")
else:
    print(f"{integer} is {O}")