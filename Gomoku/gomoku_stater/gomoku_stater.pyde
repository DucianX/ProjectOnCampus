from stone import Stone
from board import Board
from ai import AI
import time


SIZE = 1200
STROKE_WEIGHT = 4
R_OF_STONE = 30
stones = []
ai_stones = []
colorOfStone = "Black"
cellDivider = 16 # equals to num of crosses - 1
cellSize = SIZE / cellDivider # 75
board = Board(SIZE, cellDivider, cellSize, STROKE_WEIGHT)
ai = AI(board)
WINNING_COUNT = 5
ai_has_moved = False
game_over = False
R = 210
G = 180
B = 140
ROUND_COUNT = 1
Player_score = 0

def setup():
    """draw the background"""
    size(SIZE, SIZE)
    background(R, G, B)
    textSize(150)
    textAlign(CENTER, CENTER)


def input(self, message=''):
    from javax.swing import JOptionPane
    return JOptionPane.showInputDialog(frame, message)

def draw():
    """draw the stones"""
    global colorOfStone, AI_START_TIME, ai_turn, game_over
    if not game_over:
        board.display()
        # Draw all stones
        for stone in stones:
            stone.display()
        if board.board_full():
            text("GAME OVER", width / 2, height / 2)
    if game_over:
        textSize(64)  # Setting the text size
        textAlign(CENTER, CENTER)  # Aligning the text to center
        fill(0)  # Setting the text color (black in this case)
        text("GAME OVER", width / 2, height / 2)  # Displaying the text in the middle of the canvas

def mousePressed():
    """place new stones and record their places"""
    # Declare we are using global xa, ya, not create new two
    global xa, ya, ai_has_moved, xa1, ya1, game_over, WINNING_COUNT, Player_score
    
    if board.board_full():
        game_over = True
        if game_over:
            print("=======================================")
            print("Game Over! FULL!")
            print("=======================================")

    if board.board_full() == False and not game_over:
        global colorOfStone, ROUND_COUNT, ai_location
        x, y = board.get_nearest_point(mouseX, mouseY)
        # Now we only have x and y at the canvas, yet to make them fit in array!
        # Once they are fit in, make them x1 and y1!
        if not board.is_occupied(x, y):
            print("Round " + str(ROUND_COUNT) + " started.")
            # Player's turn
            x = int(x)
            y = int(y)

            # class Stone for display, so it uses "raw" x and y.
            new_stone = Stone(x, y, R_OF_STONE, colorOfStone)
            stones.append(new_stone)
            new_stone.display()

            # board.record_location takes raw x and y. It converts them inside the function.
            board.record_location(x, y)
            board.record_color(x, y, colorOfStone)
            x1 = int(x / cellSize)
            y1 = int(y / cellSize)

            # Check if player win
            print("Color: " + str(colorOfStone))
            print("Checked Game Over Status.\n")
            if board.check_for_win(x1, y1, colorOfStone):
                print("=======================================")
                print("Game Over! Black WIN!")
                print("=======================================")
                game_over = True
                

            # Now Player's turn is over, we change color.
            colorOfStone = "White" if colorOfStone == "Black" else "Black"

            # AI's turn
            # We only pass array-sized x1 and y1 into AI!
            # To execute a series of move according to player's move
            if ai_has_moved: # moved at least once
                if ai.win_move(xa1, ya1, board):
                    ai_location = ai.win_move(xa1, ya1, board)
                elif ai.find_blocking_move(board, x1, y1, ai_has_moved, xa1, ya1):
                    ai_location = ai.find_blocking_move(board, x1, y1, ai_has_moved, xa1, ya1)
                elif ai.potential_block(x1, y1, board):
                    ai_location = ai.potential_block(x1, y1, board)
                else:
                    ai_location = ai.follow_move(x1, y1)
            # If there's no need to block, AI will calculate best move.
            elif not ai_has_moved:
                print("AI has not moved yet\n")
                ai_location = ai.follow_move(x1, y1)
                ai_has_moved = True
            elif ai_has_moved and ai.find_best_move(x1, y1, xa1, ya1, board):
                ai_location = ai.find_best_move()
            

            # We got AI's location and get it on board
            print(ai_location)
            # xa and ya is scaled back to the board size
            xa = int(ai_location[0] * cellSize)
            ya = int(ai_location[1] * cellSize)
            print("xa, ya = " + str(xa) + ", " + str(ya))

            # xa1 and ya1 is good for array
            xa1 = int(ai_location[0])
            ya1 = int(ai_location[1])
            print("xa1, ya1 = " + str(xa1) + ", " + str(ya1))
            print("AI location:" + str(xa1) + "," + str(ya1) + "\n")
            ai_stone = Stone(xa, ya, R_OF_STONE, colorOfStone)
            stones.append(ai_stone)
            ai_stone.display()
            board.record_location(xa, ya)
            board.record_ai_location(xa, ya)
            board.record_color(xa, ya, colorOfStone)


            # Check if AI win
            print("Color: " + str(colorOfStone))
            if board.check_for_win(xa1, ya1, colorOfStone):
                print("=======================================")
                print("Game Over! White WIN!")
                print("=======================================")
                game_over = True
            
            # Now AI's turn is over, we change color.
            colorOfStone = "White" if colorOfStone == "Black" else "Black"
            if not game_over:
                print("=======================================")
                print("ROUND " + str(ROUND_COUNT) + " is over.")
                print("=======================================")
                ROUND_COUNT += 1
