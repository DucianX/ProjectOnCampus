import random


class Die:
    def __init__(self):
        # dunder method to initialize the current value
        self.current_value = 0 


    def roll(self):
        # Create a dice result.
        self.current_value = random.randint(1,6)

