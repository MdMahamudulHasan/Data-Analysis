
import pandas as pd 

myDataSet = {
    'cars': ["BMW", "Volvo", "Ford"],
    'passings':[3, 7, 2]
}

my_var = pd.DataFrame(myDataSet)

print(my_var)

# --------------------------------------------------Checking Pandas Version---------------------------------

import pandas as pd 
print(pd.__version__)

