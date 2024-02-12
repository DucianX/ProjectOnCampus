from pair_of_dice import PairOfDice


class GameController:
    def __init__(self):
        self.pair_of_dice = PairOfDice()
        self.point = None


    def roll(self):
        self.pair_of_dice.roll_dice()
        return self.pair_of_dice.current_value()
    

    def check_win_or_lose_first_roll(self, value):
        # value here is the roll instance from the dice_game
        if value in [2, 3, 12]:
            return "lose"
        elif value in [7, 11]:
            return "win"
        else:
            self.point = value
            return "continue"
            
    def check_win_or_lose_subsequent_rolls(self, value):
        if value == self.point:
            return "win"
        elif value == 7:
            return "lose"
        else:
            return "continue"
