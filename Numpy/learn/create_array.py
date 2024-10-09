
# NumPy is used to work with arrays. The array object in Numpy is called ndarray.

# We can create a NumPy ndarray object by using the array() function.

import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))


import numpy as np

arr = np.array((1,2,3,4,5))
print(arr)
print(type(arr))



# ------------------------------ 0 D Arrays-------------------

import numpy as np

arr = np.array(42)
print(arr)



#----------------------------------------- 1D Arrays----------------------------------------

import numpy as np

arr = np.array([3, 5,2,9,5])
print(arr)
print(type(arr))


# ----------------------------------------- 2D Arrays-----------------------------------------

import numpy as np

arr = np.array([[1, 2, 3,], [4, 5, 6,]])
print(arr)


arr = np.array([[1, 3, 5], [2, 4, 6]])
print(arr)


# if you get 1 missing value in any dimension it will show error

# arr = np.array([[1, 2, 3], [4, 5]])
# print(arr)



#-------------------------------------------- 3D Arrays---------------------------------------

import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]],  [[1, 2, 3], [4, 5, 6]]])
print(arr)




# ----------------------------------------------------Check Number of Dimension--------------------------------------


import numpy as np

a = np.array(42) # 0 Dimension
b = np.array([1, 3, 4, 5, 6]) # 1 Dimension
c = np.array([[1, 2, 3], [4, 5, 6]]) # 2 Dimension
d = np.array([[[1, 2, 3], [4, 5, 6]],  [[1, 2, 3], [4, 5, 6]]]) # 3 Dimension

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

