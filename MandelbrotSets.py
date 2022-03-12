# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 10:07:52 2021

@author: Uday Talwar
"""

import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib as mpl 

mpl.rcParams['figure.dpi'] = 4800

def mandelbrotset(steps,threshold,msize,nsize,degree):
    '''
    The underlying function is of the form z_n+1 = z_n^k + c - z_0 (initial value) = 0. 
    
    steps = number of iterations
    
    threshold = upper bound to estimate divergence/convergence of given C value
    
    msize = number of rows in np.mgrid
    
    nsize = number of columns in np.mgrid
    
    degree = the degree/power of z_n, corresponds to k in the underlying function
    '''
    
    steps = int(steps) 
    threshold = int(threshold)
    msize, nsize = int(msize), int(nsize)
    
    xmin, xmax, resox = -2,1,complex(0,msize) #the x-axis bounds of the grid and column size
    ymin, ymax, resoy = -1.5,1.5,complex(0,nsize) #y-axis bounds of the grid and row size
    
    x,y = np.mgrid[xmin:xmax:resox, ymin:ymax:resoy] #initiate mgrid

    c = x+1j*y #define c

    z = 0 #initialize z 
    
    for j in range(steps): #iterate z as z_n+1 = (z_n)^2 + c, where z_0 = 0
        
        z = np.where(abs(z)<threshold,z, threshold+1)**(degree) + c #computes only those elements that are < 50 

    req_set = (abs(z) < threshold) #filter grid for absolute values of z lower than theshold
        
    return req_set #return filtered grid

mbrot = mandelbrotset(100,50,1000,1000,2) #run iteration

#plot iteration
plt.clf()

plt.imshow(mbrot.T, extent = [-2, 1, -1.5, 1.5])
plt.gray()
plt.show()

#some other interesting renders with varying function forms

def mandelbrotset2(steps,threshold,msize,nsize,degree):
    
    '''Underlying function of the form z_n+1 = z_n^k + z_n^k-1 + c'''
    
    xmin, xmax, resox = -2,1,complex(0,msize)
    ymin, ymax, resoy = -1.5,1.5,complex(0,nsize)
    
    x,y = np.mgrid[xmin:xmax:resox, ymin:ymax:resoy] 

    c = x+1j*y

    z = c
    
    for j in range(steps): #of the form, z_n+1 = z_n^k + z_n^k-1 + c
        
        z = np.where(abs(z)<threshold,z, threshold+1)**degree + \
            np.where(abs(z)<threshold,z, threshold+1)**(degree-1) + c

    req_set = (abs(z) < threshold)
        
    return req_set

test2 = mandelbrotset2(100,50,1000,1000,3)

plt.clf()

plt.imshow(test2.T, extent = [-2, 1, -1.5, 1.5])
plt.gray()
plt.show()



def mandelbrotset3(steps,threshold,msize,nsize,degree):
    
    '''Underlying function of the form z_n+1 = z_n^k + z_n^k-1 + z_n^k-2 + c'''
    
    xmin, xmax, resox = -2,1,complex(0,msize)
    ymin, ymax, resoy = -1.5,1.5,complex(0,nsize)
    
    x,y = np.mgrid[xmin:xmax:resox, ymin:ymax:resoy]

    c = x+1j*y

    z = c
    
    for j in range(steps): #of the form, z_n+1 = z_n^k + z_n^k-1 + z_n^k-2 + c
        
        z = np.where(abs(z)<threshold,z, threshold+1)**degree + \
            np.where(abs(z)<threshold,z, threshold+1)**(degree-1) + \
                np.where(abs(z)<threshold,z, threshold+1)**(degree-2) + c 

    req_set = (abs(z) < threshold)
        
    return req_set

test3 = mandelbrotset3(100,50,1000,1000,3)

plt.clf()

plt.imshow(test3.T, extent = [-2, 1, -1.5, 1.5])
plt.gray()
plt.show()
