import math

def solver(a, b, c):
    if a == 0:
        return -1
    else:
        delta = b**2 - 4*a*c
        if delta < 0:
            return []
        elif delta == 0:
            x = -b / (2*a)
            return [x]
        else:
            x1 = (-b - math.sqrt(delta)) / (2*a)
            x2 = (-b + math.sqrt(delta)) / (2*a)
            return [x1, x2]

a = int(input("Enter the first parameter: "))
b = int(input("Enter the second parameter: "))
c = int(input("Enter the third parameter: "))

result = solver(a, b, c)
if result != -1:
    if len(result) == 0:
        print("The equation has no real solutions.")
    elif len(result) == 1:
        print("The equation has one solution:", result[0])
    else:
        print("The equation has two solutions:", result[0], "and", result[1])
else:
    print("This is not a quadratic equation.")
