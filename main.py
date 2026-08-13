import math
import string
from selectors import SelectSelector

print("This can be used to solve any second degree equation")

a = float(input("Give the first coefficient:"))

b = float(input("Give the second coefficient:"))

c = float(input("Give the third and last coefficient:"))

z = b**2 - 4 * a * c

if z == 0:
    x0 = -b/2*a
    print("The solution to your equation is", x0)
elif z > 0:
    x1 = (-b + math.sqrt(z))/2*a
    x2 = (-b - math.sqrt(z))/2*a
    print("The solutions to your equation is", x1, "and", x2)
elif z < 0:
    print("This equation has no solution in Z")