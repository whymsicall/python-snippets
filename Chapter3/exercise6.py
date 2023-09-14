month = int(input("Enter a month in number format: "))
day = int(input("Enter a day in number format: "))
year = int(input("Enter a two digit year: "))

date = f"{month}/{day}/{year}"

if year == month * day:
    print(f"{date}")
    print("This date is magic")
else:
    print(f"{date}")
    print("This date is NOT magic")