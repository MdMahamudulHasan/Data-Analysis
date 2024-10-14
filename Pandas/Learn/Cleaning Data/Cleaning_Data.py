"""

    Data Cleaning
        Data cleaning means fixing bad data in your data set.
    
    
    Bad data could be:
            ->  Empty cells
            ->  Data in wrong format
            ->  Wrong data
            ->  Duplicates

"""

# Return a new DataFrame with no empty cells:
import pandas as pd 

df = pd.read_csv('G:/Data Analysis/Pandas/Learn/data.csv')

new_df = df.dropna()
# remove all empty row with index. No change in original DataFrame

print(new_df.to_string())




# if want to change in original DataFrame , use ( inplace = True ) argument:

#Remove all rows with NULL values:
import pandas as pd 

df = pd.read_csv('G:/Data Analysis/Pandas/Learn/data.csv')

df.dropna(inplace=True)

print(df.to_string())


"""Now, the dropna(inplace = True) will NOT return a new DataFrame, but it will remove all rows containing NULL values from the original DataFrame."""



#---------------------------------------------------------Replace Empty Values---------------------------------------------


"""

    Another way of dealing with empty cells is to insert a new value instead.
    
    This way you do not have to delete entire rows just because of some empty cells.
    
    The fillna() method allows us to replace empty cells with a value:

"""


# Replace NULL values with the number 130:

import pandas as pd 

df = pd.read_csv('G:/Data Analysis/Pandas/Learn/data.csv')

df.fillna(130, inplace=True)

print(df.to_string())



#-----------------------------------------------------Replace Only for Specified Columns--------------------------------


# Replace NULL values in the "Calories" columns with the number 130:
import pandas as pd 

df = pd.read_csv('G:/Data Analysis/Pandas/Learn/data.csv')

df["Calories"].fillna(130, inplace=True)

print(df.to_string())






#---------------------------------Replace Using Mean, Median, or Mode------------------------------------------------------
#-----------------------------------------------------------------------Most Important Part in Pandas-----------------------

"""

    ""A common way to replace empty cells, is to calculate the mean, median or mode value of the column.""

    Pandas uses the mean() median() and mode() methods to calculate the respective values for a specified column:
    
"""


# Calculate the MEAN, and replace any empty values with it:
import pandas as pd 

df = pd.read_csv('G:/Data Analysis/Pandas/Learn/data.csv')

x = df['Calories'].mean()

df['Calories'].fillna(x, inplace=True)

print(df.to_string())
"""Mean = the average value (the sum of all values divided by number of values)."""




# Calculate the MEDIAN, and replace any empty values with it:
import pandas as pd 

df = pd.read_csv('G:/Data Analysis/Pandas/Learn/data.csv')

x = df['Calories'].median()

df['Calories'].fillna(x, inplace=True)

print(df.to_string())
"""Median = the value in the middle, after you have sorted all values ascending."""





# Calculate the MODE, and replace any empty values with it:
import pandas as pd 

df = pd.read_csv('G:/Data Analysis/Pandas/Learn/data.csv')

x = df['Calories'].mode()[0]

df['Calories'].fillna(x, inplace=True)

print(df.to_string())
"""Mode = the value that appears most frequently."""