# Python Sets Examples

# Creating sets
empty_set = set()
num_set = {1, 2, 3}
str_set = {'apple', 'banana', 'cherry'}
list_set = set([1, 2, 3, 4, 5])

# Accessing set elements
is_in_set = 'apple' in str_set  # Outputs: True
for item in num_set:
    print(item)

# Set methods
num_set.add(4)  # Adds 4 to num_set
num_set.remove(3)  # Removes 3 from num_set
num_set.discard(5)  # Removes 5 from num_set if present, does nothing if not
num_set.pop()  # Removes and returns an arbitrary element from num_set
num_set.clear()  # Removes all elements from num_set

# Set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2  # Outputs: {1, 2, 3, 4, 5}
intersection_set = set1 & set2  # Outputs: {3}
difference_set = set1 - set2  # Outputs: {1, 2}
symmetric_difference_set = set1 ^ set2  # Outputs: {1, 2, 4, 5}
