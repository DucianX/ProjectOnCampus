import math

def main():
    x1 = input("x1 = ")
    y1 = input("y1 = ")
    x2 = input("x2 = ")
    y2 = input("y2 = ")

    dis = math.sqrt((float(x1) - float(x2)) ** 2 + (float(y1) - float(y2)) ** 2)
    print(dis)

main()