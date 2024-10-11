import matplotlib.pyplot as plt
import numpy as np



"""
ypoints = np.array([3,1,8,4,10])

plt.plot(ypoints, linestyle = 'dotted')
plt.show()


"""

"""
        Style	                   Or
    ------------------        -------------
        'solid' (default)	       '-'	
        'dotted'	               ':'	
        'dashed'	               '--'	
        'dashdot'	               '-.'
"""


"""



import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, color = 'r')
plt.show()


"""



#---------------------------------------------------------------------Line Width----------------------------------------------------------------


"""


import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, linewidth = '20')
plt.show()               



"""


#------------------------------------------------------------------Multiple Line-----------------------------------------------------------

"""

import matplotlib.pyplot as plt
import numpy as np

y1 = np.array([3,8,1,10])
y2 = np.array([6,2,7,3,11])

plt.plot(y1)
plt.plot(y2)

plt.show()


"""



#--------------------------------------------------------------Matplotlib Labels and Title---------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------

"""


import matplotlib.pyplot as plt
import numpy as np

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320])

plt.plot(x, y)

plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.show()



"""

#------------------------------------------------------------------Create a Title for a Plot-----------------------------------------------------------


import matplotlib.pyplot as plt
import numpy as np

x = np.array([80, 85, 90, 95, 100, 105, 110, 115])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310,])

plt.plot(x, y)

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.show()