import numpy as np
'''
# conctenating two 1D arrays
arr_1 = np.array([1, 2, 3])
arr_2 = np.array([4, 5, 6])
arr_conc = np.concatenate((arr_1, arr_2))
arr_stack = np.stack((arr_1, arr_2), axis=1)
arr_alrow = np.hstack((arr_1, arr_2))
arr_alcolumn = np.vstack((arr_1, arr_2))
arr_aldepth = np.dstack((arr_1, arr_2))
print('using concatenate func:', arr_conc)
print('using stack function:', arr_stack)
print('using hstack function:', arr_alrow)
print('using vstack function:', arr_alcolumn)
print('using dstack function:', arr_aldepth)


# concatenating two 2D arrays along rows(axis = 1)
arr_1 = np.array([[2, 3], [4, 5]])
arr_2 = np.array([[5, 6], [7, 8]])
arr_con = np.concatenate((arr_1, arr_2), axis=1)
arr_stack = np.stack((arr_1, arr_2))
arr_hstack = np.hstack((arr_1, arr_2))
arr_vstack = np.vstack((arr_1, arr_2))
arr_dstack = np.dstack((arr_1, arr_2))
print('using concatenate func:', arr_con)
print('using stack function:', arr_stack)
print('using hstack function:', arr_hstack)
print('using vstack function:', arr_vstack)
print('using dstack function:', arr_dstack)

# Splitting arrays
arr = np.arange(6).reshape(3, 2)
print(arr)
arr_split = np.array_split(arr, 3)
print(arr_split)
print(',,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,...')
arr = np.arange(6).reshape(2, 3)
print(arr)
# 4 array will not be printed as there is no enough elements in input
arr_split = np.array_split(arr, 4)
print(arr_split)


arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 4)
print(newarr)

# accessing splitted array elemnts
print(newarr[0])
print(newarr[1])
print(newarr[2])
print(newarr[3])
'''

# split 2D array into three 2D arrays
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [
               10, 11, 12], [13, 14, 15], [16, 17, 18]])
new_arr = np.array_split(arr, 3)
new_arr1 = np.array_split(arr, 3, axis=1)  # along rows
new_alrow = np.hsplit(arr, 3)  # usinh hsplit along horizontal
new_alcol = np.vsplit(arr, 3)  # using .vsplit

print(new_arr1)
print(new_alrow)
print(new_alcol)


# searching arrays
arr1 = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr1 == 4)
print(x)

# finding indexes where values are even
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x = np.array(arr % 2 == 0)
print(x)

# searchsorted() which performs a binary search in array and returns the index where the specified value would be inserted to maintain the search orde

# finding indexes where the value 7 should be inserted
arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7)
y = np.searchsorted(arr, 7, side='right')
print(x)
print(y)

# searching for more than one value,using array with the specified values
# finding indexes where the value 2,4,6 should be inserted
arr = np.array([1, 3, 5, 7])
a = np.searchsorted(arr, [2, 4, 6])
print(a)


# Sorting Arrays
arr_unsor = np.array([2, 1, 5, 4, 8, 6])
print('Sorted array is', np.sort(arr_unsor))

# sorting arrays alphabetically
arr_alpha = np.array(['shristi', 'asu', 'aswina'])
print(np.sort(arr_alpha))

# sorting a boolean array
arr_bool = np.array([True, False, True])
print(np.sort(arr_bool))

# Sorting a 2D array
arr_2 = np.array([[2, 5, 4], [7, 9, 6]])
print(np.sort(arr_2))

# filtering arrays
# creating an array indeing from 0 and 2
arr_filter = np.array([41, 42, 43, 44])
x = [True, False, True, False]
print(arr_filter[x])

# creating the filter array based on conditions
arr = np.array([41, 42, 43, 44])

# create an empty list
arr_filter = []

# go through each element in arr
for element in arr:
    # if the element is higher than 42,set value True else False
    if element > 42:
        arr_filter.append(True)
    else:
        arr_filter.append(False)
new_arr = arr[arr_filter]
print('Array returning value greater than 42 is', new_arr)

# creating a filter array that will return only even elements from the original array
arr_1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
filter_arr = []
for element in arr_1:
    if element % 2 == 0:
        filter_arr.append(True)
    else:
        filter_arr.append(False)
new_arr = arr_1[filter_arr]
print('filtered array is', new_arr)

# Creating Filter Directly form Array
arr = np.array([2, 4, 6, 8, 10])
arr_filter = arr > 4
new_arr = arr[arr_filter]
print(arr_filter)
print(new_arr)

arr_filter = arr % 2 == 0
newarr = arr[arr_filter]
print('filtered array', arr_filter)
print('new array after filter', newarr)
