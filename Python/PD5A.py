# def greet_user():
#     print("Hello, User!")


# greet_user()

# def calculate_sum(a, b):
#     return a + b


# result = calculate_sum(10, 20)

# print("Sum:", result)

# def check_positive(num):

#     if num > 0:
#         return "Positive"
#     else:
#         pass


# result = check_positive(10)

# print(result)

# def find_max(a, b, c):

#     if a >= b and a >= c:
#         return a

#     elif b >= a and b >= c:
#         return b

#     else:
#         return c


# result = find_max(10, 25, 15)

# print("Maximum:", result)

# count = 10


# def modify_count():

#     global count

#     count = 20

#     print("Inside function:", count)


# modify_count()

# print("Outside function:", count)

# def modify_variable():

#     message = "Local Scope"

#     print("Inside function:", message)


# modify_variable()

# print("Outside function:", message)

# def modify_variable():

#     message = "Local Scope"

#     print("Inside function:", message)


# modify_variable()

# print("Outside function: message is not accessible")

# def factorial(n):

#     if n == 0 or n == 1:
#         return 1

#     return n * factorial(n - 1)


# result = factorial(5)

# print("Factorial:", result)

# def fibonacci(n):

#     if n <= 1:
#         return n

#     return fibonacci(n - 1) + fibonacci(n - 2)


# result = fibonacci(6)

# print("Fibonacci:", result)

# def sum_numbers(*args):

#     total = 0

#     for number in args:
#         total += number

#     return total


# result = sum_numbers(10, 20, 30, 40)

# print("Sum:", result)

# def print_student_details(**kwargs):

#     for key, value in kwargs.items():
#         print(key, ":", value)


# print_student_details(
#     name="Pavithra",
#     age=27,
#     grade="A"
# )

# def apply_operation(func, a, b):

#     return func(a, b)


# result = apply_operation(lambda x, y: x + y, 10, 20)

# print("Result:", result)

# def outer_function():

#     def inner():
#         return "Hello from Inner Function"

#     return inner()


# result = outer_function()

# print(result)

# numbers = [1, 2, 3, 4, 5]

# result = list(map(lambda x: x * 2, numbers))

# print(result)

