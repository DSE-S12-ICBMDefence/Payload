# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
Created on Tue May 12 12:14:00 2020

@author: Luuk Hendriksen
"""

import numpy as np
import matplotlib.pyplot as plt
"""
#Input
h = 500*1000                    #Orbital altitude
alpha = np.deg2rad(-1)       #Alpha in picture send in payload

#Constants
Re = 6378000                    #Radius earth

#Calculations
Rs = Re + h
beta = np.arcsin(((Rs)/(Re)) * np.sin(alpha)) + np.pi
phi = np.pi - abs(beta) - abs(alpha)
d = phi * Re

print(d)
print(np.rad2deg(phi))
print(np.rad2deg(beta))
print("Sum", np.rad2deg(abs(phi) + abs(beta) + abs(alpha)))

"""
def smallest(FOV, Numpix, h):
    Smallangle = FOV/Numpix
    alpha = np.deg2rad(-Smallangle)
    Re = 6378000
    Rs = Re + h
    beta = np.arcsin(((Rs)/(Re)) * np.sin(alpha)) + np.pi
    phi = np.pi - abs(beta) - abs(alpha)
    d = phi * Re
    return d

def biggest(FOV, Numpix, h):
    Smallangle = FOV/Numpix
    alpha = np.deg2rad(-FOV/2)
    Re = 6378000
    Rs = Re + h
    beta = np.arcsin(((Rs)/(Re)) * np.sin(alpha)) + np.pi
    phi = np.pi - abs(beta) - abs(alpha)
    d1 = phi * Re
    
    alpha = np.deg2rad(-1*(FOV/2 - Smallangle))
    beta = np.arcsin(((Rs)/(Re)) * np.sin(alpha)) + np.pi
    phi = np.pi - abs(beta) - abs(alpha)
    d2 = phi * Re
    
    d = d1 - d2
    return d


def Pixelsizes(FOV, Numpix, h):
    
    h *= 1000
    small = smallest(FOV, Numpix, h)
    big = biggest(FOV, Numpix, h)
    
    return small, big


ydata = []
xdata = []

ydata2 = []
xdata2 = []

ydata3 = []
xdata3 = []

ydata4 = []
xdata4 = []


h1 = 500
h2 = 1000

CameraRes = 720
PicturesPerRotation = 4

for i in range(1,125):
    ydata.append(Pixelsizes(i, CameraRes*PicturesPerRotation, h1)[1])
    xdata.append(i)
    ydata2.append(Pixelsizes(i, CameraRes*PicturesPerRotation, h1)[0])
    xdata2.append(i)


CameraRes = 720
PicturesPerRotation = 8
for i in range(1,125):
    ydata3.append(Pixelsizes(i, CameraRes*PicturesPerRotation, h2)[1])
    xdata3.append(i)
    ydata4.append(Pixelsizes(i, CameraRes*PicturesPerRotation, h2)[0])
    xdata4.append(i)

    #ydata3.append(Pixelsizes(180/np.pi*2*np.arctan(h1/h2*np.tan(i*np.pi/180/2)), CameraRes*PicturesPerRotation, h2)[1])
    #xdata3.append(i)
    #ydata4.append(Pixelsizes(180/np.pi*2*np.arctan(h1/h2*np.tan(i*np.pi/180/2)), CameraRes*PicturesPerRotation, h2)[0])
    #xdata4.append(i)
        
    
plt.figure()
plt.plot(xdata, ydata, color = "blue")
plt.plot(xdata2, ydata2, color = "blue")
plt.plot(xdata3, ydata3, color = "red")
plt.plot(xdata4, ydata4, color = "red")
plt.ylim((0,600))
plt.show()



    








#fig = plt.figure()
#ax1 = fig.add_subplot(111)
#ax1.set_title('Earth Camera')
#ax1.set_xlabel('X coord')
#ax1.set_ylabel('Y coord')
#ax1.plot(XEarth, YEarth, 'b')
##ax1.plot(Line1X, Line1Y, 'r')
#ax1.plot(Line2X[0::StepCount-5], Line2Y[0::StepCount-5], 'r')
#ax1.plot(Line3X[0::StepCount-5], Line3Y[0::StepCount-5], 'r')
#ax1.plot(Line4X[0::StepCount-5], Line4Y[0::StepCount-5], 'r')
#ax1.plot(Line5X[0::StepCount-5], Line5Y[0::StepCount-5], 'r')
#ax1.plot([Intersection2X,Intersection3X],[Intersection2Y,Intersection3Y],'g')
#ax1.plot([Intersection4X,Intersection5X],[Intersection4Y,Intersection5Y],'g')
#ax1.scatter(CenterX, CenterY, s=40)
#ax1.scatter(SatX, SatY, s=40)

#ax1.set_aspect(aspect=1)
#plt.show()

