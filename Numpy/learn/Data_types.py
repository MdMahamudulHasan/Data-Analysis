
"""
Data Types in Python:

    By default Python have these data types:

        strings - used to represent text data. "ABCD"
        integer - used to represent integer numbers. -1, -2, -3
        float - used to represent real numbers. 1.2, 42.42
        boolean - used to represent True or False. 0, 1
        complex - used to represent complex numbers. 1.0 + 2.0j, 1.5 + 2.5j


Data Types in NumPy:

    NumPy has some extra data types, and refer to data types with one character.
    Below is a list of all data types in NumPy and the characters used to represent them.

        i - integer
        b - boolean
        u - unsigned integer
        f - float
        c - complex float
        m - timedelta
        M - datetime
        O - object
        S - string
        U - unicode string
        V - fixed chunk of memory for other type ( void )


"""


#--------------------------------------------Checking the Data Type of an Array----------------------------------------

import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print("Data type of array:",arr.dtype)


import numpy as np
arr = np.array(["Apple", "Banana", "Cherry"])
print("Data type of array:",arr.dtype)



#-----------------------------------------Creating Arrays With a Defined Data Type----------------------------------------

import numpy as np

arr = np.array([1, 2, 3, 4 ,5], dtype='S')
print(arr)
print(arr.dtype)

# For i, u, f, S and U we can define size as well.

import numpy as np
arr = np.array([1, 2, 3, 4, 5], dtype='i4')
print(arr)
print(arr.dtype)

import numpy as np
arr = np.array([1, 2, 3, 4, 5], dtype='i8')
print(arr)
print(arr.dtype)





#-------------------------------------------Creating Arrays With a Defined DataType---------------------------------
#-------------------------------------------------------------------------------------------------------------------



"""
    The best way to change the data type of an existing array, is to make a copy of the array with the astype() method.
    
    The astype() function creates a copy of the array, and allows you to specify the data type as a parameter.
    
"""

import numpy as np

arr = np.array([1.1 , 2.1, 3.1])

new_Array = arr.astype('i')
print(new_Array)
print(new_Array.dtype)


new_Array = arr.astype('i8')
print(new_Array)
print(new_Array.dtype)

new_Array = arr.astype('S')
print(new_Array)
print(new_Array.dtype)


new_Array = arr.astype(int)
print(new_Array)
print(new_Array.dtype)


arr = np.array([-1 , 0, 3])
new_Array = arr.astype(bool)
print(new_Array)
print(new_Array.dtype)

