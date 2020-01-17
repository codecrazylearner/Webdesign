import numpy as np

my_list1 = np.array((1, 2, 3))
my_list2 = np.array([(1.5, 2, 3), (4, 5, 6)], dtype=float)
complex_arr = np.array([1, 2, 3], dtype=complex)
my_array = my_list1


print(numpy.ones((2, 2), dtype=bool))
print(np.int64(my_list1))
print(np.float32(my_list2))
print(np.complex(complex_arr))  #Complex numbers represented by 128 floats
 #Boolean type storing TRUE and FALSE values
#np.object # Python object type
#np.string_# Fixed-length string type
#np.unicode_ #Fixed-length unicode type

print("The first list is : \n", my_list1)
print("The second list is:", my_list2)
print("The array copy and original memory id is:\n",
      id(my_list1), id(my_array))
print("the copy of list_1 is :\n", my_array)

dim2_array = my_array.dtype.name
print("Array data type : \n " , my_array.dtype)
print("Array data type name : \n ", dim2_array)
print("size of the array: \n", my_array.size)
#convert an array to a different type
print("Convert into different type: ", my_array.astype(int))


zero_array = np.zeros((5, 6))
ones_array = np.ones((3, 5), dtype=np.int16)
id_array = np.eye(5)
shapes_array = my_list1.shape
dimension_array = my_array.ndim


print("Numpy zero array is: \n", zero_array)
print("Numpy ones array is :\n", ones_array)
print("Numpy identical array is :\n", id_array)
print("Numpy shape array is : \n", shapes_array)
print("Numpy ndimesion array is: \n", dimension_array)

empty_array = np.empty((3, 2))
full_array = np.full((2, 2), 7)
space_array = np.linspace(0, 2, 9)
large_array = np.linspace(0,2,15,endpoint=True)
rand_value_array = np.random.random((2, 2))

print("Numpy empty array is :\n ", empty_array)
print("Numpy full array is :\n", full_array)
print("Numpy linspace array is :\n", space_array)
print("Numpy linspace array is : \n", large_array)
print("Numpy random array is :\n", rand_value_array)

arrange_array = np.arange(10,25,5)
print("Numpy array of evenly spaced values :\n" , arrange_array)


# Print the number of `my_array`'s dimensions
print(my_array.ndim)

# Print the number of `my_array`'s elements
print(my_array.size)

# Print information about `my_array`'s memory layout
print(my_array.flags)

# Print the length of one array element in bytes
print(my_array.itemsize)

# Print the total consumed bytes by `my_array`'s elements
print(my_array.nbytes)
"""
Before you go deeper into scientific computing, it might be a good idea to first go over what broadcasting exactly is: it’s a mechanism that allows NumPy to work with arrays of different shapes when you’re performing arithmetic operations.

To put it in a more practical context, you often have an array that’s somewhat larger and another one that’s slightly smaller. Ideally, you want to use the smaller array multiple times to perform an operation (such as a sum, multiplication, etc.) on the larger array.

To do this, you use the broadcasting mechanism.

"""

# Initialize `x`
x = np.ones((3,4))

# Check shape of `x`
print(x.shape)

# Initialize `y`
y = np.random.random((3,4))

# Check shape of `y`
print(y.shape)

# Add `x` and `y`
x + y

#Two dimensions are also compatible when one of them is 1:

# Initialize `x`
x = np.ones((3,4))

# Check shape of `x`
print(x.shape)

# Initialize `y`
y = np.arange(4)

# Check shape of `y`
print(y.shape)

# Subtract `x` and `y`
x - y

# Lastly, the arrays can only be broadcast together if they are compatible in all dimensions.


# Initialize `x` and `y`
x = np.ones((3,4))
y = np.random.random((5,1,4))

# Add `x` and `y`
x + y