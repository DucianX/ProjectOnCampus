from game_controller import GameController

def main():
    print("--------------------------------")
    print("Welcome to street craps!\n")
    print("Rules:")
    print("If you roll 7 or 11 on your first roll, you win.")
    print("If you roll 2, 3, or 12 on your first role, you lose.")
    print("If you roll anything else, that's your 'point', and")
    print("you keep rolling until you either roll your point")
    print("again (win) or roll a 7 (lose)\n")
    
    game = GameController()
    input("Press enter to roll the dice...")
    
    roll = game.roll()
    
    if game.point is None:
        result = game.check_win_or_lose_first_roll(roll)
        if result == "continue":
            print(f"Your point is {roll}")
        elif result == "win":
            print(f"You rolled {roll}. You win!\n\n")
            return
        else:
            print(f"You rolled {roll}. You lose.\n\n")
            return

    while True: # Keep looping until return
        input("Press enter to roll the dice...")
        roll = game.roll()
        result = game.check_win_or_lose_subsequent_rolls(roll)
        if result == "continue":
            print(f"You rolled {roll}.")
        elif result == "win":
            print(f"You rolled {roll}. You win!\n\n")
            return
        else:
            print(f"You rolled {roll}. You lose.\n\n")
            return

if __name__ == "__main__":
    main()
