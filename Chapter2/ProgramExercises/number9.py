import math

radius = float(input("Enter the radius of a circle: "))

area = math.pi * (radius**2)
circumference = 2 * math.pi * radius

print('Radius =', radius)
print('Area =', area)
print('Circumference =', circumference)