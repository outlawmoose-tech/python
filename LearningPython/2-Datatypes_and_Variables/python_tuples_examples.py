# Python Tuples Examples

# Creating tuples
empty_tuple = ()
num_tuple = (1, 2, 3)
str_tuple = ('apple', 'banana', 'cherry')
nested_tuple = (1, (2, 3), (4, 5, 6))

# Accessing tuple elements
first_element = num_tuple[0]  # Outputs: 1
last_element = num_tuple[-1]  # Outputs: 3
sub_tuple = num_tuple[1:3]  # Outputs: (2, 3)

# Tuple functions
length = len(num_tuple)  # Outputs: 3
count_of_1 = num_tuple.count(1)  # Outputs: 1
index_of_2 = num_tuple.index(2)  # Outputs: 1

# Immutable nature of tuples
try:
    num_tuple[0] = 10  # TypeError: 'tuple' object does not support item assignment
except TypeError as e:
    print(e)
