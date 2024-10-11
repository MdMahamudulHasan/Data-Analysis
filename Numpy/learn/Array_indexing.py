
# Array indexing is the same as accessing an array element.

# You can access an array element by referring to its index number.


# -------------  Access 1D Arrays Element---------------------------

import numpy as np
arr = np.array([1, 2, 3, 4])
print(arr[0])
print(arr[2])
print(arr[1:2])
print(arr[1] + arr[2])


# -------------  Access 2D Arrays Element---------------------------


import numpy as np

arr = np.array([[1, 2, 3, 4, 5],[6, 7, 8, 9, 10]])
print("2nd element of 1st row:", arr[0,1])
print("4th element of 1st row:", arr[0,4])

print("2nd element of 2nd row:",arr[1,1])
print("4th element of 2nd row:",arr[1,4])



# -------------  Access 3D Arrays Element---------------------------

import numpy as np
arr = np.array([[[1, 2, 3],[4, 5, 6]],[[7, 8, 9],[10,11, 12]]])
print(arr[0, 1, 2])
# output = 6


"""

    arr[0, 1, 2] print value 6
    
    The first number represents the first dimension
    1st dimension = [[1, 2, 3],[4, 5, 6]]
    2nd dimension = [[7, 8, 9],[10,11, 12]]
    
    The second number represents the 2nd dimension
    1st dimension = [1, 2, 3]
    2nd dimension = [4, 5, 6]
    
    The third number represents 3 No element
    index 0 = 4 = 1st element
    index 1 = 5 = 2nd element
    index 2 = 6 = 3rd element
    
    
"""



# ---------------------------- Negative Indexing  -----------------------------

import numpy as np

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print("Last element from 2nd row:",arr[1,-1])
print("Last element from 1st row:",arr[0,-1])
