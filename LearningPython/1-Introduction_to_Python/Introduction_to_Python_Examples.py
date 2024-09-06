# This is a comment
print("Welcome to Python Programming!")  # Print statement

# Variables and Data Types
age = 25
height = 5.9
name = "Alice"
is_student = True

# Printing Variables
print(age, height, name, is_student)

# Basic Operations
x = 10
y = 5
sum = x + y
difference = x - y
product = x * y
quotient = x / y

print("Sum:", sum)
print("Difference:", difference)
print("Product:", product)
print("Quotient:", quotient)

# Conditional Statements
if age > 18:
    print(name, "is an adult.")
else:
    print(name, "is not an adult.")

# Loops
print("Numbers from 0 to 4:")
for i in range(5):
    print(i)

print("Numbers from 0 to 4 using while loop:")
i = 0
while i < 5:
    print(i)
    i += 1

# Function
def greet(name):
    return "Hello, " + name

print(greet("Alice"))
