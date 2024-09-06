# Python Lists Examples

# Creating lists
int_list = [1, 2, 3, 4, 5]
str_list = ["apple", "banana", "cherry"]
mixed_list = [1, "apple", 3.14, True]
nested_list = [1, [2, 3], [4, 5, 6]]

# Accessing list elements
first_element = int_list[0]  # Outputs: 1
last_element = int_list[-1]  # Outputs: 5
sub_list = int_list[1:3]  # Outputs: [2, 3]

# Modifying lists
int_list[0] = 10  # int_list is now [10, 2, 3, 4, 5]
int_list.append(6)  # int_list is now [10, 2, 3, 4, 5, 6]
int_list.insert(1, 15)  # int_list is now [10, 15, 2, 3, 4, 5, 6]
int_list.remove(3)  # int_list is now [10, 15, 2, 4, 5, 6]
removed_element = int_list.pop(2)  # int_list is now [10, 15, 4, 5, 6]
int_list.clear()  # int_list is now []

# List methods
fruits = ["apple", "banana"]
fruits.append("cherry")  # fruits is now ["apple", "banana", "cherry"]
more_fruits = ["date", "elderberry"]
fruits.extend(more_fruits)  # fruits is now ["apple", "banana", "cherry", "date", "elderberry"]
fruits.insert(1, "blueberry")  # fruits is now ["apple", "blueberry", "banana", "cherry", "date", "elderberry"]
fruits.remove("banana")  # fruits is now ["apple", "blueberry", "cherry", "date", "elderberry"]
removed_fruit = fruits.pop(1)  # fruits is now ["apple", "cherry", "date", "elderberry"]
fruits.clear()  # fruits is now []

# Other list functions
numbers = [3, 1, 4, 2]
numbers.sort()  # numbers is now [1, 2, 3, 4]
numbers.reverse()  # numbers is now [4, 3, 2, 1]
fruits = ["apple", "banana", "cherry"]
index_of_banana = fruits.index("banana")  # Outputs: 1
count_of_banana = fruits.count("banana")  # Outputs: 1
fruits_copy = fruits.copy()  # fruits_copy is ["apple", "banana", "cherry"]
