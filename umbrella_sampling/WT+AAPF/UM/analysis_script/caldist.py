
# coding: utf-8

# In[1]:
# In[17]:
import MDAnalysis.analysis.distances
from MDAnalysis import *
#get_ipython().magic(u'pylab inline')
import matplotlib
import pyfeat
import numpy as np
matplotlib.use('Agg')
import matplotlib.pyplot as plt


# In[2]:

u = Universe('confout.gro', 'trajK800+1.5.xtc', 'extend/trajK800+1.5.xtc')


# In[3]:

arg55 = u.select_atoms('resid 55 and name CZ')
pro4 = u.select_atoms('bynum 2521')
gly63 = u.select_atoms('resid 63 and name NE2')
ala2 = u.select_atoms('bynum 2497')
asn102n = u.select_atoms('bynum 1518')
ala3o= u.select_atoms('bynum 2507')
asn102o = u.select_atoms('bynum 1531')
ala3n= u.select_atoms('bynum 2499')


# In[4]:

ala3ca = u.select_atoms('bynum 2500')
ala3c = u.select_atoms('bynum 2506')
pro4n = u.select_atoms('bynum 2508')
pro4ca = u.select_atoms('bynum 2518')


# In[5]:

box = u.dimensions
print box
dist1_array= MDAnalysis.analysis.distances.distance_array(arg55.coordinates(), pro4.coordinates(), box)
print dist1_array
omega_array = MDAnalysis.lib.distances.calc_dihedrals(ala3ca.coordinates(),ala3c.coordinates(),pro4n.coordinates(),pro4ca.coordinates(), box)
print omega_array


# In[6]:

dist1_traj = [] #arg55:pro4
dist2_traj = [] #gly63:ala2
dist3_traj = [] #asn102n:ala3o
dist4_traj = [] #asn102o:ala3n
omega_traj = [] #omega
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
    omega_array = MDAnalysis.lib.distances.calc_dihedrals(ala3ca.coordinates(),ala3c.coordinates(),pro4n.coordinates(),pro4ca.coordinates(), box)
    omega_traj.append(omega_array[0])
    nframe+=1
    frame.append(nframe)


# In[7]:

dist1 = np.array(dist1_traj)
dist2 = np.array(dist2_traj)
dist3 = np.array(dist3_traj)
dist4 = np.array(dist4_traj)
omega = np.array(omega_traj)


# In[8]:

hist = plt.hist((dist1,dist2,dist3,dist4),bins=50, range=[1,12],normed=True)


# In[9]:

center_bin = []
for i in xrange(1, len(hist[1])):
    center = 0.5*(hist[1][i] + hist[1][i-1])
    center_bin.append(center)
print len(center_bin)


# In[10]:

np.savetxt('dist_hist.dat',np.column_stack([center_bin, hist[0][0], hist[0][1], hist[0][2], hist[0][3]]), fmt='%0.8f')


# In[11]:

np.savetxt('dist.dat',np.column_stack([frame, dist1, dist2, dist3, dist4]), fmt='%0.8f')


# In[12]:

np.savetxt('omega.dat',np.column_stack([frame, omega]), fmt='%0.8f')


# In[ ]:




# In[ ]:



