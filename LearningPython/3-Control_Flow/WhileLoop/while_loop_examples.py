
# Example 1: Basic 'while' loop
# Counting from 1 to 5

counter = 1
while counter <= 5:
    print(f'Count: {counter}')
    counter += 1


# Example 2: 'while' loop with a condition
# Simulating a user guessing a number

secret_number = 7
guess = 0
while guess != secret_number:
    guess = int(input('Guess the number: '))
    if guess != secret_number:
        print('Wrong guess, try again!')
print('Correct!')


# Example 3: 'while' loop with 'break'
# Terminating a loop when a condition is met

counter = 0
while True:
    print(f'Counter: {counter}')
    counter += 1
    if counter == 5:
        print('Stopping the loop')
        break


# Example 4: 'while' loop with 'continue'
# Skipping an iteration

counter = 0
while counter < 5:
    counter += 1
    if counter == 3:
        print('Skipping 3')
        continue
    print(f'Counter: {counter}')


# Example 5: 'while' loop to process a list
# Removing elements from a list

tasks = ['Task 1', 'Task 2', 'Task 3']
while tasks:
    current_task = tasks.pop(0)
    print(f'Processing {current_task}')
print('All tasks completed!')
