Chapter 03 Worksheet
 
     
     
 1. What is missing from this code? (1 pt)
     
    temperature = float(input("Temperature: ")
    if temperature > 90:
        print("It is hot outside.")
    else:
        print("It is not hot out.")
     
 2. Write a Python program that will take in a number from the user and print
    if it is positive, negative, or zero. Use a proper if/elif/else chain, don't
    just use three if statements.
                        
number = float(input("Please enter a number: "))
if number > 0:
    print("Your number is positive")
elif number < 0:
    print ("Your number is negative")
else:
    print("Your number is 0")                    
 
 3. Write a Python program that will take in a number from a user and print
    out ``Success'' if it is greater than -10 and less than 10, inclusive. (1 pt)
                       
number = float(input("Please enter a number: "))
if number >= -10 and number <= 10:
    print("Success")
else:
    print()
 
 4. This runs, but there is something wrong. What is it? (1 pt)
     
    user_input = input("A cherry is a: ")
    print("A. Dessert topping")
    print("B. Desert topping")
    if user_input.upper() == "A":
        print("Correct!")
    else:
        print("Incorrect.")
                        
# A und B müssen nochmal als Variablen definiert werden um sie effektiv zu vergleichen.
     
 5. There are two things wrong with this code that tests if x is set to a
    positive value. One prevents it from running, and the other is subtle.
    Make sure the if statement works no matter what x is set to.
    Identify both issues. (2 pts)
     
    x == 4
    if x >= 0:
        print("x is positive.")
    else:
        print("x is not positive.")
#Richtig                        
x = 4
if x > 0:
    print("x is positive.")
elif x < 0:
    print("x is not positive.")
else:
    print("x is not positive or negative.")
     
 6. What three things are wrong with the following code? (3 pts)
     
    x = input("Enter a number: ")
    if x = 3
        print("You entered 3")
                        
#Es fehlen dei Doppelpunkte
# Man muss den input noch convertieren 
#Man kann Strings und ints nicht so miteinander verbinden. Dafür muss einer Variable eingesetzt werden, damit das Programm universal ist.
     
 7. There are four things wrong with this code. Identify all four issues. (4 pts)
     
    answer = input("What is the name of Dr. Bunsen Honeydew's assistant? ")
    if a = "Beaker":
        print("Correct!")
        else
        print("Incorrect! It is Beaker.")
                        
#Richtig:
answer = input("What is the name of Dr. Bunsen Honeydew's assistant? ")
if answer == "Beaker":
    print("Correct!")
else:
    print("Incorrect! It is Beaker.")
     
 8. This program doesn't work correctly. What is wrong? (1 pt)
     
    x = input("How are you today?")
    if x == "Happy" or "Glad":
        print("That is good to hear!")
                       
#Richtig:
x = input("How are you today?")
if x == "Happy" or x == "Glad":
    print("That is good to hear!")
     
 9. Look at the code below. Write your best guess here on what it will print.
    Next, run the code and see if you are correct.
    Clearly label your guess and the actual answer.
    Also, if this or any other example results in an error, make sure to
    state that an error occurred.
    While you don't need to write an explanation, make sure you understand
    why the computer prints what it does. Don't get caught flat-footed when
    you need to know later. (2 pts)
     
    x = 5
    y = x == 6
    z = x == 5
    print("x=", x)
    print("y=", y)
    print("z=", z)
    if y:
        print("Fizz") #guess: x equals 6
    if z:
        print("Buzz") #guess: x equals 5
     
10. Look at the code below. Write you best guess on what it will print.
    Next, run the code and see if you are correct. (2 pts)
     
    x = 5
    y = 10
    z = 10
    print(x < y) # 5 < 10
    print(y < z) # 10 < 10
    print(x == 5) # 5
    print(not x == 5) #idk
    print(x != 5)
    print(not x != 5)
    print(x == "5")
    print(5 == x + 0.00000000001)
    print(x == 5 and y == 10)
    print(x == 5 and y == 5)
    print(x == 5 or y == 5)
     
11. Look at the code below. Write you best guess on what it will print.
    Next, run the code and see if you are correct. (2 pts)
     
    print("3" == "3")
    print(" 3" == "3")
    print(3 < 4)
    print(3 < 10)
    print("3" < "4")
    print("3" < "10")
    print( (2 == 2) == "True" )
    print( (2 == 2) == True )
    print(3 < "3")
     
 
12. What things are wrong with this section of code?
    The programmer wants to set the money variable according to
    the initial occupation the user selects. (1 pt)
     
    print("Welcome to Oregon Trail!")
 
    print("A. Banker")
    print("B. Carpenter")
    print("C. Farmer")
 
    user_input = input("What is your occupation? ")
 
    if user_input = A:
        money = 100
    else if user_input = B:
        money = 70
    else if user_input = C:
        money = 50
 
    print("Great! you will start the game with", money, "dollars.")

#Richtig:
user_input = input("What is your occupation? ")
            
    print("Type A for Banker")
    print("Type B for Carpenter")
    print("Type C for Farmer")
                        
if user_input == A:
    money = money + 100
elif user_input == B:
    money = money + 70
elif user_input == C:
    money = money + 50

print("Great! you will start the game with", money, "dollars.")
