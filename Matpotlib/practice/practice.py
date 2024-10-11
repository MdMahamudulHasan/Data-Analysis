"""


import matplotlib.pyplot as plt
import numpy as np


x = np.array([5,7,1,9,2,10])
y = np.array([30, 40, 50, 20, 60,25])

plt.scatter(x,y)


x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
plt.scatter(x, y)

plt.show()



x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])
plt.scatter(x, y, c= colors, cmap="viridis")
plt.colorbar()
plt.show()



"""


#------------------------------------------------------------Bars----------------------------------------



"""
import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 1, 8, 10])

plt.bar(x, y, width=0.2)
plt.show()

"""




import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 12, 56, 27])
my_lables = ["Apples", "Bananas", "Cherries", "Dates"]
my_colors = ["Red", "Blue", "Black", "Green"]
my_explode = [0.1, 0, 0, 0]
plt.pie(y, labels=my_lables, colors=my_colors, shadow=True, explode=my_explode)

plt.legend(title = "For Fruits")
plt.show()

