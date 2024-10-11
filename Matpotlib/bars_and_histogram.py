import matplotlib.pyplot as plt
import numpy as np

"""
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x,y)
plt.show()


"""


# --------------------------------------BAR COLOR-------------------------------------------------------------------

"""
import matplotlib.pyplot as plt
import numpy as np


x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x,y, color = 'red')
plt.show()

"""


#------------------------------------------------BAR WIDTH--------------------------------------------------------------------
"""
import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x, y, width= .5)
plt.show()


"""


#------------------------------------------------------------Histogram-------------------------------------------------
#----------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(170, 10, 250)
plt.hist(x, color='red', width = .5)
plt.show()