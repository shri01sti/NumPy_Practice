# Generating Random Numbers
import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
'''
x = random.randint(100)
print(x)
y = random.rand()
print(y)

# generating random array
arr_1i = random.randint(100, size=6)
print('1D array using integer method;', arr_1i)


# creating 2D array with 3 rows,each containing 5 random integers from 0 to 100
arr_2i = random.randint(100, size=(3, 5))
print('2D array using integer method;', arr_2i)


# creating 1D array containing 5 random integers using float method
arr_1f = random.rand(5)
print('1D array using float method;', arr_1f)

# creating 2d array with 3 rows containing 5 random nos using float method
arr_2f = random.rand(3, 5)
print('2D array using float method;', arr_2f)

# randomly returning one of the values in an array
x = random.choice([3, 5, 7, 9])
print(x)

z = random.choice([3, 6, 9, 31, 22], size=(3, 5))
print('generating 2D array with 3 row and 5 elements', z)

# random data distribution
# creating array containg 100 values, where each value has to be 3,5,7,9
# p represents probability to get those corrs values
arr_prob = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=100)
arr = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(3, 5))
print(arr_prob)
print(arr)
'''

# RANDOM PERMUTATIONS
# randomly shuffle elements of array
arr_shuffle = np.array([1, 2, 3, 4, 5, 6])
random.shuffle(arr_shuffle)
print('shuffled array:', arr_shuffle)

# generating permutation of elements {permutation() returns a rearranged array and leaves the original array unchanged}
print('permutation array:', random.permutation(arr_shuffle))
