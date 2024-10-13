"""

    Logistic Distribution is used to describe growth.

    ""Used extensively in machine learning in logistic regression, neural networks etc.""
    
    It has three parameters:
            -> loc - mean, where the peak is. Default 0.
            -> scale - standard deviation, the flatness of distribution. Default 1.
            -> size - The shape of the returned array.
"""

# Draw 2x3 samples from a logistic distribution with mean at 1 and stddev 2.0:
from numpy import random

x = random.logistic(loc=1, scale=2, size=(2, 3))

print(x) 


#---------------------------------------------------Visualization of Logistic Distribution------------------------------

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns 

sns.distplot(random.logistic(size=1000), hist=False)

plt.show()


sns.distplot(x,hist=False)
plt.show()


"""

    Difference Between Logistic and Normal Distribution
        Both distributions are near identical, but logistic distribution has more area under the tails, meaning it represents more possibility of occurrence of an event further away from mean.
        
        
        For higher value of scale (standard deviation) the normal and logistic distributions are near identical apart from the peak.

"""

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns 

nor_rand = random.normal( scale=2, size=1000)
log_rand = random.logistic( size=1000)

sns.distplot(nor_rand, hist=False, label="normal")
sns.distplot(log_rand, hist=False, label="logistic")

plt.legend()
plt.show()