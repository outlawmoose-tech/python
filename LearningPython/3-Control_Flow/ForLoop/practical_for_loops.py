
# Example 1: Processing a list of sales data
# We have a list of sales data, and we want to calculate the total sales for the month.

sales = [1500, 2500, 3200, 1750, 2800, 2900, 3100]
total_sales = 0
for sale in sales:
    total_sales += sale
print(f'Total sales for the month: ${total_sales}')


# Example 2: Filtering emails by domain
# You have a list of email addresses, and you want to filter out those with a specific domain.

emails = [
    'john@example.com', 'jane@workmail.com', 'alex@example.com', 
    'lucy@company.com', 'mike@example.com'
]
filtered_emails = []
for email in emails:
    if email.endswith('@example.com'):
        filtered_emails.append(email)
print('Filtered emails:', filtered_emails)


# Example 3: Sending automatic reminders
# Simulating sending reminder emails to users by printing messages.

users = ['Alice', 'Bob', 'Charlie', 'Diana']
for user in users:
    print(f'Reminder email sent to {user}')


# Example 4: Calculating compound interest over time
# Looping through years to calculate compound interest.

principal = 1000
rate = 0.05
years = 5
for year in range(1, years + 1):
    interest = principal * rate
    principal += interest
    print(f'Year {year}: ${principal:.2f}')


# Example 5: Iterating through a directory of files
# You can loop through a directory to process files (e.g., renaming, reading).

import os

files = ['file1.txt', 'file2.txt', 'report.pdf', 'image.png']
for file in files:
    if file.endswith('.txt'):
        print(f'Processing text file: {file}')
    elif file.endswith('.pdf'):
        print(f'Processing PDF: {file}')
    else:
        print(f'Unsupported file type: {file}')
