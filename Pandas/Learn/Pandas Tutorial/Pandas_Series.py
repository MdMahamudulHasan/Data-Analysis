"""

    What is a Series?
        A Pandas Series is like a column in a table.
    
    
    It is a one-dimensional array holding data of any type.

"""

# create a simple Pandas Series from a list

import pandas as pd 

a = [1, 7, 2]

my_var = pd.Series(a)

print(my_var)





#----------------------------------------------------Labels------------------------------------------------------

"""
    If nothing else is specified, the values are labeled with their index number. First value has index 0, second value has index 1 etc.
    
    
    This label can be used to access a specified value.

"""

#--------------------------------create Labels
import pandas as pd 

a = [1, 7, 2]

my_var = pd.Series(a, index=["x", "y", "z"])

print(my_var)


index_s = ["x", "y", "z"]
my_var = pd.Series(a, index=index_s)
print(my_var)

print(my_var["y"])



#------------------------------------------------------Key/Value Objects as Series-----------------------------------


# Create a simple Pandas Series from a dictionary:

import pandas as pd 

calories = {
    "day1": 420,
    "day2": 380,
    "day3": 390
}
my_var = pd.Series(calories)

print(my_var)


"""The keys of the dictionary become the labels."""

# Create a Series using only data from "day1" and "day2"
import pandas as pd 

calories = {
    "day1": 420,
    "day2": 380,
    "day3": 390
}
my_var = pd.Series(calories, index=["day1", "day2"])

print(my_var)


#--------------------------------------------------DataFrames--------------------------------------------------------

"""
    Data sets in Pandas are usually multi-dimensional tables, called DataFrames.

    Series is like a column, a DataFrame is the whole table.
"""

# Create a DataFrame from two Series:
import pandas as pd 

data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}
my_var = pd.DataFrame(data)

print(my_var)