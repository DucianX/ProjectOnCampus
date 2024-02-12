class Board:
    def __init__(self, SIZE, cellDivider, cellSize, STROKE_WEIGHT):
        self.SIZE = SIZE
        self.cellDivider = cellDivider # = 16
        self.cellSize = cellSize
        self.STROKE_WEIGHT = STROKE_WEIGHT
        self.list_size = self.cellDivider # = 16, but according to range, set 16 is right 
        # Record existence
        self.board_list = [[False] * (self.list_size)
                           for i in range(self.list_size)]
        # Record AI's stone
        self.ai_board_list = [[False] * (self.list_size)
                           for i in range(self.list_size)]
        # Record color
        self.color_list = [["None"] * (self.list_size)
                           for i in range(self.list_size)]
        # To keep track of the detect states of align stones
        self.detected_alignments = set()
        self.array_size = cellSize - 1

    def is_occupied(self, x, y):
        """To check if the place is empty"""
        x1 = int(round(x / self.cellSize))
        y1 = int(round(y / self.cellSize))
        return self.board_list[x1][y1]

    def record_location(self, x, y):
        """To record the location of stones"""
        x1 = int(x / self.cellSize)
        y1 = int(y / self.cellSize)
        self.board_list[x1][y1] = True
    
    def record_ai_location(self, x, y):
        """To record the location of stones"""
        x1 = int(x / self.cellSize)
        y1 = int(y / self.cellSize)
        self.ai_board_list[x1][y1] = True

    def record_color(self, x, y, color):
        # To record the color of stones
        x1 = int(x / self.cellSize)
        y1 = int(y / self.cellSize)
        self.color_list[x1][y1] = color
        print("Location: " + str(x1) + " " + str(y1) + " Color of stone recorded as:" + self.color_list[x1][y1])

    def display(self):
        cellSize = self.cellSize
        stroke(0)
        strokeWeight(self.STROKE_WEIGHT)
        # Draw vertical lines
        for i in range(1, self.cellDivider):
            line(cellSize * i, cellSize, cellSize * i,
                 cellSize * (self.cellDivider - 1))
        # Draw horizontal lines
        for i in range(1, self.cellDivider):
            line(cellSize, cellSize * i, cellSize * (self.cellDivider - 1),
                 cellSize * i)

    def get_nearest_point(self, x, y):
        # Snap the x, y to the nearest intersection point
        newX = self.get_back_to_board(round(x / self.cellSize) * self.cellSize)
        newY = self.get_back_to_board(round(y / self.cellSize) * self.cellSize)
        return newX, newY

    def get_back_to_board(self, x):
        """get the outsiders back into the board"""
        if (x < self.cellSize):
            x = self.cellSize
        elif (x > (self.cellDivider - 1) * self.cellSize):
            x = (self.cellDivider - 1) * self.cellSize
        return x

    def board_full(self):
        for row in self.board_list:
            for col in row:
                if col == False:
                    return False
        return True

    # corrected color combo method! other direction have not.
    def check_horizontal(self, x1, y1, COMBO_NUMBER):
        black_count = 1
        white_count = 1
        x = x1
        y = y1
        print("Check horizontal has been invoked.")

        for i in range(1, COMBO_NUMBER): # if combo is 3, the "adder" i need to stop at 2.
            # If a black stone at coordinate(x, y) at array
            if self.color_list[x][y] == "Black":
                # If the stone to its right is black
                # Handle from right to left case
                if (x + i <= 15) and self.color_list[x + i][y] == "Black":
                    print("We found a black adjacent stone to the right!")
                    black_count += 1
                    if black_count == COMBO_NUMBER:
                        return True
                # Handle from left to right case
                if (x - i >= 1) and self.color_list[x - i][y] == "Black":
                    print("sWe found a black adjacent stone to the left!")
                    black_count += 1
                    if black_count == COMBO_NUMBER:
                        return True
            # If white, we do the same thing: This will be added to find_best_move.
            elif self.color_list[x][y] == "White":
                # Handle from right to left case
                if (x + i <= 15) and self.color_list[x + i][y] == "White":
                    print("We found a white adjacent stone to the right!")
                    white_count += 1
                    if white_count == COMBO_NUMBER:
                        return True
                # Handle from left to right case
                if (x - i >= 1) and self.color_list[x - i][y] == "White":
                    print("We found a white adjacent stone to the left!")
                    white_count += 1
                    if white_count == COMBO_NUMBER:
                        return True
            else:
                break # Break if there is a gap in the stone
            
    def check_vertical(self, x1, y1, COMBO_NUMBER):
        black_count = 1
        white_count = 1
        x = x1
        y = y1
        print("Check vertical has been invoked.")
        
        for i in range(1, COMBO_NUMBER): # if combo is 3, the "adder" i need to stop at 2.
            # If a black stone at coordinate(x, y) at array
            if self.color_list[x][y] == "Black":
                # Handle from high to low case
                if (y + i <= 15) and self.color_list[x][y + i] == "Black":
                    print("We found a upper black adjacent stone!")
                    black_count += 1
                    if black_count == COMBO_NUMBER:
                        return True
                # Handle from low to high case
                if (y - i >= 1) and self.color_list[x][y - i] == "Black":
                    print("We found a lower black adjacent stone!")
                    black_count += 1
                    if black_count == COMBO_NUMBER:
                        return True
            # If white, we do the same thing: This will be added to find_best_move.
            elif self.color_list[x][y] == "White":
                if (y + i <= 15) and self.color_list[x][y + i] == "White":
                    print("We found a white adjacent stone to the right!")
                    white_count += 1
                    if white_count == COMBO_NUMBER:
                        return True
                if (y - i >= 1) and self.color_list[x][y - i] == "White":
                    print("We found a white adjacent stone to the left!")
                    white_count += 1
                    if white_count == COMBO_NUMBER:
                        return True
            else:
                break # Break if there is a gap in the stone

    def check_upperleft_lowerright(self, x1, y1, COMBO_NUMBER):
        black_count = 1
        white_count = 1
        x = x1
        y = y1
        print("Check upperleft-lowerright has been invoked.")

        for i in range(1, COMBO_NUMBER): # if combo is 3, the "adder" i need to stop at 2.
                # If a black stone at coordinate(x, y) at array
                if self.color_list[x][y] == "Black":
                    # Handle from high to low case
                    if (x - i >= 1) and (y - i >= 1) and self.color_list[x - i][y - i] == "Black":
                        print("We found a upper left black adjacent stone!")
                        black_count += 1
                        if black_count == COMBO_NUMBER:
                            return True
                    # Handle from low to high case
                    if (x + i <= 15) and (y + i <= 15) and self.color_list[x + i][y + i] == "Black":
                        print("We found a lower right black adjacent stone!")
                        black_count += 1
                        if black_count == COMBO_NUMBER:
                            return True
                # If white, we do the same thing: This will be added to find_best_move.
                elif self.color_list[x][y] == "White":
                    if (x - i >= 1) and (y - i >= 1) and self.color_list[x - i][y - i] == "White":
                        print("We found a upper left white adjacent stone!")
                        white_count += 1
                        if white_count == COMBO_NUMBER:
                            return True
                    if (x + i <= 15) and (y + i <= 15) and self.color_list[x + i][y + i] == "White":
                        print("We found a lower right white adjacent stone!")
                        white_count += 1
                        if white_count == COMBO_NUMBER:
                            return True
                else:
                    print("end:X = " + str(x) + "Y= " + str(y))
                    break # Break if there is a gap in the stone
    
    def check_upperright_lowerleft(self, x1, y1, COMBO_NUMBER):
        black_count = 1
        white_count = 1
        x = x1
        y = y1
        print("Check upperright lowerleft has been invoked.")

        for i in range(1, COMBO_NUMBER): # if combo is 3, the "adder" i need to stop at 2.
                # If a black stone at coordinate(x, y) at array
                if self.color_list[x][y] == "Black":
                    # Handle (placing stone) from high to low case
                    if (y - i >= 1) and (x + i <= 15) and self.color_list[x + i][y - i] == "Black":
                        print("We found a upper right black adjacent stone!")
                        black_count += 1
                        if black_count == COMBO_NUMBER:
                            return True
                    # Handle from low to high case
                    if (x - i >= 1) and (y + i <= 15) and self.color_list[x - i][y + i] == "Black":
                        print("We found a lower left black adjacent stone!")
                        black_count += 1
                        if black_count == COMBO_NUMBER:
                            return True
                # If white, we do the same thing: This will be added to find_best_move.
                elif self.color_list[x][y] == "White":
                    if (y - i >= 1) and (x + i <= 15) and self.color_list[x + i][y - i] == "White":
                        print("We found a upper right white adjacent stone!")
                        white_count += 1
                        if white_count == COMBO_NUMBER:
                            return True

                    if (x - i >= 1) and (y + i <= 15) and self.color_list[x - i][y + i] == "White":
                        print("We found a lower left white adjacent stone!")
                        white_count += 1
                        if white_count == COMBO_NUMBER:
                            return True
                else:
                    break # Break if there is a gap in the stone
                        
  
    def detect_combo(self, x1, y1, COMBO_NUMBER):
        # You should pass in processed x and y
        # To find the winning scene
        # detect combo will always detect the new combo resulted by the lateset stone.
        print("Detect_combo invoked")
        return self.check_horizontal(x1, y1, COMBO_NUMBER) or self.check_upperleft_lowerright(x1, y1, COMBO_NUMBER) or self.check_upperright_lowerleft(x1, y1, COMBO_NUMBER) or self.check_vertical(x1, y1, COMBO_NUMBER)

    def reset_detected_alignments(self):
        self.detected_alignments.clear()

    def check_for_win(self, x, y, color):
        # You should input processed x1 and y1
        """
        Check if there's a winning combination starting from (x, y) for the specified color.
        """
        print("Check! " + str(color) + ".")
        return (
            self.check_line(x, y, color, 0, 1) or  # Check vertically
            self.check_line(x, y, color, 1, 0) or  # Check horizontally
            self.check_line(x, y, color, 1, 1) or  # Check diagonal (upper left to lower right)
            self.check_line(x, y, color, 1, -1)  # Check diagonal (upper right to lower left)
            # self.check_line(x, y, color, 0, -1) or  # Check vertically 
            # self.check_line(x, y, color, -1, 0) or  # Check horizontally
            # self.check_line(x, y, color, -1, -1) or  # Check diagonal (upper left to lower right)
            # self.check_line(x, y, color, -1, 1)    # Check diagonal (upper right to lower left)
        )

    def check_line(self, x, y, color, dx, dy):
        # You should input processed x1 and y1
        """
        Check if there's a line of 5 consecutive stones of the same color in a specific direction.
        """
        count = 0
        temp_x, temp_y = x, y

        # Check forward
        for _ in range(5):
            if 1 <= temp_x < self.list_size and 1 <= temp_y < self.list_size and self.color_list[temp_x][temp_y] == color:
                count += 1
                temp_x += dx
                temp_y += dy
            else:
                print("Forward color did not continue.")
                break
        
        # Check backward
        temp_x, temp_y = x - dx, y - dy  # Start one step back
        for _ in range(4):  # Check only up to 4 because we already counted the starting point
            if 1 <= temp_x < self.list_size and 1 <= temp_y < self.list_size and self.color_list[temp_x][temp_y] == color:
                count += 1
                if count == 5:
                    break  # Early exit if we already have 5 in a row
                temp_x -= dx
                temp_y -= dy
            else:
                print("Back wards end check.")
                break
        print("Check-line is over.")
        return count == 5   
