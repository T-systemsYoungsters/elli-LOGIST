
   # 1.Why does using this code in the main loop not work to move the rectangle?

    rect_x = 50
    pygame.draw.rect(screen, WHITE, [rect_x, 50, 50, 50])
    rect_x += 1

    A: Weil rect_x dann immer wieder auf 50 gesetzt wird und nicht hochgezählt wird trotz rect_x += 1.


   # 2.The example code to bounce a rectangle used a total of four variables. What did each variable represent?
    rect_y = definiert die x-Koordinate
    rect_x = definiert die y-Koordinate
    rect_change_y = fügt einen bestimmtgen Wert zur x-Koordinate hinzu
    rect_change_x = fügt einen bestimmtgen Wert zur x-Koordinate hinzu

   # 3.If the screen is 400 pixels tall, and the shape is 20 pixels high, at what point should the code check to see if the shape is in contact with the bottom of the screen.
    A: Bei Pixel 380, da das Rechteck von der oberen linken Ecke aus gezeichnet wird und deshalb wegen der Höhe des Rechtecks einen 20 Pixel Puffer hinzufügen muss.
    400-20=380

   # 4.Explain what is wrong with the following code (explain it, don't just correct the code):
    if rect_y > 450 or rect_y < 0:
        rect_y = rect_y * -1

    A: if rect_y > 450 or rect_y < 0:
        rect_change_y = rect_change_y * -1

    Es muss eine change Varible geben, da sonst die Variable rect_y nicht beeinfluss/ geändert werden kann und dann nicht von dem Rand wegspringt.

   # 5.A student is animating a stick figure. He creates separate variables for tracking the position of the head, torso, legs, and arms. When the figure moves to the right he adds one to each of the variables. Explain an easier way to do this that only requires one pair of x, y variables. (And no, the answer has nothing to do with a list.)
    
    A: Man braucht eine Vektor Variable


  #  6.When drawing a starry background, explain why it doesn't work to put code like this in the main program loop:
    for i in range(50):
        x = random.randrange(0, 400)
        y = random.randrange(0, 400)
        pygame.draw.circle(screen, WHITE, [x, y], 2)

    A: Durch die Schleife im main loop wird der Hintergrund immer wieder erneuert und dadurch entsteht kein Bild
    
  #  7.Explain how to animate dozens of items at the same time:

    A: Mit einer for-Schleife, die zufällige x- und y-Koodrdinaten erstellt (+ am besten in einer Liste speichern) 

   # 8.If you have a list of coordinates like the following, what code would be required to print out the array location that holds the number 33?
    stars = [[ 3,  4],
             [33, 94],
             [ 0,  0]]

    A: print(stars[1][0])
    
 #   9.This code example causes snow to fall:
    # Process each snow flake in the list
    for i in range(len(snow_list)):
     
        # Get the x and y from the list
        x = snow_list[i][0]
        y = snow_list[i][1]
     
        # Draw the snow flake
        pygame.draw.circle(screen, WHITE, [x, y], 2)
     
        # Move the snow flake down one pixel
        snow_list[i][1] += 1

    So does the example below. Explain why this example works as well.
    # Process each snow flake in the list
    for i in range(len(snow_list)):
     
        # Draw the snow flake
        pygame.draw.circle(screen, WHITE, snow_list[i], 2)
     
        # Move the snow flake down one pixel
        snow_list[i][1] += 1
A: Weil der Aufbau/ die Definition der "kleineren" Liste schon in der Liste snow_list enthalten ist.

 # 10. Take a look at the radar_sweep.py program. You can find this example under the ``graphics examples'' subsection on the examples page. The radar_sweep.py is near the end of that list. Explain how this program animates the sweep to go in a circle. 
                    """
         Show how to do a radar sweep.

         Sample Python/Pygame Programs
         Simpson College Computer Science
         http://programarcadegames.com/
         http://simpson.edu/computer-science/

        """
        // Import a library of functions called 'pygame'
        import pygame
        import math

        // Initialize the game engine
        pygame.init()
         // Colors
        BLACK = (0, 0, 0)
        WHITE = (255, 255, 255)
        GREEN = (0, 255, 0)
        RED = (255, 0, 0)
        BLUE = (0, 0, 255)

        PI = 3.141592653

        // Set the height and width of the screen
        size = [400, 400]
        screen = pygame.display.set_mode(size)

        my_clock = pygame.time.Clock()

        // Loop until the user clicks the close button.
        done = False

        angle = 0

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True

            # Set the screen background
            screen.fill(WHITE)

            # Dimensions of radar sweep
            # Start with the top left at 20,20
            # Width/height of 250
            box_dimensions = [20, 20, 250, 250]

            # Draw the outline of a circle to 'sweep' the line around
            pygame.draw.ellipse(screen, GREEN, box_dimensions, 2)

            # Draw a black box around the circle
            pygame.draw.rect(screen, BLACK, box_dimensions, 2)

            # Calculate the x,y for the end point of our 'sweep' based on
            # the current angle
            x = 125 * math.sin(angle) + 145
            y = 125 * math.cos(angle) + 145

            # Draw the line from the center at 145, 145 to the calculated
            # end spot
            pygame.draw.line(screen, GREEN, [145, 145], [x, y], 2)

            # Increase the angle by 0.03 radians
            angle = angle + .03

            # If we have done a full sweep, reset the angle to 0
            if angle > 2 * PI:
                angle = angle - 2 * PI

            # Flip the display, wait out the clock tick
            pygame.display.flip()
            my_clock.tick(60)

        // Be IDLE friendly. If you forget this line, the program will 'hang'
        // on exit.
        pygame.quit()

A: Durch die mathematische Rechnung für x und y ergeben sich neue Koordinaten, die beim Erzeugen der Linie eingesetzt werden. Der Anfang der Line bilden die Koordinaten [145, 145] und das Ende das Ergebnis von den mathematischen Rechnungen bei x und y. Durch die ständig neuen Ergebnisse, sieht es so aus als würde die Linie im Kreis geleiten. 
