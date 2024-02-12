import sys


def calculate_triangular_number(n):
    return (n * (n + 1)) // 2


def main():
    tri_list = []
    while True:
        user_input = input("Enter a number, or enter 'done': ")
        if user_input.lower() == 'done':
            break
        num = calculate_triangular_number(int(user_input))
        print(f"The triangular number for {user_input} is {num}")
        tri_list.append(int(user_input))
        
    print(tri_list)
        


if __name__ == "__main__":
    main()