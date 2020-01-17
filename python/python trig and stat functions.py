import numpy as np


#unary operations on the array
trig_arr = [[1, 2, 3, 4],
            [5, 6, 7, 8]]
staat_arr = [[True, False, True]]
comp_arr = [[False, True, True]]

apower =  np.arange(10)**3
a = np.random.random((2,3))
b = np.arange(12).reshape(3,4)

expo_array = np.exp(trig_arr)
sqrt_array = np.sqrt(trig_arr)
sin_array = np.sin(trig_arr)
cos_array = np.cos(trig_arr)
log_array = np.log(trig_arr)
max_array = np.maximum(trig_arr)
dot_array=trig_arr.dot()
sums_array = trig_arr.sum(axis=0) #sum of each column
mins_array = trig_arr.min(axis=1) #min of each row
maxs_array = trig_arr.max()
cumsum_array = trig_arr.cumsum(axis=1) #cumculative sum along each row
means_array = trig_arr.mean()
medians_array = trig_arr.median()
coeff_array = trig_arr.scorrcoef()
deviate_array = np.std(trig_arr)

A = np.array( [[1,1],
            [0,1]] )
B = np.array( [[2,0], [3,4]] )
print( "Elementwise matrix : \n", A * B )                      # elementwise product

print("Matrix product :  \n", A @ B )                      # matrix product

print("matric product : \n",A.dot(B))                    # another matrix product

print(staat_arr == comp_arr)

print(staat_arr < 10)
equal_array = np.array_equal[staat_arr, comp_arr]










