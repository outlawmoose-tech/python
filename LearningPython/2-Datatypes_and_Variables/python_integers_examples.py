# Python Integers Examples

# Creating integers
a = 10
b = -5
c = 0

# Type conversion
float_num = 10.5
int_num = int(float_num)  # Outputs: 10

str_num = "20"
int_num_from_str = int(str_num)  # Outputs: 20

# Arithmetic operations
sum_result = a + b  # Outputs: 5
sub_result = a - b  # Outputs: 15
mul_result = a * b  # Outputs: -50
div_result = a / b  # Outputs: -2.0
int_div_result = a // b  # Outputs: -2
mod_result = a % b  # Outputs: 0
exp_result = a ** 2  # Outputs: 100

# Built-in functions
abs_value = abs(-10)  # Outputs: 10
quotient, remainder = divmod(15, 4)  # Outputs: (3, 3)
power = pow(2, 3)  # Outputs: 8
mod_power = pow(2, 3, 5)  # Outputs: 3
rounded_value = round(15.456, 2)  # Outputs: 15.46
max_value = max(1, 5, 3, 9, 2)  # Outputs: 9
min_value = min(1, 5, 3, 9, 2)  # Outputs: 1
