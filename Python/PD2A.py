print("Pavithra Ravichandran")
print("Welcome to Python!")
print("I am learning Python.")
print("This is my first Python practice.")
name = "Pavithra"
age = 25
favorite_color = "Blue"
print(name)
print(age)
print(favorite_color)
name = "Pavithra"      
age = 25               
height = 5.4            
is_student = True      

print(type(name))
print(type(age))
print(type(height))
print(type(is_student))
user_name = input("Enter your name: ")
print(f"Welcome, {user_name}!")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
sum_result = num1 + num2

print(f"Sum = {sum_result}")
number = input("Enter a number: ")

print(f"Before conversion: {type(number)}")

number = float(number)

print(f"After conversion: {type(number)}")
user_name = input("Enter your name: ")
user_age = input("Enter your age: ")
city = input("Enter your city: ")

print(f"My name is {user_name}, I am {user_age} years old, and I live in {city}.")
length = float(input("Enter rectangle length: "))
width = float(input("Enter rectangle width: "))

area = length * width

print(f"Area of the rectangle = {area}")



item = input("Enter item name: ")
quantity = int(input("Enter quantity: "))
price = float(input("Enter price: "))

total = quantity * price

print("\n========== RECEIPT ==========")
print(f"Item: {item}")
print(f"Quantity: {quantity}")
print(f"Price: ₹{price}")
print(f"Total: ₹{total}")
print("=============================")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(f"Before swapping: a = {a}, b = {b}")

a, b = b, a

print(f"After swapping: a = {a}, b = {b}")
celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9 / 5) + 32

print(f"{celsius}°C = {fahrenheit}°F")
profile_name = input("Enter your name: ")
profile_age = input("Enter your age: ")
height = float(input("Enter your height in cm: "))
hobby = input("Enter your favorite hobby: ")

print("\n========== PROFILE ==========")
print(f"Name: {profile_name}")
print(f"Age: {profile_age}")
print(f"Height: {height} cm")
print(f"Favorite Hobby: {hobby}")
print("=============================")
