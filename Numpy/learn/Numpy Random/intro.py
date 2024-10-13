


"""
    What is a Random Number?
    
    Random number does NOT mean a different number every time. Random means something that can not be predicted logically.
    
    Pseudo Random and True Random.
        If there is a program to generate random number it can be predicted, thus it is not truly random.
        
        Random numbers generated through a generation algorithm are called pseudo random.

"""


# -------------------------------------Generate Random Number--------------------------------------


# Generate a random integer from 0 to 100:
from numpy import random

x = random.randint(100)

print(x)


# Generate a random float from 0 to 1
from numpy import random

x = random.rand()

print(x)




# -------------------------------------Generate Random Array-----------------------------------------



# Generate a 1-D array containing 5 random integers from 0 to 100
from numpy import random

x = random.randint(100, size=(5))

print(x)


# Generate a 2-D array with 3 row
from numpy import random

x = random.randint(100, size=(3, 5))   # ( Row , No of Element )

print(x)





# Using Rand Function

from numpy import random

x = random.rand(5)

print(x)



from numpy import random

x = random.rand(3, 5)

print(x)



# -------------------------------------Generate Random Numbers from Array----------------------------

"""The choice() method allows you to generate a random value based on an array of values."""

from numpy import random

x = random.choice([3, 5, 7, 9])

print(x)


# With array
import numpy as np

arr = np.array([2, 6, 8, 10])
x = random.choice(arr)

print(x)




# Generate 2D array from array 
from numpy import random

x = random.choice([3, 5, 7, 9], size=(3, 5))

print(x)

