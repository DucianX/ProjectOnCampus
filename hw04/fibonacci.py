import sys


def fibonacci(n):
    n = int(sys.argv[1])
    n0 = 0
    n1 = 1
    fib_list = [0, 1]
    # Generate the list and print the slice
    if n > 2:
        for i in range(2, n+1):
            fib_list.append(fib_list[i-2] + fib_list[i-1])
    return fib_list[:n]

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 fibonacci.py <number>")
        return
    

    try:
        result = fibonacci(sys.argv[1])
        print(f"{result}")
    except ValueError:
        print("Invalid input. Please enter a positive integer")


if __name__ == "__main__":
    main()
        
