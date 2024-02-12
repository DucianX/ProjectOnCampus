from stone import Stone
from board import Board

SIZE = 300
STROKE_WEIGHT = 4
R_OF_STONE = 30
stones = []
colorOfStone = "Black"
cellDivider = 4
cellSize = SIZE / cellDivider
board = Board(SIZE, cellDivider, cellSize, STROKE_WEIGHT)
R = 210
G = 180
B = 140


def setup():
    """draw the background"""
    size(SIZE, SIZE)
    background(R, G, B)


def draw():
    """draw the stones"""
    global colorOfStone
    board.display()
    # Draw all stones
    for stone in stones:
        stone.display()


def mousePressed():
    """place new stones and record their places"""
    global colorOfStone
    x, y = board.get_nearest_point(mouseX, mouseY)
    print(x)
    print(y)
    print("\n")
    if not board.is_occupied(x, y):
        new_stone = Stone(x, y, R_OF_STONE, colorOfStone)
        stones.append(new_stone)
        new_stone.display()
        colorOfStone = "White" if colorOfStone == "Black" else "Black"
        board.record_location(x, y)
