import numpy as np
'''
# creating arrays and indexing elements
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))
print('indexing element is:', arr[0])
# slicing


# checking numpy version
print(np.__version__)

# using tuple to create a Numpy array
my_array = np.array((3, 6, 7, 6, 3))
print(my_array)
print('indexing element is:', my_array[2])

# dimensions in arrays........................ab
# 0D arrays
arr = np.array(22)
print(arr)
print('dimension is:', arr.ndim)  # to check dimension use ndim

# 1D array(array that has 0D array as elements)
arr_1 = np.array([2, 4, 6, 8, 10])
print(arr_1)
print('dimension is:', arr_1.ndim)
print('indexing element is:', arr_1[2] + arr_1[3])

# 2D array(has 1D array as elements), also use to represnt matrix or 2nd orde tensors
arr_2 = np.array([[2, 3, 4], [5, 6, 8]])
print(arr_2)
print('dimension is:', arr_2.ndim)
print('2nd element on 1st row:', arr_2[0, 1])
print('3rd element on 2nd row:', arr_2[1, 2])
print('last element from 2nd dim:', arr_2[1, -1])

# 3D arrays(has 2D arrays as its elements) to represent 3rd order tensor
arr_3 = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]]])
print(arr_3)
print('dimension is:', arr_3.ndim)
print('3rd element of the second array of the first array:', arr_3[0, 1, 2])

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print('3rd element of the second array of the first array:', arr[0, 1, 2])

# for higher dimensional arrays
# can define no. of dimensions by using the ndmin argument
arr_high = np.array([1, 2, 3, 4], ndmin=5)
print(arr_high)
print('num of dimensions:', arr_high.ndim)


# slicing 1D arrays
arr = np.array([3, 6, 9, 12, 15, 18, 21])
print(arr[1:5])
print(arr[4:])
print(arr[:4])
print(arr[-3:-1])
print(arr[1:5:2])
print(arr[::2])

# slicing 2D arrays
arr_2 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr_2[1, 1:4])
print(arr_2[0:2, 2])
print(arr_2[0:2, 1:4])



# Numpy Data Types(characters are used to represent them)
arr = np.array([1, 2, 3, 4, 5, 6])
print(arr.dtype)

arr_str = np.array(['apple', 'banana', 'litchi'])
print(arr_str.dtype)

# creating arrays with defined data type
arr_def = np.array([1, 2, 3, 4, 5], dtype='S')
print(arr_def)
print(arr_def.dtype)

# creating an array with data type 4bytes integer( size can be defined for data type like i,u,f, S and U)
arr_size = np.array([1, 2, 3, 4], dtype='i4')
print(arr_size)
print(arr_size.dtype)

# converting data type on existing arrays,by making a copy of the array with astypye() method which creates a copy of array
arr_ori = np.array([1.1, 2.4, 4.6, 5.5])
arr_copy = arr_ori.astype(int)
print(arr_copy)
print(arr_copy.dtype)

# change data type from integer to boolean
arr_int = np.array([1, 2, 3, 4])
arr_bool = arr_int.astype(bool)
print(arr_bool)
print(arr_bool.dtype)

# Numpy array copy as view, Copy & view
arr = np.array([2, 3, 4, 5, 6,])
arr_cop = arr.copy()
arr_cop[3] = 50  # original array doesnt get affected
arr_view = arr.view()
arr_view[2] = 40  # original array gets affected
arr[1] = 30  # wont affect on copy array but on view
print(arr)
print(arr_cop)
print(arr_view)

# getting the shape of an array using .shape
arr_shp2 = np.array(
    [[1, 2, 3, 4, ], [6, 7, 8, 9], [11, 12, 13, 14]])
arr_shp3 = np.array(
    [[[1, 2, 3, 4, ], [6, 7, 8, 9], [11, 12, 13, 14]]])
print(arr_shp2.shape)
print(arr_shp3.shape)

# creating array with 5D using ndmin using a vector with values 1,2,3,4 and verify that last dimension has value 4
arr_nd = np.array([1, 2, 3, 4], ndmin=5)
print(arr_nd)
print('shape of the array:', arr_nd.shape)

# reshaping arrays
# to change the shape of an arrar from 1D to 2D
arr_1d = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
arr_2d = arr_1d.reshape(4, 3)
arr_3d = arr_1d.reshape(2, 3, 2)
arr_3 = arr_1d.reshape(3, 2, 2)
print(arr_2d)
print(arr_3d)
print(arr_3)

# Returns copy or view
print(arr_1d.reshape(3, 4).base)  # it returns original array so it is a view

# converting 1D array with 8 elements to 3D array with 2*2 elements
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
arr_x = arr.reshape(2, 2, -1)  # cant pass -1 to more than 1D
print(arr_x)

# flattening array(means converting multidimensional array into 1D array) using reshape(-1)
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
arr_1d = arr_2d.reshape(-1)
print(arr_1d)


# Iterating Arrays
# on 1D array
arr_1 = np.array([1, 2, 3, 4])
for x in arr_1:
    print(x)

# on 2D array
arr_2 = ([[1, 2, 3, 4], [5, 6, 7, 8]])
for y in arr_2:
    print(y)

# iterating on each scalr element of 2D array
for y in arr_2:
    for z in y:
        print(z)


# iterating 3D arrays
arr_3 = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]]])
for x in arr_3:
    print(x)

# iterating on each scalr element of 3D array
for x in arr_3:
    for y in x:
        for z in y:
            print(z)
print('...................................')
# iterating arrays using nditer()
arra = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]]])
for x in np.nditer(arra):
    print(x)


# iterating array with diff data types
arr = np.array([1, 2, 3])
for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
    print(x)

# iterating with different step size
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for x in np.nditer(arr[:, ::2]):
    print(x)

arr = np.array([3, 6, 9, 12, 15, 18, 21])
print(arr[::2])

# enumerated iteration using ndenumerate (func used to create an iterator obj that provides both index and value of each element during iteration)
# on 1D array elements
arr_en = np.array([4, 8, 12])
for idx, x in np.ndenumerate(arr_en):
    print(idx, x)

# on 2D array elements
arr_2 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for idx, x in np.ndenumerate(arr_2):
    print(idx, x)
'''
