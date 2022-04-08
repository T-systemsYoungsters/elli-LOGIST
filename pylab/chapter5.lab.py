import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (162,205,90)
RED = (255, 0, 0)
BROWN = (205,133,63)
BLUE = (191,239,255)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Katze")
 
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
    screen.fill(BLUE)
 
    # --- Drawing code should go here
    # (x , y, width, lenght)
    pygame.draw.rect(screen, GREEN, [0, 420, 700, 100], 0)
    
    pygame.draw.rect(screen, BROWN, [130, 300, 40, 150], 0)
    pygame.draw.ellipse(screen, BROWN, [130, 410, 80, 40], 0)
    
    pygame.draw.rect(screen, BROWN, [200, 300, 40, 150], 0)
    pygame.draw.ellipse(screen, BROWN, [200, 410, 80, 40], 0)
    
    pygame.draw.rect(screen, BROWN, [300, 300, 40, 150], 0)
    pygame.draw.ellipse(screen, BROWN, [300, 410, 80, 40], 0)
    
    pygame.draw.rect(screen, BROWN, [370, 300, 40, 150], 0)
    pygame.draw.ellipse(screen, BROWN, [370, 410, 80, 40], 0)
    
    pygame.draw.ellipse(screen, BROWN, [100, 180, 360, 160], 0)
    
    pygame.draw.circle(screen, BROWN,(470,170), 80)
    
    pygame.draw.polygon(screen, BROWN, [[440,50], [460,110], [425,110]], 0)
    pygame.draw.polygon(screen, BROWN, [[490,50], [510,110], [475,110]], 0)
    
    pygame.draw.circle(screen, BLACK,(450,150), 5)
    pygame.draw.circle(screen, BLACK,(500,150), 5)
    
    pygame.draw.circle(screen, BLACK,(475,180), 5)
    
    pygame.draw.line(screen, BLACK, [475, 180], [475, 200], 3)
    
    pygame.draw.line(screen, BROWN, [40, 180], [200, 250], 8)
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
