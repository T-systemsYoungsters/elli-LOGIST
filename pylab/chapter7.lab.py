#variable
room_list = []
current_room = 0
#10.
done = False

#game
room = ["You are in the Bedroom 2.\nThere is a passage to the north and east",3 , 1 , None, None ]
room_list.append(room)
room = ["You are in the South Hall.\nThere is a passage to the west, north and east", 4, 2, None, 0]
room_list.append(room)
room = ["You are in the Dining Room.\nThere is a passage to the west and north", 5, None, None, 1]
room_list.append(room)
room = ["You are in the Kitchen.\nThere is a passage to the west and south", None, None, 2, 1]
room_list.append(room)
room = ["You are in the North Hall.\nThere is a passage to the west, east, south and north", 6, 5, 1, 3]
room_list.append(room)
room = ["You are in the Bedroom 1.\nThere is a passage to the east and south", None, 4, 0, None]
room_list.append(room)
room = ["You are at the Balcony.\nThere is a passage to the south", None, None, 4, None]
room_list.append(room)

while done != True:
    print()
    # Aufgabe 7.
    print (room_list[current_room][0])
    print()

    
    #12.
    user_choice = input("Which direction? ")
    
    
    # USER CHOICES
    
    #14. North
    if user_choice.upper() == 'NORTH' or user_choice.upper() == 'N':
        next_room = room_list[current_room][1]
    
     #15. None   
        if next_room == None:
                print()
                print("You can't go that way")
        else:
            current_room = next_room
        
    #East
    elif user_choice.upper() == 'EAST' or user_choice.upper() == 'E':
        next_room = room_list[current_room][2]

        if next_room == None:
            print()
            print("You can't go that way")
        else:
            current_room = next_room
        
    #South
    elif user_choice.upper() == 'SOUTH' or user_choice.upper() == 'S':
        next_room = room_list[current_room][3]

        if next_room == None:
            print()
            print("You can't go that way")
        else:
            current_room = next_room

    #West
    elif user_choice.upper() == 'WEST' or user_choice.upper() == 'W':
        next_room = room_list[current_room][4]

        if next_room == None:
            print()
            print("You can't go that way")
        else:
            current_room = next_room
    #invalid intake
    else: 
        print("Invalid Input! Please try again.")
            
 # quit command
    if user_choice.upper() == 'QUIT' or user_choice.upper() == 'Q':
        print()
        print("You quit the game.")
        done = True  