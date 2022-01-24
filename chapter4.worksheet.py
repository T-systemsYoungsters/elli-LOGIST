Chapter 04 Worksheet
 
     
    Reminder: Please use full sentences, capital letters, and proper grammar
    where appropriate.
    Don't create a loop that only loops once. That doesn't make sense.
    Python runs the code once by default anyway. Avoid loops like this:
     
    for i in range(1):
        # Do something.
     
     
 1. Write a Python program that will use a for loop to print your name
    10 times, and then the word ``Done'' at the end.
 
    for i in range(1,11):
       print("Elli")
    print("Done")
    
 2. Write a Python program that will use a for loop to print ``Red''
    and then ``Gold'' 20 times. (Red Gold Red Gold Red Gold... all on separate lines.
    Don't use \n.)
                                 
    for i in range(1,21):
        print("Red")
        for i in range(1):
           print("Gold")
                                 
 3. Write a Python program that will use a for loop to print the even
    numbers from 2 to 100, inclusive.
   
     for i in range(1,101,2):
         print(i +1)
                                 
 4. Write a Python program that will use a while loop to count from
    10 down to, and including, 0. Then print the words ``Blast off!'' Remember, use
    a WHILE loop, don't use a FOR loop.
    i = 10
    while i < -1:
       print(i)
       i = i - 1
                                 
 5. There are three things wrong with this program. List each. (3 pts)
     
    print("This program takes three numbers and returns the sum.")
    total = 0
    for i in range(3):
        x = input("Enter a number: ") #Der Input muss noch nach int konvertiert werden
        total = total + i #1. Da muss x statt i stehen, da es sonst nicht die userNummer zusammen zählt
    print("The total is:", x) # Da muss statt x total stehen, da sonst die zuletzt eingegebene Zahl augegeben wird
                                 
     
 6. Write a program that prints a random integer from 1 to 10 (inclusive).
                                 
    import random
    my_number = random.randrange(1,11)
    print(my_number)
                                 
 7. Write a program that prints a random floating point number somewhere between
    1 and 10 (inclusive). Do not make the mistake of generating a random number from
    0 to 10 instead of 1 to 10.
 
     import random
     my_number = random.random() * 11 + 1
     print(my_number)                            
                                 
 8. Write a Python program that will: (3 pts)
     
    * Ask the user for seven numbers
    * Print the total sum of the numbers
    * Print the count of the positive entries, the number entries equal to zero,
    and the number of negative entries. Use an if, elif, else chain, not just three
    if statements.

total = 0  
positiveTotal = 0
negativeTotal = 0
zeroTotal = 0

for i in range(7):
    x = int(input("Enter a number: "))
    total = total + x
    if x > 0:
        positiveTotal += 1
    elif x < 0:
        negativeTotal += 1
    elif x == 0:
        zeroTotal += 1
    
    
print("The total is:", total) 
print("The total of positive numbers: ", positiveTotal)
print("The total of negative numbers: ", negativeTotal)
print("The total of zeros: ", zeroTotal)
     
 9. Coin flip tosser: (4 pts)
     
    * Create a program that will print a random 0 or 1.
    * Instead of 0 or 1, print heads or tails. Do this
    using if statements. Don't select from a list, as shown in the chapter.
    * Add a loop so that the program does this 50 times.
    * Create a running total for the number of heads flipped, and the number of tails.
     
 import random

coinHead = 0
coinTails = 0

for i in range(50):
    coinNumber = random.randrange(0,2)
    if coinNumber == 0:
        print("heads")
        coinHead += 1
    else:
        print("tails")
        coinTails += 1
        
        
print("Total amount of head: ", coinHead)
print("Total amount of tail: ", coinTails)
                                 
10. Write a program that plays rock, paper, scissors: (4 pts)
     
    * Create a program that randomly prints 0, 1, or 2.
    * Expand the program so it randomly prints rock, paper, or scissors
    using if statements. Don't select from a list, as shown in the chapter.
    * Add to the program so it first asks the user their choice.
    * (It will be easier if you have them enter 1, 2, or 3.)
    * Add conditional statement to figure out who wins.
                                 
import random

pcPick = random.randrange(2)
userPick = 0
print("ROCK, PAPER, SCISSORS GAME!!")
print("You are going to play againt the computer.")
print("For simplicity please enter 0 for rock, 1 for paper and 2 for scissors")


userPick = int(input("Enter your choice: "))
print("Computers choice: ", pcPick)

if pcPick == userPick:
    print("It is a tie. Play again.")
elif userPick == 0:
    if pcPick == 2:
        print("Rock smashes scissors! You win!")    
    else:
        print("Paper covers rock! You lose.")
elif userPick == 1:
    if pcPick == 0:
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif userPick == 2:
    if pcPick == 1:
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")
