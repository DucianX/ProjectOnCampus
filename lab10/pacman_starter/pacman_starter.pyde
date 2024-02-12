WIDTH = 500
HEIGHT = 500
PACMAN_HEIGHT = 100
PACMAN_WIDTH = 100
SPEED = 3
x = WIDTH/2
y = HEIGHT/2
x_add = 0
y_add = 0
PIE_2 = 360
PIE_0375 = 135
PIE_0125 = 45
PIE_075 = 270
PIE_0625 = 225
PIE_0875 = 315
a = 45
mouth_speed = 3 # need to be the factor of a.
flag = "close"
towards = "right"

def setup():
    size(WIDTH, HEIGHT)
    colorMode(RGB, 1)
    fill(1.0, 1.0, 0.0)
    noStroke()

def draw():
    global x, y, a, flag  # Must be declared as global

    if flag == "close":
        a -= mouth_speed
        if a == 0: flag = "open"
    if flag == "open":
        a += mouth_speed
        if a == 45: flag = "close"
    
    background(0)

    x = x + x_add
    y = y + y_add
    
    # The following cases deal with when PacMan
    # is near the edge of the screen
    
    # If PacMan moves completely behond the right edge
    # Now we stop drawing another pacman. draw() is executed framely!
    if (x > WIDTH + (PACMAN_WIDTH/2)):
        # Reset the x value to the left side
        x = PACMAN_WIDTH/2
    # If PacMan is overlapping the right edge
    elif (x > WIDTH - (PACMAN_WIDTH/2)):
        # draw a second PacMan on the left side, also
        # overlapping
        pacman(x - WIDTH, y)
    
    # If PacMan moves past the bottom edge, 
    # redraw at the top
    if (y > HEIGHT + (PACMAN_HEIGHT/2)):
        y = PACMAN_HEIGHT/2
    elif (y > HEIGHT - (PACMAN_HEIGHT/2)):
        pacman(x, y - HEIGHT)
        
    # If PacMan moves past the left edge, 
    # redraw at the right   
    if (x < -(PACMAN_WIDTH/2)): 
        x = WIDTH - (PACMAN_WIDTH/2)
    elif (x < PACMAN_WIDTH/2):
        pacman(x + WIDTH, y)
    
    # If PacMan moves past the top, redraw at bottom
    if (y < -(PACMAN_HEIGHT/2)):
        y = HEIGHT - (PACMAN_HEIGHT/2)
    elif (y < PACMAN_HEIGHT/2):
        pacman(x, y + HEIGHT)
    
    # Always draw PacMan at his real current location.
    pacman(x, y)

def pacman(x, y):
    """Draw PacMan to the screen"""
    # Use global variables as necessary
    global pie_2
    if towards == "right":
        arc(x, y, PACMAN_WIDTH, PACMAN_HEIGHT, 
            radians(a), 
            radians(PIE_2 - a))
    elif towards == "down":
        arc(x, y, PACMAN_WIDTH, PACMAN_HEIGHT, 
            radians(PIE_0375 - a), 
            radians(PIE_2 + PIE_0125 + a))
    elif towards == "up":
        arc(x, y, PACMAN_WIDTH, PACMAN_HEIGHT, 
            radians(PIE_0875 - a), 
            radians(PIE_2 + PIE_0625 + a))
    elif towards == "left":
        arc(x, y, PACMAN_WIDTH, PACMAN_HEIGHT, 
            radians(PIE_0625 - a), 
            radians(PIE_2 + PIE_0375 + a))
        
        
def keyPressed():
    global x_add, y_add, towards  # Must be declared as global
    if (key == CODED):
        if (keyCode == DOWN):
            x_add = 0
            y_add = SPEED
            towards = "down"
        elif (keyCode == UP):
            x_add = 0
            y_add = -(SPEED)
            towards = "up"
        elif (keyCode == LEFT):
            x_add = -(SPEED)
            y_add = 0
            towards = "left"
        elif (keyCode == RIGHT):
            x_add = SPEED
            y_add = 0 
            towards = "right"
