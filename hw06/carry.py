def get_digits(n):
    return [int(digit) for digit in str(n)]
    # Convert a numebr to a list of digits.

def add_with_carry(num1, num2):
    # gets two lists
    if len(num2) > len(num1):
        num1, num2 = num2, num1
    

    num1 = num1[::-1]
    num2 = num2[::-1]
    # lists are reversed

    result = []
    carry = 0
    carries_count = 0


    for i in range(len(num1)): # i=0:unit place; i=1:tens place; i=2:hundreds place
        total = carry
        total += num1[i]
        total += num2[i] if i < len(num2) else 0

        if total >= 10:
            carry = total // 10 # the number added to the next column
            carries_count += 1
        else:
            carry = 0
        
        result.append(total % 10)
    
    if carry:
        result.append(carry) # when end, if carry still exist, add it.

    # Return the result and carries count
    return result[::-1], carries_count # reverse the list of places of numbers back


def main():
    # Input
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    # Convert numbers to list of digits
    digits_num1 = get_digits(num1)
    digits_num2 = get_digits(num2)

    # Process
    sum_digits, carries = add_with_carry(digits_num1, digits_num2)
    total = int(''.join(map(str, sum_digits)))

    # Output
    print(f"{num1} + {num2} = {total}")
    print(f"Number of carries: {carries}")

if __name__ == "__main__":
    main()



        