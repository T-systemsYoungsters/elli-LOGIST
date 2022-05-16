Chapter 09 Worksheet
 
     
    For the code below, write a prediction on what it will output. Then run
    the code and state if your prediction was accurate or not. If your prediction
    is incorrect, make sure you understand why.
 
    If you don't know why the code runs the way it does, watch the video at the
    end of the assignment for an explanation. If you are looking at the text-only
    version of this worksheet, go on-line and find the HTML version of this worksheet
    for the video.
 
    This section is worth 10 points, a half point per problem rounded up.

 1. Block 1 (Remember, guess AND actual. You'll lose 19 points if you skip
    guessing the output of the next 19 problems, and completely miss the point
    of this part.)
     
    for i in range(5):
        print(i + 1)

GUESS:1
2
3
4
5

ACTUAL:1
2
3
4
5
     
 2. Block 2
     
    for i in range(5):
        print(i)
        i = i + 1
GUESS:1
2
3
4
5

ACTUAL: 0
1
2
3
4
 3. Block 3
     
    x = 0
    for i in range(5):
        x += 1
    print(x)
GUESS:5

ACTUAL: 5

 4. Block 4
     
    x = 0
    for i in range(5):
        for j in range(5):
            x += 1
    print(x)
GUESS:25

ACTUAL:25 
 5. Block 5
     
    for i in range(5):
        for j in range(5):
            print(i, j)
GUESS&ACTUAL:
0 0
0 1
0 2
0 3
0 4
1 0
1 1
1 2
1 3
1 4
2 0
2 1
2 2
2 3
2 4
3 0
3 1
3 2
3 3
3 4
4 0
4 1
4 2
4 3
4 4
     
 6. Block 6
     
    for i in range(5):
        for j in range(5):
            print("*", end="")
            print()
GUESS:
*
**
***
****
*****

ACTUAL: 
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*

 7. Block 7
     
    for i in range(5):
        for j in range(5):
            print("*", end="")
        print()

GUESS&ACTUAL:
*****
*****
*****
*****
*****     

 8. Block 8
     
    for i in range(5):
        for j in range(5):
            print("*", end="")
    print()
GUESS&ACTUAL:  
*************************   
 9. Block 9
     
    # This is supposed to sum a list of numbers
    # What is the mistake here?
    my_list = [5, 8, 10, 4, 5]
    i = 0
    for i in my_list:
        i = i + my_list[i]
    print(i)
GUESS&ACTUAL: Der Fehler liegt bei i = i + my_list[i], da man kein Ekement i aus der Liste gehmen kann. Normalerweise sollte nur i stehen.   
10. Block 10
     
    for i in range(5):
        x = 0
        for j in range(5):
            x += 1
    print(x)
GUESS:5

ACTUAL:5     
11. Block 11
     
    import random
    play_again = "y"
    while play_again == "y":
        for i in range(5):
            print(random.randrange(2), end="")
        print()
        play_again = input("Play again? ")
    print("Bye!")
GUESS&ACTUAL:   
11010 (Fünf versch. Zahlen zwischen 0 und 1 )
Play again?  

12. Block 12
     
    def f1(x):
        print(x)
    y = 3
    f1(y)
GUESS&ACTUAL:   3

13. Block 13
     
        def f2(x):
            x = x + 1
            print(x)
        y = 3
        f2(y)
        print(y)
GUESS&ACTUAL:   
4
3
   
14. Block 14
     
    def f3(x):
        x = x + 1
        print(x)
    x = 3
    f3(x)
    print(x)
GUESS&ACTUAL:   
4
3    
15. Block 15
     
    def f4(x):
        z = x + 1
        print(z)
    x = 3
    f4(x)
    print(z)
GUESS&ACTUAL:   
NameError: name 'z' is not defined

16. Block 16
     
    def foo(x):
        x = x + 1
        print("x=", x)
 
    x = 10
    print("x=", x)
    foo(x)
    print("x=", x)
GUESS&ACTUAL: 
x= 10
x= 11
x= 10
    
17. Block 17
     
    def f():
        print("f start")
        g()
        h()
        print("f end")
 
    def g():
        print("g start")
        h()
        print("g end")
 
    def h():
        print("h")
 
    f()
GUESS&ACTUAL: 
f start
g start
h
g end
h
f end

18. Block 18
     
    def foo():
        x = 3
        print("foo has been called")
 
    x = 10
    print("x=", x)
    foo()
    print("x=", x)
GUESS&ACTUAL:  
x= 10
foo has been called
x= 10   
19. Block 19 (This demonstrates a new concept that won't be fully explained until Chapter 12.)
     
    def a(x):
        print("a", x)
        x = x + 1
        print("a", x)
 
    x = 1
    print("main", x)
    a(x)
    print("main", x)
 
    def b(y):
        print("b", y[1])
        y[1] = y[1] + 1
        print("b", y[1])
 
    y=[123, 5]
    print("main", y[1])
    b(y)
    print("main", y[1])
 
    def c(y):
        print("c", y[1])
        y = [101, 102]
        print("c", y[1])
 
    y = [123, 5]
    print("main", y[1])
    c(y)
    print("main", y[1])
GUESS:?

ACTUAL:     
main 1
a 1
a 2
main 1
main 5
b 5
b 6
main 6
main 5
c 5
c 102
main 5
 
     
 
     
 
    This next section involves finding the mistakes in the code. If you can't
    find the mistake, check out the video at the end for the answer and an explanation
    on what is wrong.
 
    This section is worth 7 points.
     
20. Correct the following code: (Don't let it print out the word ``None'')
     
    def sum(a, b, c):
        print(a + b + c)
 
    print(sum(10, 11, 12))
     

A: 
def sum(a, b, c):
        print(a + b + c)
 
sum(10, 11, 12)

21. Correct the following code: (x should increase by one, but it doesn't.)
     
    def increase(x):
        return x + 1
 
    x = 10
    print("X is", x, " I will now increase x." )
    increase(x)
    print("X is now", x)

A:
def increase(x):
    return x + 1

x = 10
print("X is", x, " I will now increase x." )
x = increase(x)
print("X is now", x)

22. Correct the following code:
     
    def print_hello:
        print("Hello")
 
    print_hello()
     
A:
def print_hello():
    print("Hello")
 
print_hello()

23. Correct the following code:
     
    def count_to_ten():
        for i in range[10]:
            print(i)
 
    count_to_ten()

A:
def count_to_ten():
     for i in range(1,11):
        print(i)
 
count_to_ten()

24. Correct the following code:
     
    def sum_list(list):
        for i in list:
            sum = i
            return sum
 
    list = [45, 2, 10, -5, 100]
    print(sum_list(list))
A:
def sum_list(list):
    sum = 0
    for i in range(len(list)):
        sum = sum + list[i]
    return sum
 
list = [45, 2, 10, -5, 100]
print(sum_list(list))

25. Correct the following code: (This almost reverses the string. What is wrong?)
     
    def reverse(text):
        result = ""
        text_length = len(text)
        for i in range(text_length):
            result = result + text[i * -1]
        return result
 
    text = "Programming is the coolest thing ever."
    print(reverse(text))

A:
def reverse(text):
    result = ""
    text_length = len(text)
    for i in range(text_length):
        result = result + text[text_length -1 -i]
    return result
 
text = "Programming is the coolest thing ever."
print(reverse(text))

26. Correct the following code:
     
    def get_user_choice():
        while True:
            command = input("Command: ")
            if command = f or command = m or command = s or command = d or command = q:
                return command
 
            print("Hey, that's not a command. Here are your options:" )
            print("f - Full speed ahead")
            print("m - Moderate speed")
            print("s - Status")
            print("d - Drink")
            print("q - Quit")
 
    user_command = get_user_choice()
    print("You entered:", user_command)
     
A:
def get_user_choice():
    while True:
        command = input("Command: ")
        if command == "f" or command == "m" or command == "s" or command == "d" or command == "q":
            return command
 
        print("Hey, that's not a command. Here are your options:" )
        print("f - Full speed ahead")
        print("m - Moderate speed")
        print("s - Status")
        print("d - Drink")
        print("q - Quit")
 
user_command = get_user_choice()
print("You entered:", user_command)     
 
     
 
    (13 pts) For this section, write code that satisfies the following items:
     
27. Write a function that prints out ``Hello World.''
 def print_hello():
    print("Hello World")
 
28. Write code that will call the function in the prior problem.
 def print_hello():
    print("Hello World")
 
print_hello()

29. Write a function that prints out ``Hello Bob'', and will take a parameter to
    let the caller specify the name. Do not put an input statement inside
    the function! Use a parameter.
def print_name(x):
    print("Hello ", x)

30. Write code that will call the function in the prior problem.
print_name("Bob")

31. Write a function that will take two numbers as parameters (not as input from
    the user) and print their product (i.e. multiply them).
def sum(x,y):
        print(x*y)
   

32. Write code that will call the prior function.
sum(4,4) 

33. Write a function that takes in two parameters. The first parameter will be a
    string named phrase. The second parameter will be a number named
    count. Print phrase to the screen count times.
    (e.g., the function takes in "Hello" and 5, then prints "Hello" five times.)
def smth(phrase, count):
   for i in range(count):
       print(phrase) 

34. Write code to call the previous function.
smth("Hi", 5)

35. Write code for a function that takes in a number, and returns the square of
    that number. (I'm not asking for the square root, but the number squared.)
    Note, this function should RETURN the answer, not print it out.
def sqr(x):
    return x*x

36. Write code to call the function above and print the output.
print(sqr(5))

37. Write a function that takes three numbers as parameters, and returns the
    centrifugal force. The formula for centrifugal force is: 
    F=m(v^2/r)
    F is force, m is mass, r is radius, and v is angular velocity.
def cen_force(m,v,r):
    return (m*(v*v/r))

38. Write code to call the function above and display the result.
print(cen_force(6,2,3))

39. Write a function that takes a list of numbers as a parameter, and prints out
    each number individually using a for loop.
def print_list(x):
    for item in range(len(x)):
        print(x[item])
