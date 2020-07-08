# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 14:50:40 2020

@author: Luuk Hendriksen
"""

import numpy as np

#input
Numpix = 1280
Numpix2 = 1280
Numpix3 = 1024
H = 600000
Re = 6378000
w1 = 15
w2 = 61
alpha = 1.24/2
alpha2 = 42

def d2(w1, w2, H):
    return (np.arcsin(((Re + H)/Re)*np.sin(np.deg2rad(w1 + ((w2 - w1)/Numpix)))) - (np.deg2rad(w1 + ((w2 - w1)/Numpix))))*Re

def d1(w1, w2, H):
    return (np.arcsin(((Re + H)/Re)*np.sin(np.deg2rad(w1))) - np.deg2rad(w1))*Re

def d4(w1,w2, H):
    return (np.arcsin(((Re + H)/Re)*np.sin(np.deg2rad(w2))) - np.deg2rad(w2))*Re

def d3(w1, w2, H):
    return (np.arcsin(((Re + H)/Re)*np.sin(np.deg2rad(w2 - ((w2 - w1)/Numpix)))) - (np.deg2rad(w2 - ((w2 - w1)/Numpix))))*Re

PixelL = d4(w1, w2, H) - d3(w1, w2, H)
PixelS = d2(w1, w2, H) - d1(w1, w2, H)
print("Largest pixel", PixelL)
print("Smallest pixel", PixelS)

Tring = d4(w1, w2, H) - d1(w1, w2, H)
print("Inner R", d1(w1, w2, H))
print("Outer R", d4(w1, w2, H))
print("Tring", Tring)
print()

def d5(alpha, H):
    return (np.arcsin(((Re + H)/Re)*np.sin(np.deg2rad(alpha))) - np.deg2rad(alpha))*Re

def d6(alpha, H):
    return (np.arcsin(((Re + H)/Re)*np.sin(np.deg2rad(alpha - ((2*alpha)/Numpix2)))) - np.deg2rad(alpha - ((2*alpha)/Numpix2)))*Re

def d7(alpha, H):
    return (np.arcsin(((Re + H)/Re)*np.sin(np.deg2rad((2*alpha)/Numpix2))) - np.deg2rad((2*alpha)/Numpix2))*Re

PixelLL = d5(alpha, H) - d6(alpha, H)
PixelSL = d7(alpha, H)
totalL = d5(alpha, H)

print("Bigger linear FOV")
print("Largest linear pixel", PixelLL)
print("Smallest linear pixel", PixelSL)
print("Total length", 2*totalL)

def d8(alpha2, H):
    return (np.arcsin(((Re + H)/Re)*np.sin(np.deg2rad((2*alpha2)/Numpix3))) - np.deg2rad((2*alpha2)/Numpix3))*Re

def d9(alpha2, H):
    return (np.arcsin(((Re + H)/Re)*np.sin(np.deg2rad(alpha2))) - np.deg2rad(alpha2))*Re

def d10(alpha2, H):
    return (np.arcsin(((Re + H)/Re)*np.sin(np.deg2rad(alpha2 - ((2*alpha2)/Numpix3)))) - np.deg2rad(alpha2 - ((2*alpha2)/Numpix3)))*Re


PixelSL2 = d8(alpha2, H)
PixelLL2 = d9(alpha2, H) - d10(alpha2, H)
totalL2 = d9(alpha2, H)
print()
print("Smaller linear FOV")
print("Smallest linear pixel second FOV", PixelSL2)
print("Largest linear pixel second FOV", PixelLL2)
print("Total length", 2*totalL2)


while abs(PixelSL - PixelSL2) > 0.2:
    if PixelSL - PixelSL2 > 10:
        alpha2 += 0.5
    if PixelSL - PixelSL2 < -10:
        alpha2 -= 0.5
    elif PixelSL - PixelSL2 > 5:
        alpha2 += 0.001
    elif PixelSL - PixelSL2 < -5:
        alpha2 -= 0.001   
    elif PixelSL - PixelSL2 > 0:
        alpha2 += 0.0001
    elif PixelSL - PixelSL2 < 0:
        alpha2 -= 0.0001
    PixelSL2 = d8(alpha2, H)
 
print()
print("Adjusted smaller linear FOV")
print("Alpha2 giving same smallest pixel", alpha2)

PixelSL2 =  d8(alpha2, H)
PixelLL2 =  d9(alpha2, H) - d10(alpha2, H)
totalL2 = d9(alpha2, H)
print("Smallest linear pixel second FOV", PixelSL2)
print("Largest linear pixel second FOV", PixelLL2)
print("Total length", 2*totalL2)

     
        



    












