
"""

    Splitting is reverse operation of Joining.
    Joining merges multiple arrays into one and Splitting breaks one array into multiple.

"""

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])
new_arr = np.array_split(arr, 3)

print(new_arr)

new_arr = np.array_split(arr, 4)
print(new_arr)



# Splitting 2-D Arrays 

import numpy as np

arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
new_arr = np.array_split(arr, 3)
print(new_arr)


new_arr = np.array_split(arr, 6)
print(new_arr)


# Split the 2-D array into three 2-D arrays along rows.

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

new_arr = np.array_split(arr, 3, axis=1)

print(new_arr)


"""An alternate solution is using hsplit() opposite of hstack() """
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

new_arr = np.hsplit(arr, 3)

print(new_arr)


