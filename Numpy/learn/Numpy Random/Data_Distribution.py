"""
    What is Data Distribution?
    
    Data Distribution is a list of all possible values, and how often each value occurs.
    
    Such lists are important when working with statics and data science.

"""

"""

    Random Distribution
    
    A random distribution is a set of random numbers that follow a certain probability density function.
    
    "The probability is set by a number between 0 and 1, where 0 means that the value will never occur and 1 means that the value will always occur."

"""

# Generate a 1-D array containing 100 values, where each value has to be 3, 5, 7 or 9.

from numpy import random

x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100))
# probabilities sum will be always 1
print(x)


# Same example as above, but return a 2-D array with 3 rows, each containing 5 values.
import numpy as np
from numpy import random

arr = np.array([3, 5, 7, 9])
probabilities = [0.1 , 0.3, 0.6, 0.0]
x = random.choice(arr,p=probabilities, size=(3, 5))
print(x)

