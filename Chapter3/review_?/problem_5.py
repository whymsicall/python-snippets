amount1 = int(input("enter a number: "))
amount2 = int(input("enter a number: "))

if amount1 > 10:
    if amount2 < 100:
        print(f"{amount1}:{amount2}")
    else:
        print("Please enter a number lower than 100 for amount2")
else:
    print("Please enter a number greater than 10 for amount1")