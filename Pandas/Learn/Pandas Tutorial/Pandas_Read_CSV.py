"""

    Read CSV Files
        A simple way to store big data sets is to use CSV files (comma separated files).
        
        CSV files contains plain text and is a well know format that can be read by everyone including Pandas.

"""

# Load the CSV into a DataFrame:
import pandas as pd 

df = pd.read_csv('G:/Data Analysis/Pandas/Learn/data.csv')

print(df.to_string())

"""use to_string() to print the entire DataFrame."""


"""
    If you have a large DataFrame with many rows, Pandas will only return the first 5 rows, and the last 5 rows:
    
"""
#print the DataFrame without the to_string() method:
import pandas as pd 

df = pd.read_csv('G:/Data Analysis/Pandas/Learn/data.csv')

print(df)


#-----------------------------------------------------------Max rows-------------------------------------------------

"""

    The number of rows returned is defined in Pandas option settings.
    
    You can check your system's maximum rows with the pd.options.display.max_rows statement.

"""

# check the number of maximum returned rows:
import pandas as pd 

print(pd.options.display.max_rows)


"""You can change the maximum rows number with the same statement."""

import pandas as pd 

pd.options.display.max_rows= 9999

df = pd.read_csv('G:/Data Analysis/Pandas/Learn/data.csv')

print(df)

"""CSV means Comma Separated Value"""

