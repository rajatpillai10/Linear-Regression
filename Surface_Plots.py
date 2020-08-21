#!/usr/bin/env python
# coding: utf-8

# #### Surface Plots | Data Visualisation

# In[1]:


from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np


# In[4]:


a = np.arange(-1,1,0.02)
b = a 
a,b = np.meshgrid(a,b)
fig = plt.figure()
axes = fig.gca(projection='3d')
axes.plot_surface(a,b,a**2+b**2,cmap='rainbow')
plt.show()


# In[6]:


fig = plt.figure()
axes = fig.gca(projection='3d')
axes.contour(a,b,a**2+b**2,cmap='rainbow')
plt.title("Contour Plot")
plt.show()


# In[ ]:




