"""

    Reshaping means changing the shape of an array.

    The shape of an array is the number of elements in each dimension.

    By reshaping we can add or remove dimensions or change number of elements in each dimension.

"""


# ----------------------------------------------Reshape From 1-D to 2-D---------------------------------------------

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

new_arr = arr.reshape(4,3)

print("4 arrays with 3 elements:",new_arr)


new_arr1 = arr.reshape(3, 4)

print("3 arrays with 4 elements:", new_arr1)


# ----------------------------------------------Reshape From 1-D to 3-D---------------------------------------------



import numpy as np
#The outermost dimension will have 2 arrays that contains 3 arrays, each with 2 elements
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

new_arr = arr.reshape(2, 3, 2)

print(new_arr)

new_arr = arr.reshape(3, 2, 2)

print(new_arr)






import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

new_arr = arr.reshape(2, 4)

print(new_arr.base)




# ----------------------------------------------Unknown Dimension---------------------------------------------
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

new_arr = arr.reshape(2, 2, -1)

print(new_arr)



# ----------------------------------------------Flattening the arrays---------------------------------------------


import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

new_arr = arr.reshape(-1)

print(new_arr)

