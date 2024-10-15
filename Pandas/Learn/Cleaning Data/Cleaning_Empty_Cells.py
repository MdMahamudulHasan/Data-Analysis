"""

    Empty Cells
        Empty cells can potentially give you a wrong result when you analyze data.

    Remove Rows
        One way to deal with empty cells is to remove rows that contain empty cells.
        This is usually OK, since data sets can be very big, and removing a few rows will not have a big impact on the result.
"""

# Return a new Data Frame with no empty cells:
import pandas as pd 

df = pd.read_csv('G:/Data Analysis/Pandas/Learn/Cleaning Data/data.csv')

new_df = df.dropna()

print(new_df.to_string())




#Remove all rows with NULL values:
import pandas as pd 
df = pd.read_csv('G:/Data Analysis/Pandas/Learn/Cleaning Data/data.csv')

df.dropna(inplace=True)

print(df.to_string())