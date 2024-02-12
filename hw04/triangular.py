import sys


def calculate_triangular_number(n):
    return (n * (n + 1)) // 2


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 triangular.py <number>")
        return
    

    try:
        number = int(sys.argv[1])
        if number < 1:
            print("Please enter a positive integer.")
        else:
            result = calculate_triangular_number(number)
            print(f"The triangular number of {number} is {result}")
    except ValueError:
        print("Invalid input. Please enter a positive integer")


if __name__ == "__main__":
    main()