import numpy as np


# Select elements at (1,0), (0,1), (1,2) and (0,0)
print(my_2d_array[[1, 0, 1, 0],[0, 1, 2, 0]])

# Select a subset of the rows and columns
print(my_2d_array[[1, 0, 1, 0]][:,[0,1,2,0]])

# Look up info on `mean` with `np.lookfor()`
#Use lookfor() to do a keyword search on docstrings.
print(np.lookfor("mean"))

# Get info on data types with `np.info()`
np.info(np.ndarray.dtype)

#you switch around the shape of the array
# Print `my_2d_array`
print(my_2d_array)

# Transpose `my_2d_array`
print(np.transpose(my_2d_array))

# Or use `T` to transpose `my_2d_array`
print(my_2d_array.T)


"""

The number of dimensions needs to be the same if you want to concatenate two arrays with np.concatenate(). 
As such, if you want to concatenate an array with my_array, which is 1-D, you’ll need to make sure that the
 second array that you have, is also 1-D.
With np.vstack(), you effortlessly combine my_array with my_2d_array. You just have to make sure that, as you’re 
stacking the arrays row-wise, that the number of columns in both arrays is the same. As such, you could also add
 an array with shape (2,4) or (3,4) to my_2d_array, 
as long as the number of columns matches. Stated differently, the arrays must have the same shape along all but 
the first axis. The same holds also for when you want to use np.r[].
For np.hstack(), you have to make sure that the number of dimensions is the same and that the number of rows in
 both arrays is the same. That means that you could stack arrays such as (2,3) or (2,4) to my_2d_array, which 
 itself as a shape of (2,4). Anything is possible as long as you make sure that the number of rows matches.
  This function is still supported by NumPy, but you should prefer np.concatenate() or np.stack().
"""
# Concatentate `my_array` and `x`
print(np.concatenate((my_array,x)))

# Stack arrays row-wise
print(np.vstack((my_array, my_2d_array)))

# Stack arrays row-wise
print(np.r_[my_resized_array, my_2d_array])

# Stack arrays horizontally
print(np.hstack((my_resized_array, my_2d_array)))

# Stack arrays column-wise
print(np.column_stack((my_resized_array, my_2d_array)))

# Stack arrays column-wise
print(np.c_[my_resized_array, my_2d_array])




# Transposing Array
i = np.transpose(b) #Permute array dimensions
i.T  #Permute array dimensions

# Changing Array Shape

b.ravel() #Flatten the array
g.reshape(3,-2) #Reshape, but don’t change data

# Adding/Removing Elements

h.resize((2,6)) #Return a new array with shape (2,6)
np.append(h,g) #Append items to an array
np.insert(a, 1, 5) #Insert items in an array
np.delete(a,[1]) #Delete items from an array

# Combining Arrays
np.concatenate((a,d),axis=0) #Concatenate arrays

np.vstack((a,b)) #Stack arrays vertically (row-wise)

np.r_[e,f] #Stack arrays vertically (row-wise)

np.hstack((e,f)) # Stack arrays horizontally (column-wise)

np.column_stack((a,d)) #Create stacked column-wise arrays

np.c_[a,d] #Create stacked column-wise arrays


# Splitting Arrays

np.hsplit(a,3) #Split the array horizontally at the 3rd index

np.vsplit(c,2) #Split the array vertically at the 2nd index
