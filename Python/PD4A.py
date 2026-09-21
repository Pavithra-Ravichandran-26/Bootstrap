# word = "PYTHON"

# for char in word:
#     print(char)

# text = input("Enter a string: ")

# count = 0

# for char in text:
#     if char in "aeiouAEIOU":
#         count += 1

# print("Number of vowels:", count)

# text = input("Enter a string: ")

# reverse = ""

# for char in text:
#     reverse = char + reverse

# print("Reversed string:", reverse)

# for number in range(1, 21):
#     print(number)

# for number in range(2, 51, 2):
#     print(number)

# for number in range(10, 0, -1):
#     print(number)

# while True:
#     number = int(input("Enter a number: "))

#     if number == 0:
#         break

#     print("You entered:", number)

# print("Loop stopped")

# for number in range(1, 51):

#     if number % 5 == 0:
#         continue

#     print(number)

# for number in range(1, 11):

#     if number == 5:
#         pass
#     else:
#         print(number)

# for number in range(1, 11):
#     print(number)

# else:
#     print("Loop finished successfully")

# word = "HELLO"

# for index, char in enumerate(word):
#     print(index, char)

sentence = input("Enter a sentence: ")

words = sentence.split()

# for position, word in enumerate(words, start=1):
#     print(position, word)

# for number in range(1, 11):

#     for multiplier in range(1, 11):
#         print(number, "x", multiplier, "=", number * multiplier)

    # print()

# import time

# start_time = time.time()

# while True:
#     print("Hello, World!")

#     if time.time() - start_time >= 5:
#         break

# while True:
#     text = input("Enter something: ")

#     if text == "exit":
#         break

#     print("You entered:", text)

number = 1

# while number <= 20:

#     if number % 2 != 0:
#         number += 1
#         continue

#     print(number)

#     number += 1

# while True:
#     number = int(input("Enter a positive number: "))

#     if number < 0:
#         continue

#     if number > 0:
#         print("You entered:", number)
#         break

# number = 1

# while number <= 30:

#     if number % 3 == 0:
#         number += 1
#         continue

#     print(number)

#     number += 1

# correct_password = "python123"

# while True:

#     password = input("Enter password: ")

#     if password == correct_password:
#         print("Correct password!")
#         break

#     print("Incorrect password. Try again.")

# correct_pin = "1234"

# for attempt in range(1, 4):

#     pin = input("Enter your PIN: ")

#     if pin == correct_pin:
#         print("PIN correct. Welcome!")
#         break

#     print("Incorrect PIN.")

# else:
#     print("Account Locked")

# for number in range(10):
#     pass

# print("Loop completed")

# for number in range(1, 6):

#     if number == 3:
#         pass
#     else:
#         print(number)

number = 1

# while number <= 5:
#     print(number)
#     number += 1

# else:
#     print("Loop completed successfully")

count = 0

while count < 5:

    word = input("Enter a word: ")

    if word == "Python":
        print("You entered Python!")
        break

    count += 1

else:
    print("You never entered 'Python'!")