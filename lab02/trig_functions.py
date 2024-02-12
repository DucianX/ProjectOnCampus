import math
import cmath
def main():
    x1 = input("Enter an angle: ")
    x11 = math.radians(float(x1))
    x2 = math.sin(x11)
    x3 = math.cos(x11)

    print("The cosine of " + str(x1) + ' is ' + str(x2))
    print("The sine of " + str(x1) + ' is ' + str(x3))

main()