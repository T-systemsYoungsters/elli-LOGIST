List the four types of data we've covered, and give an example of each:
    String -> x = "HI"
    Integer -> x = 6
    Floating point -> x =7.8
    Boolean -> x = True

What does this code print out? For this and the following problems, make sure you understand WHY it prints what it does. You don't have to explain it, but if you don't understand why, make sure to ask. Otherwise you are wasting your time doing these.
my_list = [5, 2, 6, 8, 101]
print(my_list[1])
print(my_list[4])
print(my_list[5])

Answer: Gibt den Wert von der Position aus.

What does this code print out?
my_list=[5, 2, 6, 8, 101]
for my_item in my_list:
    print(my_item)

Answer: 5
2
6
8
101

What does this code print out?
my_list1 = [5, 2, 6, 8, 101]
my_list2 = (5, 2, 6, 8, 101)

my_list1[3] = 10 
print(my_list1)
# prints [5, 2, 6, 10, 101]
my_list2[2] = 10
print(my_list2)
# Error: Tupel kann nicht verändert werden

What does this code print out?
my_list = [3 * 5]
print(my_list)
my_list = [3] * 5
print(my_list)

# Beides [3, 3, 3, 3, 3]

What does this code print out?
my_list = [5]
for i in range(5):
    my_list.append(i)
print(my_list)

# [5, 0, 1, 2, 3, 4]

What does this code print out?
print(len("Hi")) # 2
print(len("Hi there.")) # 9
print(len("Hi") + len("there.")) # 8
print(len("2")) # 1
print(len(2)) # error

What does this code print out?
print("Simpson" + "College")
print("Simpson" + "College"[1])
print( ("Simpson" + "College")[1] )

# laut Computer 
SimpsonCollege
Simpsono
i

What does this code print out?
word = "Simpson"
for letter in word:
    print(letter)

Answer: S
i
m
p
s
o
n

What does this code print out?
word = "Simpson"
for i in range(3):
    word += "College"
print(word)

Answer: SimpsonCollegeCollegeCollege

What does this code print out?
word = "Hi" * 3
print(word)

Answer: HiHiHi

What does this code print out?
my_text = "The quick brown fox jumped over the lazy dogs."
print("The 3rd spot is: " + my_text[3])
print("The -1 spot is: " + my_text[-1])

#The 3rd spot is:  
#The -1 spot is: .

What does this code print out?
s = "0123456789"
print(s[1]) # 1
print(s[:3]) # 012
print(s[3:]) # 456789


Write a loop that will take in a list of five numbers from the user, adding each to an array. Then print the array. Try doing this without looking at the book.

arraylist = []

for i in range(5):
    user_input = int(input("Enter a number: "))
    arraylist.append(user_input)
print(arraylist)

Write a program that take an array like the following, and print the average. Use the len function, don't just use 15, because that won't work if the list size changes. (There is a sum function I haven't told you about. Don't use that. Sum the numbers individually as shown in the chapter.) (Also, a common mistake is to calculate the average each time through the loop to add the numbers. Finish adding the numbers before you divide.)
my_list = [3,12,3,5,3,4,6,8,5,3,5,6,3,2,4]my_list = [3,12,3,5,3,4,6,8,5,3,5,6,3,2,4]

num = 0

for i in range(len(my_list)):
    num += my_list[i]

num = num/len(my_list)
    
print(num)