R = float(input("Enter the length of the row, in feet: "))
E = float(input("Enter amount of space used by an end-post assembly: "))
S = float(input("Enter the amount of space you would like to have between the vines, in feet: "))

V = (R - (2 * E)) / S

print("Number of grapevines that will fit in a row: ", V)
