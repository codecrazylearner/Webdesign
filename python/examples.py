import numpy as np
import matplotlib.pyplot as plt

array = np.arange(20)
print(array)

# BASIC CHARACTERISTICS OF THE ARRAYS
# Make the array 'my_array'
my_arrays = np.array([[1, 2, 3, 4], [5, 6, 7, 8]], dtype=np.int64)

my_array = my_arrays

# Print `my_array with type array, size, shape, dim, dtype , itemsize
print("my_array  \n ", my_array)
print("my_array type : \n", type(my_array))
print("my_array shape  :  \n", my_array.shape)
print("my_array dimensions :  \n", my_array.ndim)
print("my_array dytpe : \n", my_array.dtype)
print("my_array length of one array element in bytes :  \n", my_array.itemsize)
print("info of my_array memory layout:  \n", my_array.flags)
print("total consumed bytes of my_array's elements: \n ", my_array.nbytes)

# NUMPY FUNCTIONS TO CREATE ALL DIFFERENT KINDS OF ARRAYS:

print("\n\nNUMPY FUNCTIONS TO CREATE ALL DIFFERENT KINDS OF ARRAYS \n")

# create an array of given shape and type, filled with ones
print("Ones array:  \n", np.ones((3, 4), dtype=np.int32, order='C'))

# create an array of given shape and type,filled with zeros and order C or F
print("Zeros array: \n", np.zeros((2, 3, 4), dtype=np.int16, order='F'))

# create n array with random values of the given shape and type
print("Array with random values:  \n", np.random.random((2, 2)))

# create an empty array with given shape and type, without initializing entries
print("Empty array :  \n", np.empty((3, 2)))

# create an array with given shape and type , filled with fill_value
print("Full array:  \n", np.full((2, 2), 7))

# create an array with ones on the diagonal and zeros elsewhere
print("array using eye function: \n", np.eye(2, 2))

# print the identity array that is almost an equivalent function as eye
print("identity array : \n ", np.identity(3))

# BASIC OPERATIONS USING ELEMENT-WISE, UNARY, BINARY OPERATORS AND UNIVERSAL FUNCTIONS

an_array = np.array([1, 2, 3, 5])
a = np.array([4, 5, 10, 12])

# array operations on single array(elementwise operations)
print("original element-wise array :  \n", an_array)
print("Added array :  \n", an_array + 1)
print("Subtracted array :  \n", an_array - 1)
print("Multiplied array:  \n", an_array * 12)
print("Squared array :  \n", an_array ** 4)
print("Divided array with floor divison:  \n", an_array // 2)
print("Divided array with true division:  \n", an_array / 2)

# Array operations using overlodaed operators
print("Original scalar array a: \n ", a)
a += 4
print("Scalar addition using += : \n", a)
a -= 2
print("Scalar subtraction using -= : \n", a)
a *= 2
print("Scalar multiplication using  *= :\n", a)
a //= 2
print("Scalar division using //= :\n", a)

# Array operations using binary operators

b = np.array([[1, 2],
              [3, 4]])
c = np.array([[4, 3],
              [2, 1]])

print("Original array b and c: \n ", b, c)
print("Addition using binary operators:  \n", b + c)
print("Subtraction using binary operators:  \n", b - c)
print("Multiplication using binary operators:  \n", b * c)
print("Matrix multiplication:  \n", b.dot(c))

# All the operations we did above using overloaded operators can be done using
# ufuncs  like np.add, np.subtract, np.multiply, np.divide, np.sum, etc.


# ARRAYS USING SORTING FUNCTIONS AND TRIGONOMETRIC FUNCTIONS)


# create an array of sine values
a = np.array([0, np.pi / 2, np.pi])
print("Sine values of array elements:", np.sin(a))

# exponential values
a = np.array([0, 1, 2, 3])
print("Exponent of array elements:", np.exp(a))

# square root of array values
print("Square root of array elements:", np.sqrt(a))

# create an array of log values

in_array = [1, 3, 5, 2 ** 8]
print("Input array : ", in_array)

out_array = np.log(in_array)
print("Output array : ", out_array)

print("\nnp.log(4**4) : ", np.log(4 ** 4))
print("np.log(2**8) : ", np.log(2 ** 8))

# sorting the array row-wise,colum-wise,sort algorithm etc
a = np.array([[1, 4, 2],
              [3, 4, 6],
              [0, -1, 5]])

print("Original array to be sorted :\n ", a)

# sort array row-wise
print("Row-wise sorted array:\n", np.sort(a, axis=1))

# specify sort algorithm
print("Column wise sort by applying merge-sort:\n",
      np.sort(a, axis=0, kind='mergesort'))

# Example to show sorting of structured array
# set alias names for dtypes
dtypes = [('name', 'S10'), ('grad_year', int), ('gpa', float)]

# Values to be put in array
values = [('Sara', 2009, 4, 0), ('Bob', 2008, 3.5),
          ('Michael', 2008, 3.85), ('lizzy', 2009, 3.9)]

# Creating array
arr = np.array(values, dtype=dtype)
print("\nArray sorted by names:\n",
      np.sort(arr, order='name'))

print("Array sorted by graduation year, gpa:\n",
      np.sort(arr, order=['grad_year', 'gpa']))

# NUMPY FUNCTIONS FOR APPENDING ARRAYS BY INSERTING,DELETING,JOINING,
# SPLITTING,CHANGING SHAPE AND CONVERTING ARRAY TO A DIFFERENT TYPE

my_array = np.array([[1, 2, 3, 4], [5, 6, 7, 8]], dtype=np.int64)
my_2d_array = my_array
new_array = np.append(my_array, [7, 8, 9, 10])
new_2darray = np.append(my_2d_array, [[7], [8]], axis=1)

# you switch around the shape of the array
# Print `my_2d_array`
print(my_2d_array)

# print the inserted element in my_array
np.insert(my_array, 1, 5)
print("Array after inserting: \n", my_array)

# print the deleted element in my array
np.delete(my_array, [1])
print("Array after deleting an element:  \n", my_array)

# Select elements at (1,0), (0,1), (1,2) and (0,0)
print("Elements at(1,0), (0,1), (1,2) and (0,0) of my_2d_array :\n",
      my_2d_array[[1, 0, 1, 0], [0, 1, 2, 0]])

# Select a subset of the rows and columns
print("Subset of my_2d_array : \n",
      my_2d_array[[1, 0, 1, 0]][:, [0, 1, 2, 0]])

# ARRAY INDEXING
index_array = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
index2_array = np.arange(0, 12)
copied_array = index_array.copy()

print("The original array :\n", index_array)
print(" the copied array :\n", copied_array)

sliced_array = index_array[0:2, 0:2]  # sliced of 2d array
print("First 2 rows and cols array : \n ", sliced_array)

slice_array = index_array[::-1]  # reversed index_array
print("reversed array : \n", slice_array)

index_array[:2, 1:] = 15
print(" first 2 rows and from col 1 : \ n", index_array)

# index2_array[0:5] = 20
print("first five elements: \n", index2_array)

print("Elements from 2 to 8:\n", index2_array[2:8])  # slice only first 8 elements of an array

index2_array[0:10] = 20  # assign the first 10 elements to a value
print("first 10 elements array : \n", index2_array)

arrange_array = index2_array[0:6]
print("New sliced arrange array: \n", arrange_array)

arrange_array[:] = 30  # assign all the elements to 30
print("Changed arrange array : \n", arrange_array)
print("Index array:\n ", index2_array)

#FANCY INDEXING
alt_array = index_array[:2, ::2]
print("Slices first 2 rows and alternate 0 and 2 cols: \n", alt_array)

indices_array = index_array[[0, 1, 2, 3],[3, 2, 1, 0]]
print("elements at indices(0,3),(1,2),(2,1),(3,0) :\n", indices_array)

subset_array = index_array[[1, 0, 1, 0]][:,[0, 1, 2, 0]]
print("Subset of the index_array :\n", subset_array)

#CONDITIONAL AND BOOLEAN OPERATIONS
condit = index_array > 0
condit_array = index_array[condit]
print("Conditional array :\n ", condit_array)
# CONCATENATE AN ARRAY
# The number of dimensions needs to be the same when using np.concatenate()

# Concatentate `my_array` and `x`
x = np.ones((3, 4))
print(np.concatenate((my_array, x)))

# DIFFERENT WAYS TO JOIN ARRAYS
# Stack arrays row-wise making sure the number of columns in both arrays are the same
# and arrays must have the same shape along all but the first axis
#  applies to both with vstack() and np.r_.

print(np.vstack((my_array, my_2d_array)))
print(np.r_[my_resized_array, my_2d_array])

# Stack arrays horizontally making sure number of dimensions and
# # the number of rows in both arrays are the same
print(np.hstack((my_resized_array, my_2d_array)))

# Stack arrays column-wise
print(np.column_stack((my_resized_array, my_2d_array)))
print(np.c_[my_resized_array, my_2d_array])

# SPLIT THE ARRAYS'

# Split `my_stacked_array` horizontally at the 2nd index
print(np.hsplit(my_stacked_array, 2))

# Split `my_stacked_array` vertically at the 2nd index
print(np.vsplit(my_stacked_array, 3))

# NUMPY BROADCASTING

# Initialize `x`
x = np.ones((3, 4))
# Check shape of `x`
print(x.shape)

# Adding compatible and equal arrays using broadcasting
# Initialize `y`
y = np.random.random((3, 4))
# Check shape of `y`
print(y.shape)
# Add `x` and `y`
print("Adding compatible arrays using broadcasting:  \n", x + y)

# Subtracting 2 arrays, when one array is 1D as  they are considered compatible
# Initialize `y`
y = np.arange(4)
# Check shape of `y`
print(y.shape)
# Subtract `x` and `y`
print("Subtraction when one is 1D array using brodcasting : \n",
      x - y)

# Addition of arrays is possible when the size of element of one array is 1
# Initialize `x` and `y`
x = np.ones((3, 4))
y = np.random.random((5, 1, 4))
# Add `x` and `y`
# x has dimension 3x4 and y has size 1, so x has size 3 and x behaves as if it were copied along the dimension and the result is (5,3,4)
print(x + y)

# CHANGING ARRAY SHAPE AND SIZE WHEN BROADCASTING CAN'T BE DONE
# returns evenly spaced numbers over a specified interval.
# num is the number of samples to generate.

print("Change array space using linspace  :\n", np.linspace(0, 10, num=4))

# FLATTEN AND RAVEL IS USED TO CHANGE nD TO 1-D ARRAY

# returns a copy of the array collapsed into one dimensional

my_stacked_array = np.array([[5, 6, 7, 8],
                             [10, 11, 12, 13],
                             [15, 16, 17, 18]])
# Flatten returns copy of otiginal array, original doesn't change after modified,
# slower and occupies memory and is a method
print("Flatten array: \n", my_stacked_array.flatten())

# Ravel returns reference of the array, original changes when modified,
# library level function which is faser and does not occupy memory
print("Using ravel array : \n ", my_stacked_array.ravel())

# Making a random array
ran_array = np.array([1, 2, 3, 4, 5, 6])

# Required values 12, existing values 6
ran_array.resize(3, 4)
print("Resized 1-D array : \n", ran_array)

# Making a random array
x = np.array([1, 2, 3, 4, 5, 6],
             [20, 30, 40, 50, 60, 70])

# Resize the array permanently
x.resize(2, 3)

print("Resized array : \n", x)

# reshape with new dimensions and if new array is larger than the original
# , the new array filled with copies of the original array.

print("Copies of original array as the new array is large: \n",
      x.resize(6, 4))

# new array filled with zeros
print("Array filled with zeros: \n", np.resize())

# RESHAPING THE ARRAY WITHOUT CHANGING THE DATA
# Reshape, but don’t change data
print("Reshape without changing data:  \n", x.reshape(3, -2))

# convert an array to a different type
print("Convert the array into different type: ", my_array.astype(int))

# TRANSPOSING ARRAY

# Transpose `x`
print("Array using transpose : \n", np.transpose(x))

# Or use `T` to transpose `my_2d_array`
print("Array using .T option to transpose :\n ", x.T)

# Use lookfor() to do a keyword search on docstrings.
# Look up info on `mean` with `np.lookfor()`

print(np.lookfor("mean"))
# Get info on data types with `np.info()`
print(np.info(np.x.dtype))

# Initialize your array
my_3d_array = np.array([[[1, 2, 3, 4],
                         [5, 6, 7, 8]],
                        [[1, 2, 3, 4],
                         [9, 10, 11, 12]]], dtype=np.int64)

# Pass the array to `np.histogram()`
# histogram computes the occurrences of the array that fall within each
# bin which determines the area that each bar of your histogram takes up

print(np.histogram(my_3d_array))

# Specify the number of bins
print(np.histogram(my_3d_array, bins=range(0, 13)))

# construct the histogram with aflattened 3d array and  range of bins
plt.hist(my_3d_array.ravel(), bins=range(0, 13))

# Add a title to the plot

plt.title("Frequency of my 3-D array elements")
plt.show()
points = np.arange(-5, 5, 0.01)

# make  a meshgrid
xs, ys = np.meshgrid(points, points)
z = np.sqrt(xs ** 2 + ys ** 2)

# display the image on the axes
plt.imshow(z, cmap=plt.cm.gray)

# draw a color bar
plt.colorbar()
plt.show()

axes_values = np.arange(-100, 100, 10)
dx, dy = np.meshgrid(axes_values, axes_values)

print("dx: ", dx)
print("dy", dy)

function1 = 2 * dx + 3 * dy
function2 = np.cos(dx) + np.cos(dy)

print("2dx+3dy : ", function1)
print("cos(dx)+cos(dy) :", function2)

# replace function2 by function1 to get graph of function1
# plotting the function on graph
plt.imshow(function2)
plt.title("function cos plot")
plt.colorbar()
plt.savefig('myfig2.png')
