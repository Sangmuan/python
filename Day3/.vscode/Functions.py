name = input("Enter your name: ")
print("Hello, " + name + "!")

# DAY 3

def greet(*names):
    for name in names:
        print("Hello, " + name + "!")
greet("Alice", "Bob", "Charlie")


def total_sum(*numbers):
    print(sum(numbers))

total_sum(1, 2, 3)
total_sum(10, 20)

#Functions 2

def show_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

show_info(name="Alice", age=25, city="Paris")

# Functions 3

def demo(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

demo(1, 2, 3, name="Alice", age=25)

# Function 4   Function callling another function

def square(x):
    return x * x

def display_result(y):
    result = square(y)
    print("Result:", result)

display_result(10)

#Function 5   Recursive function
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
print(factorial(5))  # Output: 120


# Function 6   recursive function
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # Output: 120

# Function 7   Lambda function
def add(x, y):
    return x + y
print(add(5, 3))  # Output: 8

# Function 8   Lambda function
add = lambda x, y: x + y
print(add(5, 3))  # Output: 8

msg = lambda name: "Hello, " + name + "!"
print(msg("Alice"))  # Output: Hello, Alice!

# Function 

def multiplier(factor):
    def multiply(n):
        return n * factor
    return multiply
double = multiplier(2)
print(double(5))  # Output: 10

# Funtion decorator

def shout(func):
    def wrapper():
        print("Calling function...")
        func()
        print("Function call complete.")
    return wrapper

@shout
def hello():
    print("Hello, world!")

hello()

