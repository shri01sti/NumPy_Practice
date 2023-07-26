import numpy as np
# wuthout ufunc, using python biltin zip() method
'''
arr1 = [1, 2, 3, 4]
arr2 = [2, 5, 7, 9]
z = []
for i, j in zip(arr1 + arr2):
    z.append(i+j)
print(z)

# using add()
x = [1, 2, 3, 4, 5]
y = [3, 4, 5, 6, 7]
z = np.add(x, y)
print('addition using ufunc add():', z)

# normal addition
a = np.array([1, 2, 3, 4])
b = np.array([2, 4, 5, 6])
c = a+b
print(c)

# creating our own ufunc for addition


def my_add(x, y):
    return x + y


my_add = np.frompyfunc(my_add, 2, 1)
print('Addition creating own ufunc:', my_add([1, 2, 3, 4], [5, 6, 7, 8]))

# check if a function is a ufunc or not
print(type(np.add))
print(type(np.concatenate))

# using an if statement to check if the function is a ufunc or not
if type(np.add) == np.ufunc:
    print('add is ufunc')
else:
    print('add is not a ufunc')

# Simple Addition # add #subtract #multiply#division #power #remainder or#mod #Quotient and mod(return value is two array, 1st one is quotient and the aother is mod),#absolute values


def perform_array_operation(arr1, arr2):
    arr_add = np.add(arr1, arr2)
    arr_sub = np.subtract(arr1, arr2)
    arr_mul = np.multiply(arr1, arr2)
    arr_div = np.divide(arr1, arr2)
    arr_pow = np.power(arr1, arr2)
    arr_rem = np.remainder(arr1, arr2)
    arr_mod = np.mod(arr1, arr2)
    arr_divmod = np.divmod(arr1, arr2)
    arr_abs = np.absolute(arr1)

    return {
        'Sum is': arr_add,
        'Subtraction is': arr_sub,
        'Product is': arr_mul,
        'division is': arr_div,
        'power is': arr_pow,
        'remainder is': arr_rem,
        'mod is': arr_mod,
        'divmod is': arr_divmod,
        'absolute is': arr_abs

    }


arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([2, 4, 6, 8, 10])
result = perform_array_operation(arr1, arr2)

for operation, arr_result in result.items():
    print(operation, arr_result)
'''

# Rounding Decimals
# truncation trunc(),fix(),rounding around(),floor(), ceil()
arr_trun = np.trunc([3.5678, -2.2134])
arr_fix = np.fix([2.2312, -3.456])
arr_round = np.around([3.456, 2.789])
arr_floor = np.floor([-2.3678, 5.6667])
arr_ceil = np.ceil([2.2345, 4.4567])
print(arr_trun)
print(arr_fix)
print(arr_round)
print(arr_floor)
print(arr_ceil)
