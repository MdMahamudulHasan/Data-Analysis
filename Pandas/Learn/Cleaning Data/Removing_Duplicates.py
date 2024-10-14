"""

    To discover duplicates, we can use the duplicated() method.
    
    The duplicated() method returns a Boolean values for each row:

"""


# Returns True for every row that is a duplicate, otherwise False:
import pandas as pd 
df = pd.read_csv('G:/Data Analysis/Pandas/Learn/Cleaning Data/data.csv')

print(df.duplicated())



#----------------------------------------------Removing Duplicates--------------------------------------


"""To remove duplicates, use the drop_duplicates() method."""


# Remove all duplicates:

df.drop_duplicates(inplace=True)

print(df.duplicated())


"""

Remember: The (inplace = True) will make sure that the method does NOT return a new DataFrame, but it will remove all duplicates from the original DataFrame.

"""