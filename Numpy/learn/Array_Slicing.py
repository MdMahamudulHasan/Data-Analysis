
# Slicing in python means taking elements from one given index to another given index.

# we pass slice instead of index like: [ start : End ]
# we can also define the step, like this:[ start : end : step ]

# if we don't pass 'Start' its considered '0'
# if we don't pass 'End' its considered length of array in that dimension
# if we dont pass 'Step' its considered 1

import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print("Slice element index 1 to index 5 :",arr[1:5])
print("Slice element index 4 to End:",arr[4:])
print("Slice element beginning to index 4:",arr[:4])



# ------------------------------------------------------Negative Slicing----------------------------------

import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print("Using negative indexing:",arr[-2:-1])
print("Using negative indexing:",arr[-5:-1])


# ------------------------------------------------------Use Step----------------------------------

import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print("Using step 1: ",arr[ : : 1])
print("Using step 2: ",arr[ : : 2])
print("index 1 to index 5 and step 2: ",arr[1:5:2])


#----------------------------------------------------Slicing 2D arrays--------------------------------------

import numpy as np
arr = np.array([[1, 2, 3, 4, 5],[6, 7, 8, 9, 10]])

# for single dimension
print("2nd dimension:", arr[1, 1:4])
print("1st dimension:", arr[0, 1:4])
print("use step 2 in 2nd dimension:",arr[1, : : 2])
print("use step 2 in 1st dimension:",arr[0, : : 2])

# both dimension
print("2nd index element both dimension:",arr[0:2, 2])
print("index 1 to index 4 elements from both dimension: ", arr[0:2, 1:4])