# -*- coding: utf-8 -*-
"""
Created on Wed Dec 07 13:59:40 2016

@author: medialab
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# joint in kinect
JointType_SpineBase = 0
JointType_SpineMid = 1
JointType_Neck = 2
JointType_Head = 3
JointType_ShoulderLeft = 4
JointType_ElbowLeft = 5
JointType_WristLeft = 6
JointType_HandLeft = 7
JointType_ShoulderRight = 8
JointType_ElbowRight = 9
JointType_WristRight = 10
JointType_HandRight = 11
JointType_HipLeft = 12
JointType_KneeLeft = 13
JointType_AnkleLeft = 14
JointType_FootLeft = 15
JointType_HipRight = 16
JointType_KneeRight = 17
JointType_AnkleRight = 18
JointType_FootRight = 19
JointType_SpineShoulder = 20
JointType_HandTipLeft = 21
JointType_ThumbLeft = 22
JointType_HandTipRight = 23
JointType_ThumbRight = 24



factor = 10
Jlen = {}
Jlen['0203'] = 13.4  #head2neck
Jlen['2002'] = 8.3   #neck2spinshoulder
Jlen['0120'] = 15.4  #spinshoulder2spinmiddle
Jlen['0001'] = 32.5  #spinmiddle2spinbase
Jlen['2008'] = 16.65 #spinshoulder2Rshoulder
Jlen['0809'] = 33.2  #Rshoulder2Relbow
Jlen['0910'] = 27.1  #Relbow2Rwrist
Jlen['2004'] = 16.65 #spinshoulder2Lshoulder
Jlen['0405'] = 33.2  #Lshoulder2Lelbow
Jlen['0506'] = 27.1  #Lelbow2Lwrist

J = {}
J[JointType_SpineBase] = np.array([80,100,0])

def uni_vec(Body,start,end):
    tmp = Body[start]-Body[end]
    vlen = sum(tmp**2)**5
    return tmp/vlen
  

def human_mod(Body):
    # Body : include all joints 3D position
    
    Vec0001 = uni_vec(Body, JointType_SpineBase    , JointType_SpineMid)
    Vec0120 = uni_vec(Body, JointType_SpineMid     , JointType_SpineShoulder)
    Vec2002 = uni_vec(Body, JointType_SpineShoulder, JointType_Neck)
    Vec0203 = uni_vec(Body, JointType_Neck         , JointType_Head)
    Vec2004 = uni_vec(Body, JointType_SpineShoulder, JointType_ShoulderLeft)
    Vec0405 = uni_vec(Body, JointType_ShoulderLeft , JointType_ElbowLeft)
    Vec0506 = uni_vec(Body, JointType_ElbowLeft    , JointType_WristLeft)
    Vec2008 = uni_vec(Body, JointType_SpineShoulder, JointType_ShoulderRight)
    Vec0809 = uni_vec(Body, JointType_ShoulderRight, JointType_ElbowRight)
    Vec0910 = uni_vec(Body, JointType_ElbowRight   , JointType_WristRight)
    
    J[JointType_SpineMid]      = J[JointType_SpineBase]    + Vec0001*Jlen['0001']
    J[JointType_SpineShoulder] = J[JointType_SpineMid]     + Vec0120*Jlen['0120']
    J[JointType_Neck]          = J[JointType_SpineShoulder]+ Vec2002*Jlen['2002']
    J[JointType_Head]          = J[JointType_Neck]         + Vec0203*Jlen['0203']
    J[JointType_ShoulderLeft]  = J[JointType_SpineShoulder]+ Vec2004*Jlen['2004']
    J[JointType_ElbowLeft]     = J[JointType_ShoulderLeft] + Vec0405*Jlen['0405']
    J[JointType_WristLeft]     = J[JointType_ElbowLeft]    + Vec0506*Jlen['0506']
    J[JointType_ShoulderRight] = J[JointType_SpineShoulder]+ Vec2008*Jlen['2008']
    J[JointType_ElbowRight]    = J[JointType_ShoulderRight]+ Vec0809*Jlen['0809']
    J[JointType_WristRight]    = J[JointType_ElbowRight]   + Vec0910*Jlen['0910']

    return J


def draw_human_mod(Joints):
    
    keys = Joints.keys()
    nframe = Joints[keys[0]].shape[1]   #total number of the frames
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    for fno in range(50,300):
        plt.cla()
        x = []
        y = []
        z = []

        for i in  xrange(nframe):
            x.append(Joints[keys[i]][0][fno])
            y.append(Joints[keys[i]][1][fno])
            z.append(-1*Joints[keys[i]][2][fno])

    ax.scatter(x, z, z, c = 'red', s = 100)

    ax.set_xlim(min(z),max(z))
    ax.set_ylim(min(x),max(x))
    ax.set_zlim(min(y),max(y))
    ax.set_title(fno)

    plt.draw()
    plt.pause(1.0/120)
    
             
    
    
    