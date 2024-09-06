
# Example 1: Basic 'for' loop
# Looping through a list of numbers

numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(f'Number: {num}')


# Example 2: Looping through a string
# Each character in the string gets printed

word = 'Python'
for letter in word:
    print(f'Letter: {letter}')


# Example 3: Looping through a dictionary
# Accessing both keys and values in a dictionary

person = {'name': 'Alice', 'age': 30, 'city': 'New York'}
for key, value in person.items():
    print(f'{key}: {value}')


# Example 4: Using range() in a 'for' loop
# Looping through a range of numbers

for i in range(5):
    print(f'Iteration {i}')


# Example 5: Nested 'for' loops
# Looping through a 2D list (list of lists)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
    for num in row:
        print(f'Number: {num}')


# Example 6: Using 'for' loop with 'else'
# The 'else' block will execute after the loop finishes, if no break is encountered

for num in range(5):
    print(f'Number: {num}')
else:
    print('Loop finished without break')


# Example 7: Using 'break' and 'continue' in a 'for' loop
# Demonstrating loop control statements

for i in range(10):
    if i == 3:
        print('Breaking at 3')
        break
    elif i == 7:
        print('Skipping 7')
        continue
    print(f'Number: {i}')
