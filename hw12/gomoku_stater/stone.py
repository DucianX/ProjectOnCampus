import time


class Stone:
    


    def __init__(self, x, y, r, colorOfStone):
        self.x = x
        self.y = y
        self.r = r
        self.colorOfStone = colorOfStone
        self.WHITE = 255
        self.BLACK = 0


    def display(self):
        """show the stone on the canva"""
        """Draws a stone in b/w in turns"""
        if self.colorOfStone == "White":
            fill(self.WHITE)
            noStroke()
            ellipse(self.x, self.y, self.r*2, self.r*2)
        else:
            fill(self.BLACK)
            noStroke()
            ellipse(self.x, self.y, self.r*2, self.r*2)
   