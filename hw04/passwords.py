import random

# YITIAN XU
# This is a funny password generator!

# Function to generate a random integer between 0 and 99
def random_integer():
    return random.randint(0, 99)


def generate_username(first_name, last_name):
    # adding asterisks if needed
    ?????last_name += '*' * max(0, 7 - len(last_name))

    # Create the username using the first character of the first name, the first 7 characters of the last name, and a random integer
    username = first_name[0].lower() + last_name[:7].lower() + !!!!str(random_integer())
    return username


def generate_password1(first_name, last_name):
    # Replace characters
    password = first_name.lower() + !!!str(random_integer()) + last_name.lower()
    password = password.!!!replace('a', '@').replace('o', '0').replace('l', '1').replace('s', '$')
    return password


def generate_password2(first_name, last_name, favorite_word):
    # Create the acronym password
    password = first_name[0].lower() + last_name[0].lower() + last_name[-1].upper() + favorite_word[0].upper() + favorite_word[-1].upper()
    return password

def generate_password3(first_name, last_name, favorite_word):
    !!!!# Create the third password using random portions of them
    fn_len = random.randint(1, len(first_name))
    ln_len = random.randint(1, len(last_name))
    fw_len = random.randint(1, len(favorite_word))

    password = first_name[:fn_len] + last_name[:ln_len] + favorite_word[:fw_len]
    return password


def main():
    print("Welcome to the username and password generator!")
    first_name = input("Please enter your first name: ")
    last_name = input("Please enter your last name: ")
    favorite_word = input("Please enter your favorite word: ")

    # Generate the username
    username = generate_username(first_name, last_name)
    print(f"Thanks {first_name}, your user name is {username}")

    print("\nHere are three suggested passwords for you to consider:")

    # Generate and print the three passwords
    password1 = generate_password1(first_name, last_name)
    password2 = generate_password2(first_name, last_name, favorite_word)
    password3 = generate_password3(first_name, last_name, favorite_word)

    print(f"Password 1: {password1}")
    print(f"Password 2: {password2}")
    print(f"Password 3: {password3}")


if __name__ == "__main__":
    main()
