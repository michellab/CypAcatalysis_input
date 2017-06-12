
# coding: utf-8

# In[1]:

#get_ipython().magic(u'pylab inline')
import pyfeat
import numpy as np
import matplotlib.pyplot as plt

# In[8]:

#here is all the important data this is what you will have to change for more data! make sure 
#kappas and colvar files are matching!!!
data = []
filenames = [ 'COLVARK300+0.0_all','COLVARK300+3.0_all','COLVARK100+0.5_all', 'COLVARK300+0.75_all', 'COLVARK300+1.0_all', 'COLVARK500+1.25_all', 'COLVARK800+1.5_all', 'COLVARK800+1.75_all', 'COLVARK600+2.0_all', 'COLVARK500+2.25_all', 'COLVARK500+2.5_all', 'COLVARK800+2.75_all', 'COLVARK800-0.5_all', 'COLVARK800-0.75_all', 'COLVARK800-1.0_all', 'COLVARK800-1.25_all', 'COLVARK800-1.5_all', 'COLVARK800-1.75_all', 'COLVARK700-2.0_all' ,'COLVARK800-2.25_all', 'COLVARK500-2.5_all', 'COLVARK300-3.0_all', 'COLVARK800-2.75_all',  'COLVARK500-0.25_all'] #list of input files
kappa = np.array([ 300, 300, 100, 300, 300, 500, 800, 800, 600, 500, 500, 800, 800, 800, 800, 800, 800, 800, 700, 800, 500, 300, 800, 500]) #array of kappa values matching file list
omega_0 = np.array([ 0.0, 3.0, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0, 2.25, 2.5, 2.75, -0.5, -0.75, -1.0, -1.25, -1.5, -1.75, -2.0, -2.25, -2.5, -3.0, -2.75, -0.25])
kBT=300*0.008


# In[10]:

for f in filenames:
    data.append(np.loadtxt(f,usecols=(1,2))) # this will load the data from file f using the second column of the file


# In[11]:

#def B(omega,kappa,omega_0):
 #   return 0.5*kappa*(omega-omega_0)**2
def B(omega,kappa, omega_0):
    pi = 3.1415926536
    if omega_0 < 0 and omega > 0:
        return 0.5*kappa*((-pi + omega - pi)-omega_0)**2
    if omega_0 > 0 and omega < 0:
        return 0.5*kappa*((pi + omega + pi)-omega_0)**2
    else:
        return 0.5*kappa*(omega-omega_0)**2


# In[12]:

#find the minimum and maximum of our data for binning
currmin=100.0
currmax = -100
for d in data:
    if currmin> np.min(d[:,0]):
        currmin = np.min(d[:,0])
    if currmax<np.max(d[:,0]):
        currmax = np.max(d[:,0])
print currmax, currmin


# In[13]:

bins = np.linspace(currmin+0.01, currmax+0.01,100) #generates an array of linearly spaced bin centres


# In[14]:

#discretize omega trajectories
discrete_traj = []
for d in data:
    discrete_traj.append(np.digitize(d[:,0],bins))


# In[ ]:

#for i in xrange(len(discrete_traj)):
#    print np.max(discrete_traj[i])
#    plt.plot(discrete_traj[i])


# In[ ]:

biases_list = []
for d in data:
    traj_length = d[:,0].shape[0]
    bias = np.zeros(shape=(traj_length,kappa.shape[0]))
    for i in xrange(traj_length):
        curr_omega = d[i,0]
        for k in xrange(kappa.shape[0]):
            temp_bias = B(curr_omega, kappa[k], omega_0[k])/kBT
            bias[i][k] = temp_bias
    biases_list.append(bias)


# In[ ]:

b_K_i = np.zeros(shape=(kappa.shape[0],bins.shape[0]))
N_i = np.zeros(shape=(bins.shape[0]))
N_K_i = np.zeros(shape=(kappa.shape[0], bins.shape[0]))
for i in xrange(len(discrete_traj)):
    for t in xrange(discrete_traj[i].shape[0]):
        curr_state = discrete_traj[i][t]
        N_i[curr_state] = N_i[curr_state]+1
        N_K_i[i][curr_state] = N_K_i[i][curr_state]+1
        for K in xrange(kappa.shape[0]):
            b_K_i[K][curr_state] = b_K_i[K][curr_state]+biases_list[i][t][K]
b_K_i = b_K_i/N_i


# In[ ]:

wham_obj = pyfeat.wham_me(N_K_i,b_K_i,maxiter = 10000)


# In[ ]:

#plt.plot(bins,wham_obj.f_i*0.59616123)
#plt.xlabel(r'$\omega$ in [radians]', fontsize=15)
#plt.ylabel('F', fontsize=15 )
#plt.savefig('free_energy_of_freeAAPF.png')


# In[ ]:

np.savetxt('free_energy_of_freeAAPF.dat', np.transpose([bins,wham_obj.f_i*0.59616123]), fmt='%1.4e')


# In[ ]:

#plt.plot(bins,(wham_obj.f_i*0.59616123))
#plt.xlabel(r'$\omega$ in [radians]', fontsize=15)
#plt.ylabel('F kcal/mol', fontsize=15 )
#plt.savefig('free_energy_of_freeAAPF2.png')


# In[ ]:




# In[ ]:



