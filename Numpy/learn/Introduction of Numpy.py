#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

a= [20, 20, 40]
b= [10, 20, 30]
print(a)
print(b)
print(np.array(a)* np.array(b))
print(type(a))
print(type(b))


# In[6]:


import numpy as np
a = np.array([11,12,13])
print (a)
print(type(a))


# In[2]:


import numpy as np

print(np.__version__)


# In[3]:


import numpy as np


# 0D Arrays
arr = np.array(43)
print(arr)


# In[4]:


import numpy as np

#1-D Array
arr = np.array([1, 2, 3, 4, 5])
print(arr)


# In[5]:


import numpy as np

#2-D Array
arr = np.array([[1, 3, 5], [2, 3, 6]])
print(arr)


# In[6]:


import numpy as np

#3-D Array
arr = np.array([[[1, 2, 3],[4, 5, 6]], [[1, 2, 3],[4, 5, 6]]])
print(arr)


# In[7]:


import numpy as np

# Check Number of Dimensions
a = np.array(43)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 3, 5], [2, 3, 6]])
d = np.array([[[1, 2, 3],[4, 5, 6]], [[1, 2, 3],[4, 5, 6]]])


print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)


# In[10]:


#  Higher Dimensional Arrays
import numpy as np

arr = np.array([1, 2, 3, 4, 5], ndmin = 5)

print(arr)
print('Number of dimensions : ',arr.ndim)


# In[14]:


#----------------------------------------- Numpy Array Indexing---------------


# 1-D Array Access
import numpy as np

arr = np.array([1, 2, 3, 4])
print(arr[0])
print(arr[3])
print(arr[2] + arr[3])


# In[19]:


# Numpy Array Indexing

# 2-D Array Access
import numpy as np

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print("2nd element on 1st row: ", arr[0, 1])
print("5th element on 2nd row: ", arr[1, 4])


# In[20]:


# Numpy Array Indexing

# 3-D Array Access
import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr[0, 1, 2])


# In[21]:


# Negative Indexing

import numpy as np

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print ('Last element from 2nd dim: ',arr[1, -1])


# In[24]:


#--------------------------------- Slicing Arrays---------------------------

import numpy as np

arr= np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5])
print(arr[4:])
print(arr[:4])


# In[30]:


# Negative Slicing

import numpy as np

arr= np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[-3:-1])

# Use step value
print(arr[1:5:2])
print(arr[::2])


# In[39]:


#--------Slicing 2-D Arrays

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[1, 1:4])
print(arr[0:2, 2])

print(arr[0:2, 1:4])


# In[40]:


#-----------------------------Nympy Array Copy vs View-----------------------


# -----COPY-----

import numpy as np
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0]=42

print(arr)
print(x)


# In[41]:


#------VIEW------

import numpy as np
arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42
print(arr)
print(x)


# In[42]:


# MAKE CHANGES VIEW

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
x[0] = 31

print(arr)
print(x)


# In[43]:


#--------------------------Check if Arrays Owns its Data--------------

import numpy as np

arr = np.array([1, 2, 3, 4, 5])

x = arr.copy()
y = arr.copy()

print(x.base)
print(y.base)


# In[45]:


# ---------------------------------Numpy Array Shape-------------------------

import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr. shape)


# In[48]:


import numpy as np

arr = np.array([1, 2, 3, 4], ndmin = 5)
print(arr)
print("Shape of array: " ,arr.shape)


# In[50]:


#-------------------------------Numpy Array Reshaping------------------------

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(3,4)
print(newarr)

newarr1 = arr.reshape(2, 3, 2)
print(newarr1)


# In[51]:


#---------------Returns Copy or View----------------------

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(arr.reshape(2, 4).base)


# In[53]:


import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = arr.reshape(2, 4)
print(newarr)
print(newarr.base)


# In[54]:


#-------------------------------Iterating Arrays-----------------------------

import numpy as np

arr = np.array([1, 2, 3])

for x in arr:
    print(x)


# In[55]:


import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
    print(x)


# In[57]:


import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
    for y in x:
        print(y)


# In[58]:


import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
  for y in x:
    for z in y:
      print(z)


# In[59]:


# --------------------Iterating Arrays Using nditer()----------------------

import numpy as np

arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr):
  print(x)


# In[60]:


#----------------------Enumerated Iteration Using ndenumerate()----------------

import numpy as np

arr = np.array([1, 2, 3])
for idx, x in np.ndenumerate(arr):
    print(idx, x)


# In[61]:


import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for idx, x in np.ndenumerate(arr):
    print(idx, x)


# In[ ]:




