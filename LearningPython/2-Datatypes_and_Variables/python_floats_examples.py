# Filename: python_floats_example.py
# Description: Script shows examples of float type
# Company: Outlaw Moose
# Author: Todd S ([Your Email], optional)
# Created on: 2024-09-06
# Last modified: 2024-09-06
# Version: 1.0 


# Python Floats Examples

# Creating floats
a = 10.5
b = -5.75
c = 0.0

# Type conversion
int_num = 10
float_num = float(int_num)  # Outputs: 10.0

str_num = "20.5"
float_num_from_str = float(str_num)  # Outputs: 20.5

# Arithmetic operations
sum_result = a + b  # Outputs: 4.75
sub_result = a - b  # Outputs: 16.25
mul_result = a * b  # Outputs: -60.375
div_result = a / b  # Outputs: -1.826086956521739
int_div_result = a // b  # Outputs: -2.0
mod_result = a % b  # Outputs: 4.75
exp_result = a ** 2  # Outputs: 110.25

# Built-in functions
abs_value = abs(-10.5)  # Outputs: 10.5
rounded_value = round(15.456, 2)  # Outputs: 15.46

import math
ceil_value = math.ceil(15.2)  # Outputs: 16
floor_value = math.floor(15.8)  # Outputs: 15
sqrt_value = math.sqrt(16.0)  # Outputs: 4.0

nan_check = math.isnan(float('nan'))  # Outputs: True
inf_check = math.isinf(float('inf'))  # Outputs: True
