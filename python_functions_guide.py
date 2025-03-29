# Understanding Python Functions: A Step-by-Step Guide

# 1. What is a Function?
"""
A function is a reusable block of code that performs a specific task. Functions help you:
- Organize your code
- Avoid repetition
- Make your code more maintainable
- Break down complex problems into smaller parts
"""

# 2. Basic Function Syntax
def greet():
    print("Hello, World!")

# Calling the function
greet()

# 3. Function Parameters
def greet_person(name):
    print(f"Hello, {name}!")

# Calling the function with different arguments
greet_person("Alice")
greet_person("Bob")

# 4. Return Values
def add_numbers(a, b):
    return a + b

# Using the return value
result = add_numbers(5, 3)
print(f"The sum is: {result}")

# 5. Function Scope
# Global variable
message = "Global message"

def print_message():
    # Local variable
    local_message = "Local message"
    print(message)  # Can access global variable
    print(local_message)  # Can access local variable

print_message()
# print(local_message)  # This would cause an error - local_message is not accessible here

# 6. Advanced Concepts
# Default Parameters
def greet_with_title(name, title="Mr."):
    print(f"Hello, {title} {name}!")

# Using default parameter
greet_with_title("Smith")  # Uses default title
greet_with_title("Johnson", "Dr.")  # Overrides default title

# Keyword Arguments
def create_profile(name, age, city):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"City: {city}")

# Using keyword arguments
create_profile(name="Alice", age=25, city="New York")
create_profile(city="London", name="Bob", age=30)  # Order doesn't matter

# *args and **kwargs
def sum_all(*numbers):
    return sum(numbers)

print(sum_all(1, 2, 3, 4, 5))

def print_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

print_info(name="Charlie", age=35, city="Paris")

# 7. Practice Exercises
# Exercise 1: Create a function that calculates the factorial of a number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))  # Should print 120

# Exercise 2: Create a function that checks if a string is a palindrome
def is_palindrome(text):
    cleaned_text = ''.join(text.lower().split())
    return cleaned_text == cleaned_text[::-1]

print(is_palindrome("A man a plan a canal Panama"))  # Should print True

"""
Additional Tips:
1. Use descriptive function names that explain what the function does
2. Keep functions focused on a single task
3. Document your functions using docstrings
4. Use type hints to make your code more readable and maintainable
5. Test your functions with different inputs

Remember: Practice makes perfect! Try creating your own functions and experiment with different concepts.
""" 