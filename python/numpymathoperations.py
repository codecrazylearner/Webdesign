import numpy as np

twod_array=np.array([[-4, -3, -2, -1],
            [2, 4, 6, 8]])
ford_array=np.array([[1., 2., 3., 4.],
                     [5., 6., 7., 8.],
                     [9, 10., 11., 12.],
                     [13, 14., 15., 16.]])
oned_array=([1, 2, 3, 4])

print(twod_array.shape)
print(twod_array.ndim)

diagonal1_array=np.diag(twod_array)

diagonal2_array=np.diag(np.array([1, 2, 3, 4]))
print("Diagonal of a 2-D array :\n" , diagonal1_array)
print("Diagonal of a 1-D array :\n" ,diagonal2_array)
print("Datatype of a Numpy array : \n" , ford_array.dtype)
print("Diagonal of 4-D arraay : \n" , np.diag(ford_array))

#array is largge numpy skips central part and only prints the corners
print(np.arange(10000))
print(np.arange(10000).reshape(100,100))

#to disable this and force numpyt to print the entire array we use set_printoptions
np.set_printoptions(threshold=np.nan)

combined_array = np.arange(6) + np.arange(0,51,10)
print(combined_array)# combines both arrays and then spaces out evenly the numbers

basic_array = np.array([20, 30, 40, 50])
print(basic_array < 35)

print("sin array :\n ", 10*np.sin(basic_array))

add_array = oned_array + oned_array
multi1_array = twod_array * twod_array
multi2_array = twod_array ** 5
subtract1_array = multi1_array - twod_array
subtract2_array = twod_array - twod_array

add_an_array = np.add(oned_array , twod_array)
divide_array = np.divide( twod_array ,  oned_array)
divided_array = 1 / twod_array

print("Add array: \n" , add_array, add_an_array)
print("multiply_array :  \n " , multi1_array , multi2_array)
print("Subtract array : \n ", subtract1_array , subtract2_array)
print("Array Division : \n  " , divide_array , divided_array)

a = np.ones((2,3), dtype=int)
b = np.random.random((2,3))
a *= 3
b += a
a += b                  # b is not automatically converted to integer type

a = np.ones(3, dtype=np.int32)
b = np.linspace(0,pi,3)
print(b.dtype.name)
c = a + b

d = np.exp(c*1j)
print(c.dtype.name)
print(d.type.name)



