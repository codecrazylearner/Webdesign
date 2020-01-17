import numpy as np

arrange_array = np.arange(0, 20)  # create an evenly spaced values
print("Original arrange array : \n", arrange_array)

index_array = arrange_array[0:8] # slice only first 8 elements of an array

arrange_array[0:10] = 20  # assign the first 10 elements to a value
print("New arranged array : \n", arrange_array)

index_array[:] = 30  # assign all the elements to 30
print("Changed index array : \n", index_array)

#deep copy results of the arrays


copied_array = arrange_array.copy()  # deep copy of the array
print("copied array : \n", copied_array)

copy_array = np.copy(arrange_array)  # copy of the array
print("copy of the array : \n", copy_array)

print(copied_array is arrange_array)

print(copied_array.base is arrange_array) #copied array doesnt share anything with arrrange_array

#copy can be called after slicing if original array is not required anymore
a = np.arange(int(1e8))
b = a[:100].copy()
del a # memory of 'a' can be released

array_len = copied_array.shape[0]
print("Array length of 2d: \n", array_len)



#view or shallow copy results on array
view_array = arrange_array.view()  # A shallow or view copy of the array with same data
print("the view of the array : \n", view_array)

#creates new array object that looks at the same data
print(view_array is arrange_array)
print(view_array.base is arrange_array) #view_array is a view ofthe data owned by arrange_array

view_array.shape = ( 2, 6)#arrange_array shape doesnT change
print(arrange_array.shape)

view_array[0, 4] = 1234 #arrange_Array data changes

sort_arrays = arrange_array.sort()  # sort the arrays
print("Sorted arrays : \n", sort_arrays)

sxaxis_array = copy_array.sort(axis=0)  # sort elements of an arrays axis
print("sort x axis : \n ", sxaxis_array)

array_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("array 2d  : \n", array_2d)
print("array 2d with select elements : \n", array_2d[1][2])

sliced_array = array_2d[0:2, 0:2]  # sliced of 2d array
print("sliced array : \n ", sliced_array)

slice_array = array_2d[: :-1]# reversed array_2d
print("reversed array : \n", slice_array)

array_2d[:2, 1:] = 15
print(" Modified array 2d : \ n", array_2d)


for i in range(array_len):  # using loops to index
    array_2d = i
print("Modified again array 2d: \n ", array_2d)

# more than one way of accessing rows of an array
print("array2d some elements: \n")
print(array_2d[[0, 1]])

print("array2d some elements: \n")
print(array_2d[[1, 0]])

#iteration of arrays
a = np.arange(10)**2

for i in a:
    print(i**(1/3.))
for i in a.flat:
    print(i) #flat attribute which is an iterator over all the elements of array

# Select the element at the 1st index
print(my_array[1])

# Select the element at row 1 column 2
print(my_2d_array[1][2])

# Select the element at row 1 column 2
print(my_2d_array[1,2])

# Select the element at row 1, column 2 and
print(my_3d_array[1,1,2])

#Subsetting

a[2] #Select the element at the 2nd index 3
b[1,2] #Select the element at row 1 column 2


 #Slicing
a[0:2] #Select items at index 0 and 1

b[0:2,1] #Select items at rows 0 and 1 in column 1


b[:1] #Select all items at row 0
# array([[1.5, 2., 3.]]) (equivalent to b[0:1, :])
c[1,...] #Same as [1,:,:]


a[ : :-1] #Reversed array a
a[a<2] #Select elements from a less than 2

# Fancy Indexing
b[[1, 0, 1, 0],[0, 1, 2, 0]] #Select elements (1,0),(0,1),(1,2) and (0,0)

b[[1, 0, 1, 0]][:,[0,1,2,0]] #Select a subset of the matrix’s rows



