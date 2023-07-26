import numpy as np
# hyperbolic functions in radian
'''
x = np.sinh(np.pi/2)
print(x)

# creating arrays for cosh value
arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
x = np.cosh(arr)
print(x)

# finding angles
x = np.arcsinh(1.5)
arr_ang = np.array([0.5, 1.0, 0.2, 0.3])
y = np.arctanh(arr_ang)
print(x)
print(y)
'''


# Set operations
arr = np.array([1, 1, 1, 2, 3, 4, 5, 5, 6, 7])
x = np.unique(arr)
print(x)

# union, intersection, difference and symmetric difference of two set arrays
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([2, 4, 6, 8])
arr_union = np.union1d(arr1, arr2)
arr_intersect = np.intersect1d(arr1, arr2, assume_unique=True)
arr_diff = np.setdiff1d(arr1, arr2, assume_unique=True)
arr_symdiff = np.setxor1d(arr1, arr2, assume_unique=True)
print('Union of two arrays:', arr_union)
print('Intersection of two arrays:', arr_intersect)
print('Difference of two arrays:', arr_diff)
print('Symmetric difference:', arr_symdiff)
