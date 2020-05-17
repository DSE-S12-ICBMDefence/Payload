# -*- coding: utf-8 -*-
"""
Created on Sat May 16 16:44:15 2020

@author: Luuk Hendriksen
"""

import numpy as np
import matplotlib.pyplot as plt

#All SI units

#Functions
def planck(Wavelength, Temp, emissivity):
    return emissivity*((2*h*c*c)/(Wavelength**5))/(np.exp((h*c)/(Wavelength*k*Temp)) - 1)

def NetD(LowWave, HighWave):
    FreqArray = np.linspace(LowWave,HighWave, 600)
    NetDArray = D + C*FreqArray + B*np.power(FreqArray,2) + A*np.power(FreqArray,3)
    Integral = np.trapz(NetDArray,FreqArray)
    NetD = Integral/(HighWave-LowWave)
    return NetD


Te1= 3500
Ae1 = 8.25
Te2= 2200
Ae2 = 20
Te3= 1600
Ae3 = 25
Ae = Ae1+Ae2+Ae3 
Tb = 303.15
emissivityE = 0.1
emissivityB = 0.8
h = 6.63 * 10**(-34)
c = 3* 10**(8)
k = 1.38 * 10**(-23)

MinSNRRatio = 5.5
MinSNR = 10
MinTDiff = 5

VisualLambs = np.array([0.413,0.443,0.490,0.520,0.565,0.620,0.665,0.682,0.750,0.820,0.865,0.905,0.940,0.980]) * 10**(-6)
NetDs = np.array([390,515,557,556,555,467,399,273,302,203,255,138,100,59])

A,B,C,D = np.polyfit(VisualLambs,NetDs,3)

#Input
LowerLamb = 0.975 * 10**(-6) 
UpperLamb = 1 * 10**(-6)
TargetDT = 7.5
TargetRatio = 1.1
PixelArea = np.power(15.0*np.power(10.0,-6),2)
OrbitAltitude = 500000

#def PixelSize(LowerLamb, UpperLamb, TargetDT, TargetRatio):
    
if UpperLamb < 1.1*10**(-6):
    NetD = NetD(LowerLamb, UpperLamb)
else:
    NetD = 20*10**(-3)

#Initials
H = 180
W = 180
Ab = (H*W) - Ae

Waves = np.linspace(LowerLamb, UpperLamb, 1000)
PlanckTe = Ae1/Ae * planck(Waves, Te1, emissivityE) + Ae2/Ae * planck(Waves, Te2, emissivityE) + Ae3/Ae * planck(Waves, Te3, emissivityE)
PlanckTb = planck(Waves, Tb, emissivityB) + planck(Waves, 5250, 0.000028)

Ttable = np.linspace(Tb, Te3, 20000)
Wmmtable = np.zeros(len(Ttable))

SR = PixelArea/OrbitAltitude

for i in range(len(Ttable)):
    PlanckT = planck(Waves, Ttable[i], emissivityB) + planck(Waves, 5250, 0.000028)
    Wmmtable[i] = np.trapz(PlanckT, Waves)*SR
    
WmmTe = np.trapz(PlanckTe, Waves)*SR
WmmTb = np.trapz(PlanckTb, Waves)*SR



WTe = WmmTe * Ae
WTb = WmmTb * Ab

Wmmav = (WTe + WTb)/(H*W)
minimum = abs(Wmmav - Wmmtable[0])
index = 0

for i in range(len(Wmmtable)):
    Wmmavdiff = abs(Wmmav - Wmmtable[i])
    if Wmmavdiff < minimum:
        minimum = Wmmavdiff
        index = i
        
Tav = Ttable[index]


PlanckTbNetD = planck(Waves, Tb + NetD, emissivityB) + planck(Waves, 5250 + NetD, 0.000028)
WmmTbNetD = np.trapz(PlanckTbNetD, Waves)*SR
print("NetD: ",NetD)
FluxR = Wmmav/(WmmTbNetD-WmmTb)
print("SNR with rocket:", FluxR)
Tdiff = Tav - Tb
print("Tdiff: ", Tdiff)
PlanckTe2 = planck(Waves, Tb, emissivityE)
WmmTe2 = np.trapz(PlanckTe2, Waves)*SR
WTe2 = WmmTe2 * Ae
WTb2 = WmmTb * Ab
Wmmav2 = (WTe2 + WTb2)/(H*W)
FluxR2 = Wmmav2/(WmmTbNetD-WmmTb)
print("SNR with OUT rocket:", FluxR2)
SNRRatio = (FluxR-FluxR2)
print("Power ratio:",SNRRatio)

TbNetD = Tb + NetD
TdiffN = Tav/TbNetD

print("")
print("")
print("")
print("")
print("")

if SNRRatio < MinSNRRatio:
     print("***********************************************")
     print("RES too large, SNR ratio smaller than threshold")
     print("***********************************************")
if FluxR < MinSNR:
    print("***********************************************")
    print("RES too large, SNR smaller than threshold")
    print("***********************************************")
if Tdiff < MinTDiff:
    print("***********************************************")
    print("RES too large, Tdiff smaller than threshold")
    print("***********************************************")






