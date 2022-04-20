What does this program print out? (Remember: TWO answers. Your guess and the actual result. Label both.)
x = 0
while x < 10:
    print(x)
    x = x + 2

GUESS: 0 2 4 6 8
ACTUAL:
0
2
4
6
8

What does this program print out?
x = 1
while x < 64:
    print(x)
    x = x * 2
Answer:
1
2
4
8
16
32

Why is the ``and x >= 0'' not needed?
x = 0
while x < 10 and x >= 0:
    print(x)
    x = x + 2
Answer: Da x schon kleiner als 10 definiert ist und und x nie kleiner 0 sein kann, da in der 4. Zeile +2 addiert wird.

What does this program print out? (0 pts) Explain. (1 pt)
x = 5
while x >= 0:
    print(x)
    if x == "1":
        print("Blast off!")
    x = x - 1

Answer: Das Programm zählt von 5 bis 0 runter. Leider funktioniert die Zeile print("Blast off!") nicht, da im If darüber die 1 in "" steht und damit als String gewertet wird.
Deshalb kann kein Vergleich mit 1 und "1" passieren.

Fix the following code so it doesn't repeat forever, and keeps asking the user until he or she enters a number greater than zero: (2 pts)
x = float(input("Enter a number greater than zero: "))
 
while x <= 0:
    print("Too small. Enter a number greater than zero: ")

Fixed:
x = float(input("Enter a number greater than zero: "))
 
if x <= 0:
    print("Too small. Enter a number greater than zero: ")

Fix the following code:
#Fixed
x = 10
 
while x > 0:
    print(x)
    x = x - 1
 
print("Blast-off")

What is wrong with this code? It runs but it has unnecessary code. Find all the unneeded code. Also, answer why it is not needed. (1 pt)
i = 0
for i in range(10):
    print(i)
    i += 1

FIXED:
for i in range(10):
    print(i)

1. Man muss nicht die Variable vorher definieren, da sie schon in der Schleife definiert wird.
2. Das "Hochzählen" in Zeile 4 ist nicht nötig wegen der range() Funktion.

Explain why the values printed for x are so different. (2 pts)
# Sample 1
x = 0
for i in range(10):
    x += 1
for j in range(10):
    x += 1
print(x)
 
# Sample 2
x = 0
for i in range(10):
    x += 1
    for j in range(10):
        x += 1
print(x)

Answer: Da in Sample 1 zwei Schleifen nacheinader ablaufen und dadurch 10+10=20 ergibt.
In Sample 2 gibt es eine Schleife in der Schleife. Das heißt, das die erste Schleife nur 1 mal runterzählt bis sie die andere Schleife erreicht hat, die dann aber 10 mal runterzählt. Danach springt sie wieder in die erste Schleife und alles beginnt von vorne. Deshalb hat Sample 2 das Ergebnis 110. 