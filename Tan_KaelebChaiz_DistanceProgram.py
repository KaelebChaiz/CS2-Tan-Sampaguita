import math

# Asks the user to enter the coordinates of the first point
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))

# Asks the user to enter the coordinates of the second point
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

# Computes the distance using the distance formula
distance = math.sqrt(pow(x2-x1, 2) + pow(y2-y1, 2))

# Prints the distance
print("The distance between the two points is:", distance)
