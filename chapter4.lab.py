import random
from re import U
x = '     '

print("Welcome to Camel!")
print("You have stolen a camel to make your way across the great Mobi desert.")
print("The natives want their camel back and are chasing you down!")
print("Survive your desert trek and out run the natives.")
print(x)
print(x)

miles = 0
thirst = 0
tiredness = 0
natives = 20
canteen = 7



done = False

while not done :
    print("A. Drink from your canteen.")
    print("B. Ahead moderate speed.")
    print("C. Ahead full speed.")
    print("D. Stop for the night.")
    print("E. Status check.")
    print("Q. Quit.")
    print(x)
    
    userChoice = input("Your Choice? ")
    print(x)
    if userChoice.upper() == "Q":
        done = True
        
    elif userChoice.upper() == "A":
        if canteen > 0:
            canteen -= 1
        else:
            print("Error. You have nothing left.")
            print(x)
            
        print("Canteens left: ", canteen)   
        print(x)
         
    elif userChoice.upper() == "B":
        miles += random.randrange(5,13)
        print("Miles traveled: ", miles)
        print(x)
        thirst += 1
        tiredness = random.randrange(1,4)   
        natives += tiredness > 8 
        
    elif userChoice.upper() == "C":
        miles += random.randrange(10,21)
        print("Miles traveled: ", miles)
        print(x)
        thirst += 1
        tiredness = random.randrange(1,4)
        natives += random.randrange(7,15)
        
    elif userChoice.upper() == "D":
        print(x)
        print("The camel is happy")
        print(x)
        tiredness == 0
        natives -= random.randrange(7,15)
        
    elif userChoice.upper() == "E":
        print(x)
        print("Miles traveled: ", miles)
        print("Drinks in canteen: ", canteen)
        print(f"The natives are {natives} miles behind you.")
        print(x)
    
    
    
            
    if thirst > 4:
        print("You are thirsty")
        print(x)
    elif thirst > 6:
        print("You died of thirst!")
        print(x)
        done = True
    if tiredness > 5:
        print("Your camel is getting tired.")
        print(x)
    elif tiredness > 8 and thirst > 6:
        print("Your camel is dead.")
        done = True
    if natives == 0:
        print("The natives caught up. You are dead.")
        done = True
    elif natives < 15:
        print("The natives are getting close!")
        print(x)
    if miles > 200 and thirst < 6 and tiredness < 8 :
        print("You won!")
        done = True
        
    oasisChance = random.randrange(1,20)
    if oasisChance == 7 and done == False :
        print("You have found an oasis! You are reseting")
        print(x)
        canteen = 7
        thirst = 0
        tiredness = 0 
