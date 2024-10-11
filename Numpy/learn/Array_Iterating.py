"""

    Iterating means going through elements one by one.

"""


import numpy as np

arr = np.array([1, 2, 3])

print("Normal print:",arr)

print("Using Iterating:")

for x in arr:
    print(x)




#----------------------------------------------Iterating for 2-D Arrays-------------------------------------------


#Iterate on the elements of the following 2-D array:

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
    print(x)




# Iterate on each scalar element of the 2-D array:

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
    for y in x:
        print(y)





#----------------------------------------------Iterating for 3-D Arrays-----------------------------------------


# In a 3-D array it will go through all the 2-D arrays.

import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print("Iterate on the elements of the following 3-D array:")

for x in arr:
    print(x)


print("After using two loop:")

for x in arr:
    for y in x:
        print(y)
        

print("Iterate down to the scalars:")

for x in arr:
    for y in x:
        for z in y:
            print(z)


#----------------------------------------------Iterating Arrays Using nditer()-----------------------------------------

"""

    The function nditer() is a helping function that can be used from very basic to very advanced iterations. 
    It solves some basic issues which we face in iteration, lets go through it with examples.

"""

import numpy as np 

arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

print("Using nditer:")

for x in np.nditer(arr):
    print(x)
    



#----------------------------------------------Iterating With Different Step Size-----------------------------------------


import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for x in np.nditer(arr[:, ::2]):
    print(x)
    
    
    
    
#----------------------------------------------Enumerated Iteration Using ndenumerate()-----------------------------------------


"""
    Enumeration means mentioning sequence number  of somethings one by one.
    
    Sometimes we require corresponding index of the element while iterating, the ndenumerate() method can be used for those usecases.
    
"""

# Enumerate on following 1D arrays elements:

import numpy as np

arr = np.array([1, 2, 3])

for x in np.ndenumerate(arr):
    print(x)

for idx, x in np.ndenumerate(arr):
    print(idx, x)



# Enumerate on following 1D arrays elements:

import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for idx, x in np.ndenumerate(arr):
    print(idx, x)
    
    
    