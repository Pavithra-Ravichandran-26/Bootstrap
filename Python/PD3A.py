num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Sum:", num1 + num2)
print("Difference:", num1 - num2)
print("Product:", num1 * num2)
print("Quotient:", num1 / num2)
print("Remainder:", num1 % num2)

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if num1 > num2:
    print("First number is greater.")
elif num1 < num2:
    print("First number is less.")
else:
    print("Both numbers are equal.")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Before swapping: a =", a, "b =", b)

a = a + b
b = a - b
a = a - b

print("After swapping: a =", a, "b =", b)

year = int(input("Enter a year: "))

if year % 400 == 0:
    print("Leap year")
elif year % 100 == 0:
    print("Not a leap year")
elif year % 4 == 0:
    print("Leap year")
else:
    print("Not a leap year")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

print("Largest number:", largest)

radius = float(input("Enter radius: "))

area = 3.14 * radius * radius

print("Area of the circle:", area)

num = float(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible to vote.")
else:
    print("Not eligible to vote.")

marks = float(input("Enter your marks: "))

if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
else:
    print("Grade: Fail")

balance = 5000

amount = float(input("Enter withdrawal amount: "))

if amount > balance:
    print("Insufficient funds.")
else:
    balance = balance - amount
    print("Withdrawal successful.")
    print("Remaining balance:", balance)

num = int(input("Enter a number: "))

if num % 5 == 0 and num % 11 == 0:
    print("The number is divisible by both 5 and 11.")
else:
    print("The number is not divisible by both 5 and 11.")

character = input("Enter a character: ")

if character.lower() in "aeiou":
    print("Vowel")
else:
    print("Consonant")

num = int(input("Enter a number: "))

print("Even" if num % 2 == 0 else "Odd")