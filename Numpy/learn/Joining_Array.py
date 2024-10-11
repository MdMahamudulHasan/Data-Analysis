"""

    Joining means putting contents of two or more arrays in a single array.
    In SQL we join tables based on a key, Whereas in NumPy we join arrays by axes.
    
    We pass a sequence of arrays that we want to join to the 'concatenate()' function, along with the axis.
    If axis is not explicitly passed, it is taken as 0.

"""

# Join two arrays

import numpy as np

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])

arr = np.concatenate((arr1, arr2))
print(arr)



# For 2-D array

import numpy as np

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

arr = np.concatenate((arr1, arr2), axis=1)
print(arr)




#------------------------------------------------Joining Arrays Using Stack Functions---------------------------------------

"""

    Stacking is same as concatenation, the only difference is that stacking is done along a new axis.
    
    We pass a sequence of arrays that we want to join to the stack() method along with the axis. If axis is not explicitly passed it is taken as 0.
    
"""

import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

arr = np.stack((arr1, arr2))

print("Without axis:")
print(arr)

arr = np.stack((arr1, arr2), axis=1)

print("With axis:")
print(arr)



#------------------------------------------------Stacking Along Rows---------------------------------------


"""NumPy provides a helper function: hstack() to stack along rows."""

import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

arr = np.hstack((arr1, arr2))
print(arr)


#------------------------------------------------Stacking Along Columns---------------------------------------


"""NumPy provides a helper function: vstack() to stack along Columns."""


import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

arr = np.vstack((arr1, arr2))
print(arr)



#------------------------------------------------Stacking Along Height (depth)---------------------------------------


"""NumPy provides a helper function: vstack() to stack along height, which"""


import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

arr = np.dstack((arr1, arr2))
print(arr)


