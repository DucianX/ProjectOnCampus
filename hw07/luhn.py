import sys


def digit_modify(x):
    x = int(x * 2)
    if (x >= 10):
        x = x // 10 + x % 10
    return x


def main(num):
    num_list = [0] * len(num)
    i = 0
    # make a list, each element is a digit
    for digit in num:
        num_list[i] = int(digit)
        i += 1
    # modify!
    for i in range(len(num_list) - 2, -1, -1):
        num_list[i] = digit_modify(num_list[i])
    # sum!
    sum = 0
    for x in num_list:
        sum += x
    if (not sum % 10):
        print("Valid")
    else:
        print("Fake!")


if __name__ == "__main__":
    main(sys.argv[1])
