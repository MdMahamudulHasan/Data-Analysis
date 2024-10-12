
"""
    Getting some elements out of an existing array and creating a new array out of them is called filtering.
    
    In NumPy, you filter an array using a boolean index list.
    
    
    
    A boolean index list is a list of booleans corresponding to indexes in the array.
            If the value at an index is True that element is contained in the filtered array, 
            if the value at that index is False that element is excluded from the filtered array.

"""

import numpy as np

arr = np.array([76, 41, 42, 43, 44])
x = [True, False, False, True, True]

new_arr = arr[x]
print(new_arr)


#------------------------------------------------Creating the Filter Array---------------------------------------------

# Create a filter array that will return only values higher than 42:
import numpy as np

arr = np.array([41, 42, 40, 43, 44])

filter_arr = []

for element in arr:
    if element > 42:
        filter_arr.append(True)
    else:
        filter_arr.append(False)

new_arr = arr[filter_arr]
print(filter_arr)
print(new_arr)




# Create a filter array that will return only even elements from the original array:

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

filter_arr = []

for element in arr:
    if element % 2 == 0:
        filter_arr.append(True)
    else:
        filter_arr.append(False)

new_arr = arr[filter_arr]
print(filter_arr)
print(new_arr)



#------------------------Creating Filter Directly From Array-----------------------------------------

"""The above example is quite a common task in NumPy and NumPy provides a nice way to tackle it."""



# Create a filter array that will return only values higher than 42:

import numpy as np

arr = np.array([41, 42, 43, 44])
filter_arr = arr > 42

new_arr = arr[filter_arr]

print(filter_arr)
print(new_arr)



# Create a filter array that will return only even elements from the original array:

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

filter_arr = arr % 2 == 0

new_arr = arr[filter_arr]

print(filter_arr)
print(new_arr)