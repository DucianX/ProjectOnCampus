import math


def diamond_printer():
    # Convert the input into integer
    user_input = input("Height: ")
    height = int(user_input)
    # To caculate the blanks in front of * in 
    # the 1ST ROW
    blank_front_initial = (height - 1) // 2
    i = 1
    num_of_aster = 1
    # i is for count the rows
    # Case for odd height
    # Upper
    for i in range((height + 1) // 2 - 1):
        print(blank_front_initial * ' ' + num_of_aster * '*')
        num_of_aster += 2
        blank_front_initial -= 1
        # Handle the even height as a special case: extra line
        if height % 2 == 0:
            if i == (height + 1) // 2 - 2:
                print(blank_front_initial * ' ' + num_of_aster * '*')
    # Lower
    i = 1
    for i in range((height + 1) // 2):
        print(blank_front_initial * ' ' + num_of_aster * '*')
        num_of_aster -= 2
        blank_front_initial += 1

    
if __name__ == "__main__":
    diamond_printer()