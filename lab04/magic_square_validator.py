NUM_LINE = 3
# Define NUM_LINE as a global constant, otherwise it will be availble only in main()
    
def main():
    line = []
    for i in range (NUM_LINE):
        row = input("Plz input three numbers.")
        if len(row) != 3:
            print("Invalid input. Plz enter three numbers.")
            return
        row = [int(char) for char in row]
        line.append(row)
        # make chars ints, and append them to the line.

    if is_magic_square(line):
        print("This is a magic square!")
    else:
        print("Not a magic square!")

def is_magic_square(line):
    # check the sum of rows
    for row in line:
        if sum(row) != 15:
            return False
    
    # check the sum of columns
    for col in range(len(line)):
       if  sum(line[row][col] for row in range(len(line)))!= 15:
            return False
       
    # check the sum of diagonals
    if sum(line[i][i] for i in range(len(line))) != 15 or sum(line[i][len(line) - 1 - i] for i in range(len(line))) != 15:
        return False
    
    return True

main()