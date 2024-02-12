class AI:
    WINNING_COUNT = 5
    PRIORITY_COUNT = 4

    def __init__(self, board1):
        self.board = board1
        self.have_at_least_one_white = False

    def potential_block(self, x, y, board):
            # To handle 3+1 and 4+1 Case secondly
            print("Potential block invoked.\n")
            x = int(x)
            y = int(y)
            def horizontal_case(x, y):
                # Horizontal Case
                for i in range(1, 4):
                    if (x + i + 1) <= 15 and (x - i - 1) >= 1:
                        if(self.board.board_list[x + (i + 1)][y] and not
                        self.board.board_list[x + i][y]):
                            return (x + i, y)
                        if(self.board.board_list[x - (i + 1)][y] and not
                        self.board.board_list[x - i][y]):
                            return (x - i, y)

            def vertical_case(x, y):
                # Vertical Case
                # To handle 3+1 and 4+1 Case
                for i in range(1, 4):
                    if (y + i + 1) <= 15 and (y - i - 1) >= 1:
                        if(self.board.board_list[x][y + (i + 1)] and not
                        self.board.board_list[x][y + i]):
                            return (x, y + i)
                        if(self.board.board_list[x][y - (i + 1)] and not
                        self.board.board_list[x][y - i]):
                            return (x, y - i)

            def ullr_case(x, y):
                # Upperleft-Lowerright Case
                # To handle 3+1 and 4+1 Case
                for i in range(1, 4):
                        if((x + i + 1 <= 15) and (y + i + 1 <= 15) and self.board.board_list[x + (i + 1)][y + (i + 1)] and not
                        self.board.board_list[x + i][y + i]):
                            return (x + i, y + i)
                        if((x - i - 1 >= 1) and (y - i - 1 >= 1) and self.board.board_list[x - (i + 1)][y - (i + 1)] and not
                        self.board.board_list[x - i][y - i] and (x - i - 1 >= 1) and (y - i - 1 >= 1)):
                            return (x - i, y - i)
            
            def urll_case(x, y):
                # Upperright-Lowerleft Case
                # To handle 3+1 and 4+1 Case
                for i in range(1, 4):
                        if((x + i + 1 <= 15) and (y - (i + 1) >= 1) and self.board.board_list[x + (i + 1)][y - (i + 1)] and not
                        self.board.board_list[x + i][y - i]):
                            return (x + i, y - i)
                        if((x - (i + 1) >= 1) and (y + i + 1 <= 15) and self.board.board_list[x - (i + 1)][y + (i + 1)] and not
                        self.board.board_list[x - i][y + i] and (x - (i + 1) >= 1) and (y + i + 1 <= 15)):
                            return (x - i, y + i)
            return horizontal_case(x, y) or vertical_case(x, y) or ullr_case(x, y) or urll_case(x, y)

    def find_move_combo_based(self, x, y, board):
        # We are passing in the AI's last move
        # This function means that if AI have own stones aligned, from 2 to 3, they gonna add one to it.
        print("find_move_combo_based invoked")        
        for COMBO_NUMBER in range (3, 1, -1):
            # To make sure it is the combo of whites
            if board.detect_combo(x, y, COMBO_NUMBER) and board.color_list[x][y] == "White":
                if board.check_horizontal(x, y, COMBO_NUMBER):
                    if not self.board.board_list[x + 1][y]:
                        return(x + 1, y)
                    if not self.board.board_list[x - 1][y]:
                        return(x - 1, y)
                if board.check_vertical(x, y, COMBO_NUMBER):
                    if not self.board.board_list[x][y + 1]:
                        return(x, y + 1)
                    if not self.board.board_list[x][y - 1]:
                        return(x, y - 1)
                if board.check_upperleft_lowerright(x, y, COMBO_NUMBER):
                    if not self.board.board_list[x + 1][y + 1]:
                        return(x + 1, y + 1)
                    if not self.board.board_list[x - 1][y - 1]:
                        return(x - 1, y - 1)
                if board.check_upperright_lowerleft(x, y, COMBO_NUMBER):
                    if not self.board.board_list[x - 1][y + 1]:
                        return(x - 1, y + 1)
                    if not self.board.board_list[x + 1][y - 1]:
                        return(x + 1, y - 1)
                else:
                    print("Couldnt find any white combo")
                    return None

    def find_blocking_move(self, board, x1, y1, ai_has_moved, xa1, ya1):
        """Check if the opponent has a winning move and return the blocking move"""
        x = x1
        y = y1
        xa = xa1
        ya = ya1
        # Because (x1, y1) is made by player, so it must be a black, causing colorOfStone unneeded.
        # Case of 3 stones are horizontal aligned
        # And they must be place continuely to be detected
        print("find blocking move invoked.\n")

        # Blocking 3-combo is the priority.
        def combo_3(x, y):
            # To handle the 3-combo situation of player first
            if self.board.check_horizontal(x, y, 3):
                print("Detected horizontal aligners")
                for i in range(1, 3):
                    # Handled FILL_IN_MIDDLE case and continuous case.
                    if (x + i <= 15) and not self.board.board_list[x + i][y]:
                        return (x + i, y)
                    # if one end of aligners is dead then try other end
                    # This handles from right to left placement, continuously.
                    elif (x - i >= 1) and not self.board.board_list[x - i][y]:
                        return (x - i, y)
            elif self.board.check_vertical(x, y, 3):
                print("Detected vertical aligners")
                for i in range(1, 3):
                    if (y + i <= 15) and not self.board.board_list[x][y + i]:
                        return (x, y + i)
                    # if one end of aligners is dead then try other end
                    # This handles from right to left placement, continuously.
                    elif (y - i >= 1) and not self.board.board_list[x][y - i]:
                        return (x, y - i)
            elif self.board.check_upperleft_lowerright(x, y, 3):
                for i in range(1, 3):
                    if (x + i <= 15) and (y + i <= 15) and not self.board.board_list[x + i][y + i]:
                        return (x + i, y + i)
                    # if one end of aligners is dead then try other end
                    # This handles from right to left placement, continuously.
                    elif (x - i >= 1) and (y - i >= 1) and not self.board.board_list[x - i][y - i]:
                        return (x - i, y - i)
            elif self.board.check_upperright_lowerleft(x, y, 3):
                for i in range(1, 3):
                    if (x + i <= 15) and (y - i >= 1) and not self.board.board_list[x + i][y - i]:
                        return (x + i, y - i)
                    # if one end of aligners is dead then try other end
                    # This handles from right to left placement, continuously.
                    elif (x - i >= 1) and (y + i <= 15) and not self.board.board_list[x - i][y + i]:
                        return (x - i, y + i)
            else:
                print("Did not find any combo in combo_3.\n")
                return 

        # TODO: Let combo-3 override 2+1 or 3+1 blocking move.
        # do block 3-combo of player first.
        if combo_3(x, y):
            print("COMBO-3")
            return combo_3(x, y)
        # But if ai reach 3, ai should continue its stone instead of take potential_block.
        # AI must move at least once to get us the xa and ya.
        elif ai_has_moved:
            if self.potential_block(x, y, board):
                return self.potential_block(x, y, board)
            print("Will return find move combo based, xa,ya =" + str(xa) + str(ya))
            if self.find_move_combo_based(xa, ya, board):
                return self.find_move_combo_based(xa, ya, board)


    def win_move(self, x, y, board):
        # We are passing in the AI's last move
        # This function means that if AI have own stones aligned, from 2 to 3, they gonna add one to it.
        print("Win_move invoked")
        print("x, y =" + str(x) + " " + str(y) + "\n")
        for COMBO_NUMBER in range(3, 5):
            # When combo 3 and 4, AI sticks to it
            if board.detect_combo(x, y, COMBO_NUMBER) and board.color_list[x][y] == "White":
                print("find_move_combo_based invoked")
                if board.check_horizontal(x, y, COMBO_NUMBER):
                    if (x+1<=15) and not self.board.board_list[x + 1][y]:
                        return(x + 1, y)
                    elif (x-1>=1) and not self.board.board_list[x - 1][y]:
                        return(x - 1, y)
                    elif (x-4>=1) and not self.board.board_list[x - 4][y]:
                        return(x - 4, y)
                    elif (x+4<=15) and not self.board.board_list[x + 4][y]:
                        return(x + 4, y)
                    else:
                        continue
                elif board.check_vertical(x, y, COMBO_NUMBER):
                    if (y+1<=15) and not self.board.board_list[x][y + 1]:
                        return(x, y + 1)
                    elif (y+4<=15) and not self.board.board_list[x][y + 4]:
                        return(x, y + 4)
                    elif (y-1>=1) and not self.board.board_list[x][y - 1]:
                        return(x, y - 1)
                    elif (y-4>=1) and not self.board.board_list[x][y - 4]:
                        return(x, y - 4)
                    else:
                        continue
                elif board.check_upperleft_lowerright(x, y, COMBO_NUMBER):
                    if (x+1<=15) and (y+1<=15) and not self.board.board_list[x + 1][y + 1]:
                        return(x + 1, y + 1)
                    elif (x+4<=15) and (y+4<=15) and not self.board.board_list[x + 4][y + 4]:
                        return(x + 4, y + 4)
                    elif (x-1>=1) and (y-1>=1) and not self.board.board_list[x - 1][y - 1]:
                        return(x - 1, y - 1)
                    elif (x-4>=1) and (y-4>=1) and not self.board.board_list[x - 4][y - 4]:
                        return(x - 4, y - 4)
                    else:
                        continue
                elif board.check_upperright_lowerleft(x, y, COMBO_NUMBER):
                    if (x-1>=1) and (y+1<=15) and not self.board.board_list[x - 1][y + 1]:
                        return(x - 1, y + 1)
                    elif (x-4>=0) and (y+4<=15) and not self.board.board_list[x - 4][y + 4]:
                        return(x - 4, y + 4)
                    elif (x+1<=15) and (y-1>=1) and not self.board.board_list[x + 1][y - 1]:
                        return(x + 1, y - 1)
                    elif (x+4<=15) and (y-4>=1) and not self.board.board_list[x + 4][y - 4]:
                        return(x + 4, y - 4)
                    else:
                        continue
                else:
                    print("Different stones aligned. Check white failed.Couldnt find any white combo\n\n")
                    return False
            else:
                print("detect combo failed.Couldnt find any combo in white.")
                return False
        
    def follow_move(self, x, y):
        # Base case. Just stick with player!
        print("Follow move function invoked.\n")
        self.have_at_least_one_white = True
        if (x + 1 <= 15) and not self.board.board_list[x + 1][y]:
            print("Stick to the right")
            return([x + 1, y])
        elif (x - 1 >= 1) and not self.board.board_list[x - 1][y]:
            return(x - 1, y)
            print("Stick to the left")
        elif (y + 1 <= 15) and not self.board.board_list[x][y + 1]:
            print("Stick to upper")
            return(x, y + 1)
        elif (y - 1 >= 1) and not self.board.board_list[x][y - 1]:
            print("Stick to the lower")
            return(x, y - 1)
        elif (x + 1 <= 15) and (y + 1 <= 15) and not self.board.board_list[x + 1][y + 1]:
            print("Stick to the lower right")
            return(x + 1, y + 1)
        elif (x - 1 >= 1) and (y - 1 >= 1) and not self.board.board_list[x - 1][y - 1]:
            print("Stick to the upper left")
            return(x - 1, y - 1)
        elif (x - 1 >= 15) and (y + 1 <= 15) and not self.board.board_list[x - 1][y + 1]:
            print("Stick to the lower left")
            return(x - 1, y + 1)
        elif (x + 1 <= 15) and (y - 1 >= 1) and not self.board.board_list[x + 1][y - 1]:
            print("Stick to the upper right")
            return(x + 1, y - 1)
        else:
            print("Follow move failed.")
            return False
        # To follow player's move when upper function has not met the execution condition

    def find_best_move(self, x, y, xa, ya, board): 
        # Find the best move by checking adjacent positions to the player's pieces
        # Return the move (x, y) if found, else return a random move or None
        # WINNING_COUNT for 4 steps, PRIORITY for 3.
        if self.have_at_least_one_white:
            return self.find_move_combo_based(xa, ya, board)
        else:
            return self.follow_move(x, y)
        


