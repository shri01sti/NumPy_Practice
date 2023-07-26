import numpy as np
from math import log
'''
# log base 2, 10, natural log or load=g at base 'e'
# The arange(1, 10) function returns an array with integers starting from 1 (included) to 10 (not included).
arr = np.arange(1, 10)
print(np.log2(arr))
print(np.log10(arr))
print(np.log(arr))

# log without any base
nplog = np.frompyfunc(log, 2, 1)
print('log without any base;', nplog(100, 15))

# Define the NumPy universal function for log
nplog = np.frompyfunc(log, 2, 1)
# or
# Apply the nplog function to arrays as inputs
result = nplog(np.array([100]), np.array([15]))
print(result)

# Summation
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([4, 5, 6, 7])
arr_add = np.add(arr1, arr2)
arr_sum = np.sum([arr1, arr2])
arr_sumaxis = np.sum([arr1, arr2], axis=1)
arr_cumsum = np.cumsum([arr1])
print('Summation is:', arr_sum)
print('Addition is:', arr_add)
print('Summation over axis is:', arr_sumaxis)
print('Cumulative sum is:', arr_cumsum)

# Summation  using a function


def array_operations(arr1, arr2):
    arr_add = np.add(arr1, arr2)
    arr_sum = np.sum([arr1, arr2])
    arr_sumaxis = np.sum([arr1, arr2], axis=1)
    arr_cumsum = np.cumsum(arr1)
    return arr_sum, arr_add, arr_sumaxis, arr_cumsum


# Input arrays
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([4, 5, 6, 7])

# Call the function and get the results
sum_result, add_result, sumaxis_result, cumsum_result = array_operations(
    arr1, arr2)

# Print the results
print('Summation is:', sum_result)
print('Addition is:', add_result)
print('Summation over axis is:', sumaxis_result)
print('Cumulative sum is:', cumsum_result)

# Products
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 5, 7, 9])

x = np.prod(arr1)
y = np.prod([arr1, arr2])
z = np.prod([arr1, arr2], axis=1)
cum_prod = np.cumprod(arr1)
print(x)
print(y)
print(z)
print(cum_prod)

# Difference
arr_diff = np.array([12, 14, 15, 6])
new_arr = np.diff(arr_diff)
x = np.diff(arr_diff, n=2)
print('difference:', new_arr)
# difference between the output of previous one
print('difference with n = 2:', x)

# LCM
num1 = 4
num2 = 6
arr = np.array([2, 6, 8])
arr_1 = np.arange(1, 11)
x = np.lcm(num1, num2)
y = np.lcm.reduce(arr)
z = np.lcm.reduce(arr_1)
print('lcm of 4 and 6 is', x)
print('lcm of an array:', y)
print('lcm of num from 1 to 10:', z)


# HCF /GCD
a = np.gcd(num1, num2)
b = np.gcd.reduce(arr)
print('hcf is', a)
print('hcf of an array:', arr)
'''

# Trigonometric Function
x = np.sin(np.pi/2)
arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/4])
y = np.sin(arr)
z = np.deg2rad(arr)  # degree to radian
a = np.rad2deg(arr)  # radian to degree
print(x)
print(y)
print('in radian:', z)
print('in degree:', a)

# finding angles
ang1 = np.arcsin(1.0)
arr = np.array([1, -1, 0.1])
new_arr = np.arcsin(arr)
print(ang1)
print(new_arr)

# hypotenuse
base = 3
perp = 4
x = np.hypot(base, perp)
print('hypotenuse side:', x)
