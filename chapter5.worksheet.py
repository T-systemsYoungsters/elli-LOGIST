Chapter 05 Worksheet
 
     
 1. Explain how the computer coordinate system differs from the standard Cartesian
    coordinate system. There are two main differences. List both.
  - The x coordinates work the same as the Cartesian coordinates system but the y coordinates are reversed.
  - The screen covers the lower right quadrant, where the Cartesian coordinate system usually focuses on the upper right quadrant
  
 2. Before a Python Pygame program can use any functions
    like pygame.display.set_mode(), what two lines of code must occur first?
   - import pygame
   - pygame.init()

 3. Explain how WHITE = (255, 255, 255) represents a color.
   - 255 tells the monitor to display as much of the color as possible -> alle Farben zusammen ergeben weiß
  
 4. When do we use variable names for colors in all upper-case, and when do we
    use variable names for colors in all lower-case? (This applies to all variables,
    not just colors.)
  - upper-case = We don't expect the color to change; it is a constant
  - lower-case = We expect the color to change
  
 5. What does the pygame.display.set_mode() function do?
  - open a window, removes the start menu, title bars, and gives the game control of everything on the screen
  
 6. What does this for event in pygame.event.get() loop do?
   - wartet bis der User etwas macht, z.B. das Fenster zu schließen
  
 7. What is pygame.time.Clock used for?
   - Used to manage how fast the screen updates (fpm)
  
 8. For this line of code: (3 pts)
     
    pygame.draw.line(screen, GREEN, [0, 0], [100, 100], 5)
     
    * What does screen do? - deklariert die Oberfläche
    * What does [0, 0] do? - deklariert den Anfangspunkt
    * What does [100, 100] do? - deklariert den Endpunkt
    * What does 5 do? - deklariert die Breite
     
 
 9. What is the best way to repeat something over and over in a drawing?
  - To draw soething with loops and offsets
 
10. When drawing a rectangle, what happens if the specified line width is zero?
   - Das Rechteck ist aufgefüllt
  
11. Describe the ellipse drawn in the code below.
    * What is the x, y of the origin coordinate? 20, 20
    * What does the origin coordinate specify? The center of the circle? Die obere linke Ecke von einem unsichtbaren Rechteck (um der Ellipse)
    * What is the length and the width of the ellipse? 250, 100
     
    pygame.draw.ellipse(screen, BLACK, [20, 20, 250, 100], 2)
     
12. When drawing an arc, what additional information is needed over drawing
    an ellipse?
   -radians to determine what angle to draw.
    
13. Describe, in general, what are the three steps needed when printing text to
    the screen using graphics?
   - First, the program creates a variable that holds information about the font to be used, such as what typeface and how big.
   - Second, the program creates an image of the text
   - The third thing is to tell the program where this image of the text should be stamped
    
14. When drawing text, the first line of the three lines needed to draw text
    should actually be outside the main program loop. It should only run once at
    the start of the program. Why is this? You may need to ask.
   - Damit der Text einheitlich ist
  
15. What are the coordinates of the polygon that the code below draws?
   - [50,100],[0,200],[200,200],[100,50]
    pygame.draw.polygon(screen, BLACK, [[50,100],[0,200],[200,200],[100,50]], 5)
     
16. What does pygame.display.flip() do?
  - Zeigt alles was davor gezeichnet wurde
  
17. What does pygame.quit() do?
   - quits the game
  
18. Look up on-line how the pygame.draw.circle works. Get it working
    and paste a working sample here. I only need the one line of code that draws the
    circle, but make sure it is working by trying it out in a full working program.
    
    pygame.draw.circle(screen , RED ,(200,170), 80, 3)
