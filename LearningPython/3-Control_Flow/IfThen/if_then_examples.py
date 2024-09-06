
# Example 1: Basic 'if' statement
# Checking if a number is positive

number = 10
if number > 0:
    print(f'{number} is positive')


# Example 2: 'if-else' statement
# Checking if a number is even or odd

number = 7
if number % 2 == 0:
    print(f'{number} is even')
else:
    print(f'{number} is odd')


# Example 3: 'if-elif-else' statement
# Checking the grade category of a score

score = 85
if score >= 90:
    print('Grade: A')
elif score >= 80:
    print('Grade: B')
elif score >= 70:
    print('Grade: C')
else:
    print('Grade: F')


# Example 4: Nested 'if' statements
# Checking if a person is eligible to vote

age = 18
citizen = True

if age >= 18:
    if citizen:
        print('Eligible to vote')
    else:
        print('Not a citizen, ineligible to vote')
else:
    print('Underage, ineligible to vote')


# Example 5: Multiple conditions using 'and'/'or'
# Checking if a number is in a specific range

number = 25
if number >= 10 and number <= 30:
    print(f'{number} is between 10 and 30')
else:
    print(f'{number} is outside the range')
