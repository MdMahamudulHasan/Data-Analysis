import matplotlib.pyplot as plt
import numpy as np




"""

xpoints = np.array([0.1,6])
ypoints = np.array([100,250])

plt.plot(xpoints, ypoints)
plt.show()



"""


"""


xpoints = np.array([0.1,6])
ypoints = np.array([100,250])

plt.plot(xpoints, ypoints,'o')
plt.show()


"""


#------------------------------------Multiple Points--------------------------------------------


"""

xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])
plt.plot(xpoints,ypoints)
plt.show()


"""


#--------------------------------------------Without X-Points--------------------------------------------


"""


ypoints = np.array([3,7,1,2,10,6,16,2])
plt.plot(ypoints)
plt.show()



"""



#-----------------------------------------Marker-------------------------------------------------------


"""

ypoints = np.array([3,7,1,2,10,6,16,2])
plt.plot(ypoints, marker = 'o')
plt.show()

"""






"""



ypoints = np.array([3,7,1,2,10,6,16,2])
plt.plot(ypoints, marker = '*')
plt.show()



"""




#-----------------------------------------------Format Strings----------------------------------------------



"""


ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, 'o:r')
plt.show()



"""

"""
    Line Syntax	                    Description
------------------              -------------------
       '-'                         	Solid line	
       ':'	                        Dotted line	
       '--'	                        Dashed line	
       '-.'	                     Dashed/dotted line





       Color Syntax             	Description
    -------------------         --------------------
           'r'	                        Red	
           'g'	                       Green	
           'b'	                        Blue	
           'c'	                        Cyan	
           'm'	                       Magenta	
           'y'	                       Yellow	
           'k'	                        Black	
           'w'	                        White
"""





#----------------------------------------Marker Size--------------------------------------------------

"""

ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, 'o:r', ms = 20)
plt.show()


"""



#----------------------------------------Marker Color--------------------------------------------------

ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, 'o:b', ms = 20, mec = 'r', mfc= 'k')
plt.show()
