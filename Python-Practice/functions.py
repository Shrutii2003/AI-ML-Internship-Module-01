# Python Functions Practice

# Simple function
def greet():
    print("Hello, welcome to Python!")

greet()


# Function with parameters
def greet_user(name):
    print("Hello", name)

greet_user("Shruti")
greet_user("Rahul")


# Function to add two numbers
def add_numbers(a, b):
    return a + b

result = add_numbers(10, 20)
print("Sum:", result)


# Function to calculate square
def square(number):
    return number * number

print("Square of 5:", square(5))
