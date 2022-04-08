Chapter 01 Worksheet 
 
     
    When writing answers to questions, please use proper grammar, capitalization,
    and punctuation. Please limit the length of each line to 80 characters.
     
 1. Write a line of code that will print your name.

 print("Elli")
 
 2. How do you enter a comment in a program?

 # This is a comment
 
 3. What do the following lines of code output?
       ALSO: Why do they give a different answer?
     
    print(2 / 3) # = 1.5
    print(2 // 3) # = 2
    # because floor division will always round the answer down
     
 4. Write a line of code that creates a variable called pi and sets
       it to an appropriate value.
       pi = 3.14159

       or 

       import math
       print(math.pi)
 
 5. Why does this code not work?
     
    A = 22
    print(a)
    # It does not work because Python is a case sensitive language and 'A' and 'a' are not the same
     
 6. All of the variable names below can be used. But which ONE of these is
       the better variable name to use?
     
    a
    A
    Area
    AREA
    area
    area_of_rectangle # this one is the best
    Area_Of_Rectangle
     
 7. Which of these variables names are not allowed in Python? (More than one
    might be wrong. Also, this question is not asking about improper names, just
    names that aren't allowed. Test them if you aren't sure.)
     
    apple
    Apple
    APPLE
    Apple2
    1Apple #this one is not allowed
    account number
    account_number
    account.number #this one is not allowed
    accountNumber
    account# #this one is not allowed
    pi
    PI
    fred
    Fred
    GreatBigVariable
    greatBigVariable
    great_big_variable
    great.big.variable #this one is not allowed
    2x  #this one is not allowed
    x2x
    total% 
    #left  #this one is not allowed
     
 8. Why does this code not work?
     
    print(a)
    a = 45

    # This wont work because you have to set the variable before everything and thats why 
    # python doesnt know what to print

     
 9. Explain the mistake in this code:
     
    pi = float(3.14)
    # the number itselve indicates a float and you cant convert it any further
     
10. This program runs, but the code still could be better. Explain what is
    wrong with the code.
     
    radius = float(input("Radius:"))
    x = 3.14
    pi = x    # instead of x you could write the code together
    area = pi  * radius ** 2 # Python might confuse the order of operations, use parentheses 
    print(area)


     
11. Explain the mistake in the following code:
     
    x = 4
    y = 5
    a = ((x) * (y)) # you dont have to put any parentheses 
    print(a)
     
12. Explain the mistake in the following code:
     
    x = 4
    y = 5
    a = 3(x + y) # there is a * missing between the 3 and the parentheses 
    print(a)
     
13. Explain the mistake in the following code:
     
    radius = input(float("Enter the radius:")) # the order of input and float is wrong, just swap them 
     
14. Do all these print the same value? Which one is better to use and why?
     
    print(2/3+4)
    print(2 / 3 + 4)
    print(   2 /    3+    4  )  # yes 
     
15. What is a constant?
   #a variable you can not change anymore 
 
16. How are variable names for constants different than other variable names?
# you write your variables in lower case and constants only in upper case

17. What is a single quote and what is a double quote?
    Give and label an example of both.
 # Single quotes are used to mark a quote within a quote, e.g. "This 'is' a quote"
 #Use double quotes to enclose your strings when you know there are going to be single quotes within your string, e.g. "Hi"

18. Write a Python program that will use escape codes to print a double-quote
    and a new line using the Window's standard. (Note: I'm asking for the Window's
    standard here. Look it up out of Chapter 1.)
  # print("This is what you need:\n\"name\"")

 
19. Can a Python program print text to the screen using single quotes instead
    of double quotes?
    # No
 
20. Why does this code not calculate the average?
     
    print(3 + 4 + 5 / 3)
    # because there are no parentheses
     
 
21. What is an ``operator'' in Python?
   # common mathematical operators
22. What does the following program print out?
     
    x = 3
    x + 1
    print(x) 
    # it will print 3
     
 
23. Correct the following code:
     
    user_name = input("Enter your name: )"
    # CORRECT: user_name = input("Enter your name: ")
     
 
24. Correct the following code:
     
    value = int(input(print("Enter your age")))
    # CORRECT: value = int(input("Enter your age"))
