
# coding: utf-8

# In[1]:

import MDAnalysis.analysis.distances
from MDAnalysis import *
#get_ipython().magic(u'pylab inline')
import pyfeat 
import matplotlib 
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt



# In[2]:

u = Universe('confout.gro', 'trajK300-3.0.xtc', 'extend/trajK300-3.0.xtc')


# In[3]:

arg55 = u.select_atoms('resid 55 and name CZ')
pro4 = u.select_atoms('bynum 2539')
gly63 = u.select_atoms('resid 63 and name NE2')
ala2 = u.select_atoms('bynum 2515')
asn102n = u.select_atoms('bynum 1521')
ala3o= u.select_atoms('bynum 2525')
asn102o = u.select_atoms('bynum 1534')
ala3n= u.select_atoms('bynum 2517')


# In[4]:

box = u.dimensions
print box
dist1_array= MDAnalysis.analysis.distances.distance_array(arg55.coordinates(), pro4.coordinates(), box)
print dist1_array


# In[5]:

dist1_traj = [] #arg55:pro4
dist2_traj = [] #gly63:ala2
dist3_traj = [] #asn102n:ala3o
dist4_traj = [] #asn102o:ala3n
frame = []
nframe = 0
for ts in u.trajectory:
    dist1_array= MDAnalysis.analysis.distances.distance_array(arg55.coordinates(), pro4.coordinates(), box)
    dist1_traj.append(dist1_array[0])
    dist2_array= MDAnalysis.analysis.distances.distance_array(gly63.coordinates(), ala2.coordinates(), box)
    dist2_traj.append(dist2_array[0])
    dist3_array= MDAnalysis.analysis.distances.distance_array(asn102n.coordinates(), ala3o.coordinates(), box)
    dist3_traj.append(dist3_array[0])
    dist4_array= MDAnalysis.analysis.distances.distance_array(asn102o.coordinates(), ala3n.coordinates(), box)
    dist4_traj.append(dist4_array[0])
    nframe+=1
    frame.append(nframe)


# In[6]:

dist1 = np.array(dist1_traj)
dist2 = np.array(dist2_traj)
dist3 = np.array(dist3_traj)
dist4 = np.array(dist4_traj)


# In[7]:

hist = plt.hist((dist1,dist2,dist3,dist4),bins=50, range=[1,12],normed=True)


# In[8]:

center_bin = []
for i in xrange(1, len(hist[1])):
    center = 0.5*(hist[1][i] + hist[1][i-1])
    center_bin.append(center)
print len(center_bin)


# In[9]:

np.savetxt('dist_hist.dat',np.column_stack([center_bin, hist[0][0], hist[0][1], hist[0][2], hist[0][3]]), fmt='%0.8f')


# In[10]:

np.savetxt('dist.dat',np.column_stack([frame, dist1, dist2, dist3, dist4]), fmt='%0.8f')


# In[ ]:




# In[ ]:




# In[ ]:



