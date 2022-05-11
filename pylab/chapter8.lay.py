import pygame
import random
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (78,238,148)
RED = (255, 0, 0)
BLUE = (142,229,238)
YELLOW = (255,215,0)
BLUE2 = (0,0,225)
PI = 3.14159
RAIN = (79,148,205)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 600)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Ellis Animation")
 
# Create an empty array
rain_list = []
 
# Loop 50 times and add a snow flake in a random x,y position
for i in range(100):
    x = random.randrange(0, 700)
    y = random.randrange(0, 700)
    rain_list.append([x, y])
    
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLUE2)
    pygame.draw.ellipse(screen, YELLOW, [220,100,230,230])
    pygame.draw.line(screen, GREEN, [0,570],[700,570],80)
    
    
    
    
    #Bild
    
    pygame.draw.ellipse(screen, BLACK, [290,180,10,10])
    pygame.draw.ellipse(screen, BLACK, [360,180,10,10])
    pygame.draw.arc(screen, BLACK, [280,220,100,30], 0,  PI/2, 2)
    
    #Strahlen
    pygame.draw.line(screen, YELLOW, [170,100], [250,180],10)
    pygame.draw.line(screen, YELLOW, [420,280], [510,350],10)
    pygame.draw.line(screen, YELLOW, [330,330], [330,400],10)
    pygame.draw.line(screen, YELLOW, [330,30], [330,110],10)
    pygame.draw.line(screen, YELLOW, [510,100], [410,150],10)
    pygame.draw.line(screen, YELLOW, [250,250], [180,320],10)
    
    #Regen
        # Process each snow flake in the list
    for i in range(len(rain_list)):
 
        # Draw the snow flake
        pygame.draw.circle(screen, RAIN, rain_list[i], 2)
 
        # Move the snow flake down one pixel
        rain_list[i][1] += 1
 
        # If the snow flake has moved off the bottom of the screen
        if rain_list[i][1] > 700:
            # Reset it just above the top
            y = random.randrange(-50, -10)
            rain_list[i][1] = y
            # Give it a new x position
            x = random.randrange(0, 700)
            rain_list[i][0] = x
    
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
