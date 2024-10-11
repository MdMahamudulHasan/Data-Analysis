"""
import matplotlib.pyplot as plt
import numpy as np

x = np.array([35, 25, 25, 15])

plt.pie(x)
plt.show()



"""

#--------------------------PIE Labels--------------------------------------------------------
"""
import matplotlib.pyplot as plt
import numpy as np


y = np.array([35, 25, 25, 15])
my_labels = ["Appels", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels=my_labels)
plt.show()


"""
#--------------------------PIE Explode--------------------------------------------------------
"""


import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
my_labels = ["Apples", "Bananas", "Cherries", "Dates"]
my_explode = [0.1, 0.1, 0.1, 0.1]
plt.pie(y, labels=my_labels, explode=my_explode, shadow=True)
plt.show()



"""

# -----------------------------------------------------------Colors-------------------------------------------------
"""
import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
my_labels = ["Apples", "Bananas", "Cherries", "Dates"]
my_explode = [0.1, 0.1, 0.1, 0.1]
my_colors = ["Black", "Red", "Blue", "Green"]

plt.pie(y, labels=my_labels, explode=my_explode, shadow=True, colors=my_colors)

plt.show()

"""


# ---------------------------------------Legend----------------------------------------------------------------------



import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
my_labels = ["Apples", "Bananas", "Cherries", "Dates"]
my_explode = [0.1, 0.1, 0.1, 0.1]
my_colors = ["Black", "Red", "Blue", "Green"]

plt.pie(y, labels=my_labels, explode=my_explode, shadow=True, colors=my_colors)
plt.legend(title = "For Fruits")
plt.show()