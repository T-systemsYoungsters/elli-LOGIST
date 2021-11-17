#1.1 Part A

fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = (fahrenheit - 32)*(5/9)
print("The temperature in Celsius: ", celsius)


#1.2 Part B

print("Area of a trapezoid")
t_height = float(input("Enter the height of the trapezoid: "))
t_bottom_base = float(input("Enter the length of the bottom base: "))
t_top_base = float(input("Enter the length of the top base: "))
area = 0.5*(t_top_base + t_bottom_base)*t_height
print("The area is: ", area)


#1.3 Part C

print("Area of an ellipse")
pi = 3.14159
ellipse_radius1 = float(input("Enter the first radius: "))
ellipse_radius2 = float(input("Enter the second radius: "))
area = pi*ellipse_radius1*ellipse_radius2
print("The area is: ", area)
