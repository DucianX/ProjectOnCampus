def main():
    try: # no honor system!
        block_pattern = input("Please enter your pattern: \n")
        width = int(input("Width: "))
        height = int(input("Height: "))
        #get input for pattern, width and height.

        if len(block_pattern) != 1:
            raise ValueError("Pattern should be a single character.\n")

        # int(width)
        # int(height)
        for i in range(height): #define height, loop through height
            for j in range(width): #loop through width
                if i == 0 or i == height - 1 or j == 0 or j == width - 1:
                    print(block_pattern, end = "")
                else:
                    print(' ', end = "")
            print() #when finish one line, switch to the next one 
            #(The cursor is traversed from left to right, top to bottom. )

    
    except ValueError as e:
        print("Error:", e)

main()



