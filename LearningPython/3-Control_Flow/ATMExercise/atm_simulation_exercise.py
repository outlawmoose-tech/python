
# Python Exercise Solution

# Scenario: A simple ATM simulation
# The program will repeatedly ask the user to enter their PIN.
# If the PIN is correct, the user can check their balance, deposit, or withdraw money.

correct_pin = 1234
balance = 1000.00
attempts = 3

# Step 1: Check the PIN using a 'while' loop
while attempts > 0:
    entered_pin = int(input('Enter your PIN: '))
    if entered_pin == correct_pin:
        print('Access granted.')
        # Step 2: Use a 'for' loop to show the menu multiple times
        for i in range(3):  # User can make up to 3 transactions
            print('1. Check balance')
            print('2. Deposit money')
            print('3. Withdraw money')
            print('4. Exit')
            choice = int(input('Choose an option: '))
            # Step 3: Use 'if-else' to perform the operation based on the user's choice
            if choice == 1:
                print(f'Your balance is ${balance:.2f}')
            elif choice == 2:
                deposit = float(input('Enter amount to deposit: '))
                balance += deposit
                print(f'${deposit:.2f} deposited. New balance: ${balance:.2f}')
            elif choice == 3:
                withdraw = float(input('Enter amount to withdraw: '))
                if withdraw <= balance:
                    balance -= withdraw
                    print(f'${withdraw:.2f} withdrawn. New balance: ${balance:.2f}')
                else:
                    print('Insufficient funds.')
            elif choice == 4:
                print('Exiting. Thank you for using the ATM.')
                break
            else:
                print('Invalid choice, try again.')
        break
    else:
        attempts -= 1
        print(f'Incorrect PIN. You have {attempts} attempts left.')
        if attempts == 0:
            print('Account locked due to too many failed attempts.')
