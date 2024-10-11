
"""

    The main difference between a copy and a view of an array is that:
    
        -> the copy is a new array.
        -> the view is just a view of the original array.
        
        -> The copy owns the data and any changes made to the copy will not affect original array.
        -> any changes made to the original array will not affect the copy.
        

"""


#-------------------------------------------------Copy----------------------------------------------

import numpy as np 
arr = np.array([1, 2, 3, 4, 5, 6])
x = arr.copy()

print("Original Array: ",arr)
print("Copy Array: ",x)


# After changes in array element
arr [0] = 42
print("Original Array: ",arr)
print("Copy Array: ", x)


#-------------------------------------------------View----------------------------------------------


import numpy as np 
arr = np.array([1, 2, 3, 4, 5, 6])
x = arr.view()

print("Original Array: ",arr)
print("Copy Array: ",x)


# After changes in array element
arr [0] = 42
print("Original Array: ",arr)
print("Copy Array: ", x)



#-------------------------------------------Check if Array Owns its Data---------------------------------
#-------------------------------------------------------------------------------------------------------------------


"""

    Every NumPy array has the attribute base that returns None if the array owns the data.

    Otherwise, the base  attribute refers to the original object.

"""

import numpy as np
arr = np.array([1, 2, 3, 4, 5])

x = arr.copy()
y = arr.view()

print(x)
print(y)
print(x.base)
print(y.base)


# after change the array element
arr = np.array([1, 2, 3, 400, 5])

print(x)
print(y)
print(x.base)
print(y.base)

# The copy returns None.
# The view returns the original array.