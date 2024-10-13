"""

    A permutation refers to an arrangement of elements. e.g. [3, 2, 1] is a permutation of [1, 2, 3] and vice-versa.
    
    The NumPy Random module provides two methods for this: shuffle() and permutation().

    
    Shuffling Arrays
        Shuffle means changing arrangement of elements in-place. i.e. in the array itself.
    
    
"""
# shuffle() changed main array
# Randomly shuffle elements of following array:

import numpy as np
from numpy import random

arr = np.array([1, 2, 3, 4, 5])

random.shuffle(arr)

print(arr)



"""The permutation() method returns a re-arranged array (and leaves the original array un-changed)."""

import numpy as np
from numpy import random

arr = np.array([1, 2, 3, 4, 5, 6])

x = random.permutation(arr)

print(arr)
print(x)


