import random
def guess():
    tries = 0
    ran_num = random.randint(1, 50)
    user_number = input("Welcome to the Guessing Game!\nI picked a number between 1 and 50. Try and guess!\n")
    while int(user_number) != ran_num:
    # loop until the answer is correct
        difference = int(user_number) - ran_num
        abs_difference = abs(difference)
        tries += 1
        if abs_difference <= 1:
            temp = "scalding hot"
        elif abs_difference <= 2:
            temp = "extremely warm"
        elif abs_difference <= 3:
            temp = "very warm"
        elif abs_difference <= 5:
            temp = "warm"
        elif abs_difference <= 8:
            temp = "cold"
        elif abs_difference <= 13:
            temp = "very cold"
        elif abs_difference <= 20:
            temp = "extremely cold"
        elif abs_difference >= 20:
            temp = "icy freezing miserably cold"
        #get the correct temp

        print(f"Your guess is {temp}")
        user_number = input()
    
    print(f"Congratulations. You figured it out in {tries} tries.")
    if tries == 1:
        print("That was lucky!")
    if 2 <= tries <= 4:
        print("That was amazing!")
    if 5 <= tries <= 6:
        print("That was okay.")
    if tries == 7:
        print("Meh.")
    if 8 <= tries <= 9:
        print("This is not your game.")
    if tries >= 10:
        print("OMG. Come on, man. You did that on purpose.")

guess()
        


        
