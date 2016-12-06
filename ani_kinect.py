# -*- coding: utf-8 -*-
"""
Created on Tue Dec 06 17:18:35 2016

@author: Dawnknight
"""

import cPickle 
import matplotlib.pyplot as plt
from Mocam2Kinect import *
from mpl_toolkits.mplot3d import Axes3D


data = cPickle.load(file('mocapdata1128_array.pkl','r'))





Kbody = Mocam2Kinect(data)

keys = Kbody.keys()
NUM_LABELS = len(keys)  # total number of the labels
NUM_FRAMES = Kbody[keys[0]].shape[1]   #total number of the frames
print 'The total frames: ', NUM_FRAMES

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for frame_no in range(50,300):
    plt.cla()
    
    xs = []
    ys = []
    zs = []
    for i in  xrange( NUM_LABELS ):
        xs.append(Kbody[keys[i]][0][frame_no])
        ys.append(Kbody[keys[i]][1][frame_no])
        zs.append(-1*Kbody[keys[i]][2][frame_no])
        
    ax.scatter(xs, zs, ys)
    ax.set_xlim(-0.5,1.5)
    ax.set_ylim(-0.2,1.9)
    ax.set_zlim(1,2)
    ax.set_title(frame_no)
    plt.draw()
    plt.pause(1.0/120)

