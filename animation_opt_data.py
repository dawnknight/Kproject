# -*- coding: utf-8 -*-
"""
Created on Fri Dec 02 13:04:16 2016

@author: liuqi
"""


import pickle as pk
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import pygame

f = open('mocapdata1128_array.pkl','rb')
data_all = pk.load(f).values()

keys = data_all[0]
NUM_LABELS = len(keys)  # total number of the labels
NUM_FRAMES = len(data_all[2][0])   #total number of the frames
print 'The total frames: ', NUM_FRAMES

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# data_orig   = {}  # dictionary
# data_interp = {}   


ax.set_xlabel('X axis')
ax.set_ylabel('Z axis')
ax.set_zlabel('Y axis')
    
for frame_no in range(50,300):
    plt.cla()
    
    xs = []
    ys = []
    zs = []
    for i in  xrange( NUM_LABELS ):
        xs.append(data_all[2][i*3][frame_no])
        ys.append(data_all[2][i*3+1][frame_no])
        zs.append(-1*data_all[2][i*3+2][frame_no])
        
    ax.scatter(xs, zs, ys)
    ax.set_xlim(-0.5,1.5)
    ax.set_ylim(-0.2,1.9)
    ax.set_zlim(1,2)
    plt.draw()
    plt.pause(1.0/120)
