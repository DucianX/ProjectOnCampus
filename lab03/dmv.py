import random

def produce_license():
    print("Welcome to the DMV (estimated wait time is 3 hours)")
    name = input("Please enter your first, middle, and last name:\n")
    birth = input("Enter date of birth (MM/DD/YY):\n")
    name_splited = name.split()
    if len(name_splited) == 3:
        first_name, middle_name, last_name = name_splited
    if len(name_splited) == 2:
        first_name, last_name = name_splited
        middle_name = ''
    birth2 = birth[:-2] + "21"

    print("-------------------------------------")
    print("Washington Driver License")
    
    number = ""
    for i in range(7):
        number += str(random.randint(0, 9))

    print("DL ",number)
    print("LN ",last_name)
    print("FN ",first_name + ' ' + middle_name)
    print("DOB ",birth)
    print("EXP ",birth2)
    print("-------------------------------------")

produce_license()
