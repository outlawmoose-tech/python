# Filename: python_dictionaries_example.py
# Description: Script shows examples of float type
# Company: Outlaw Moose
# Author: Todd S ([Your Email], optional)
# Created on: 2024-09-06
# Last modified: 2024-09-06
# Version: 1.0

# Python Dictionaries Examples

# Creating dictionaries
empty_dict = {}
fruit_dict = {'apple': 1, 'banana': 2, 'cherry': 3}
nested_dict = {'fruit': {'apple': 1, 'banana': 2}, 'numbers': [1, 2, 3]}

# Accessing and modifying dictionary elements
apple_value = fruit_dict['apple']  # Outputs: 1
fruit_dict['date'] = 4  # Adds 'date': 4 to fruit_dict
fruit_dict['apple'] = 5  # Changes the value of 'apple' to 5
del fruit_dict['banana']  # Removes the key 'banana'

# Dictionary methods
value = fruit_dict.get('apple', 'Not Found')  # Outputs: 5
keys = fruit_dict.keys()  # Outputs: dict_keys(['apple', 'cherry', 'date'])
values = fruit_dict.values()  # Outputs: dict_values([5, 3, 4])
items = fruit_dict.items()  # Outputs: dict_items([('apple', 5), ('cherry', 3), ('date', 4)])
value = fruit_dict.pop('date', 'Not Found')  # Outputs: 4
fruit_dict.update({'banana': 2, 'fig': 6})  # Updates fruit_dict with new key-value pairs

# Iterating over dictionaries
for key in fruit_dict:
    print(key)

for value in fruit_dict.values():
    print(value)

for key, value in fruit_dict.items():
    print(key, value)
