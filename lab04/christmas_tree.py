def main():
    while True:
        try:
            base_width = int(input("base width: "))
            if base_width < 3 or base_width % 2 != 1:
                print("Please enter an odd number greater than or equal to 3.")
                continue  # Restart the loop to ask for input again
                            # !!!the continue statement in Python finds and applies to the nearest enclosing loop. 
            
            height = (base_width + 1) // 2
            
            for i in range(height):
                if i == 0:
                    top_spaces = ' ' * (height - i - 1) #CAUTION! i starts from ZERO!
                    print(top_spaces + '*' + top_spaces) # Top of the tree
                elif i > 0 and i < height - 1:
                    lr_spaces = height - 1 - i
                    middle_spaces = ' ' * (i * 2 - 1)
                    print(lr_spaces * ' ' + '/' + middle_spaces + '\\')                    
                elif i == height - 1:
                    print('/' + '_' * (base_width - 2) + '\\') #note the way '+' works


            break #When drew a whole tree
        
        except ValueError:
            print("Invalid input. Type in an odd number.") 

main()
             
            