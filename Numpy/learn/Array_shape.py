
# The shape of an array is the number of elements in each dimension.
# Numpy arrays have an attribute called shape that returns a tuple with each index having the number of corresponding elements


import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

print(arr.shape)





import numpy as np

arr = np.array([1, 2, 3, 4, 5] , ndmin=5)

print("Shape of array: ", arr.shape)




shape = arr.shape

print("Data type of shape:",type(shape))

