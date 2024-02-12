import sys
import math

def draw_circle(radius):
    for y in range(-radius, radius):
        for x in range(-radius, radius): #!!!this is so-called the grid.
            distance = math.sqrt(x**2 + y**2)
            if distance <= radius:
                print("o", end="")
            else:
                print(" ", end="")
        print()  # Move to the next line after each row

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 circle.py <radius>")
        return

    try:
        radius = int(sys.argv[1])
        if radius < 1:
            print("Please enter a positive integer for the radius.")
            return

        draw_circle(radius)

    except ValueError:
        print("Invalid input. Please enter a positive integer for the radius.")

main()