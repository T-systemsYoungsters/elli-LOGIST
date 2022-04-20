#Part 1

def dreieck(height):
    count = 1
    num = 10
    for x in range(height):
        for j in range(count):
            print(num, end=" ")
            num +=1
        count += 1
        print()

HEIGHT = int(input("Die Höhe vom Dreieck: "))
dreieck(HEIGHT)


#Part 2
def box(rows):
    print("o" * rows * 2)
    for x in range(rows-2):
        print("o" + (" " * ((rows*2) - 2)) + "o")
    print("o" * rows * 2)

SIZE = int(input("Box size: "))
box(SIZE)
print()

#Part 3

def box2(rows):
    for i in range(1, rows, 2):
        for a in range(i, rows, 2):
            print (a,end=" ")
        for b in range(i-1):
            print (" ",end=" ")
        for c in range(rows-1, i-1, -2):
            print (c,end=" ")            
        print()
        

    for i in range(rows-1, 0, -2):
        for x in range(-i, -rows, -2):
            print (-x,end=" ")
        for y in range(i-1):
            print (" ",end=" ")
        for z in range(-rows+1, -i+1, 2):
            print (-z,end=" ")
        print()
    
       

user_input = int(input("Size of a box with a box size: ")) * 2
box2(user_input)
