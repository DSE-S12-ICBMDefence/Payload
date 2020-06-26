# -*- coding: utf-8 -*-
"""
Created on Sat May 16 16:44:15 2020

@author: Luuk Hendriksen, Guillermo Presa
"""

import numpy as np
import matplotlib.pyplot as plt

#All SI units

#Functions

#Filter definition:

SelectFilter = 2 #[1/ 2/ None]


LowCutoffFilter = 0
HightCutoffFilter = 0
FilterTransparency = 0
LowCutoffBand = 0
HighCutoffBand = 0
Scaling = 1

if SelectFilter == 2:
    LowCutoffFilter = 4.1 * 10**(-6)
    HightCutoffFilter = 4.52 * 10**(-6)

    FilterTransparency = 0.8
    Scaling = 0.7

    LowCutoffBand = 4.22 * 10**(-6)
    HighCutoffBand = 4.45 * 10**(-6)                 
    UseFilter = True
elif SelectFilter == 1:
    LowCutoffFilter = 2.625 * 10**(-6)
    HightCutoffFilter = 2.775  * 10**(-6)

    FilterTransparency = 0.25
    Scaling = 1

    LowCutoffBand = 2.7 * 10**(-6)
    HighCutoffBand = 2.9 * 10**(-6)
    UseFilter = True
else:
    UseFilter = False


def planck(Wavelength, Temp, emissivity, Filtered = True):
    PlankArray = np.zeros(np.shape(Wavelength)[0])
    if Filtered == True:
        if UseFilter == True:
            for i in range(0,np.shape(Wavelength)[0]):
                if Wavelength[i] > LowCutoffFilter and Wavelength[i] < HightCutoffFilter:
                    if Temp > 500 and Temp < 4000:
                        PlankArray[i] = Scaling*FilterTransparency*emissivity*((2*np.pi*h*c*c)/(Wavelength[i]**5))/(np.exp((h*c)/(Wavelength[i]*k*Temp)) - 1)
                    else:
                        PlankArray[i] = FilterTransparency*emissivity*((2*np.pi*h*c*c)/(Wavelength[i]**5))/(np.exp((h*c)/(Wavelength[i]*k*Temp)) - 1)
                if Temp < 500 and Wavelength[i] > LowCutoffBand and Wavelength[i] < HighCutoffBand:
                    PlankArray[i] = 0
                if Wavelength[i] < LowCutoffFilter or Wavelength[i] > HightCutoffFilter:
                    PlankArray[i] = 0
            return PlankArray
        else:
            return emissivity*((2*np.pi*h*c*c)/(Wavelength**5))/(np.exp((h*c)/(Wavelength*k*Temp)) - 1)
    else:
        return emissivity*((2*np.pi*h*c*c)/(Wavelength**5))/(np.exp((h*c)/(Wavelength*k*Temp)) - 1)
    #print("ERROR, no condition satisfied!!!!!!!!!!!!!!!!!!!!!!!!!!")

def NetD(LowWave, HighWave):
    FreqArray = np.linspace(LowWave,HighWave, 600)
    NetDArray = D + C*FreqArray + B*np.power(FreqArray,2) + A*np.power(FreqArray,3)
    Integral = np.trapz(NetDArray,FreqArray)
    NetD = Integral/(HighWave-LowWave)
    return NetD


Ascale = 11.75
Te1= 2500
Ae1 = 1*Ascale
Te2= 1700
Ae2 = 1*Ascale
Te3= 1200
Ae3 = 12*Ascale
Ae = Ae1+Ae2+Ae3 
Tb = 303.15
emissivityE = 0.1
emissivityB = 0.8
h = 6.624 * 10**(-34)
c = 3* 10**(8)
k = 1.38 * 10**(-23)

MinSNRRatio = 5
MinSNR = 5
MinTDiff = 5

VisualLambs = np.array([0.413,0.443,0.490,0.520,0.565,0.620,0.665,0.682,0.750,0.820,0.865,0.905,0.940,0.980]) * 10**(-6)
NetDs = np.array([390,515,557,556,555,467,399,273,302,203,255,138,100,59])

A,B,C,D = np.polyfit(VisualLambs,NetDs,3)

#Input
LowerLamb = 2.64 * 10**(-6) 
UpperLamb = 5 * 10**(-6)
TargetRatio = 1.1
PixelArea = np.power(15.0*np.power(10.0,-6),2)
OrbitAltitude = 500000

#def PixelSize(LowerLamb, UpperLamb, TargetDT, TargetRatio):
    
if UpperLamb < 1.1*10**(-6):
    NetD = NetD(LowerLamb, UpperLamb)
else:
    NetD = 92.6*10**(-3)

#Initials
NormalAngle = 0
H = 3300
W = 3300
Ab = (H*W) - Ae

emissivityB = emissivityB*np.cos(NormalAngle*np.pi/180)

Waves = np.linspace(LowerLamb, UpperLamb, 1000)
PlanckTe = Ae1/Ae * planck(Waves, Te1, emissivityE) + Ae2/Ae * planck(Waves, Te2, emissivityE) + Ae3/Ae * planck(Waves, Te3, emissivityE)
PlanckTb = planck(Waves, Tb, emissivityB) + planck(Waves, 5250, 0.000028)



NormFactor = np.power(10.0,-9) * np.amax(PlanckTe)

PlotFontSize = 25
Waves2 = 1000000*Waves
plt.figure()
plt.plot(Waves2, 100/NormFactor * np.power(10.0,-9) * PlanckTe, color = "red", label = "Net exhaust gas")
plt.plot(Waves2, 100/NormFactor * np.power(10.0,-9) * PlanckTb, color = "green", label = "Background radiance")
plt.plot(Waves2, 100/NormFactor * np.power(10.0,-9) * Ae1/Ae * planck(Waves, Te1, emissivityE), color = "orange", linestyle = "dashdot", label = "Exhaust gas at 3500k")
plt.plot(Waves2, 100/NormFactor * np.power(10.0,-9) * Ae2/Ae * planck(Waves, Te2, emissivityE), color = "orange", linestyle = "dashed", label = "Exhaust gas at 2200k")
plt.plot(Waves2, 100/NormFactor * np.power(10.0,-9) * Ae3/Ae * planck(Waves, Te3, emissivityE), color = "orange", linestyle = "dotted", label = "Exhaust gas at 1600k")
plt.xlabel('Wavelenght [μm]', fontsize = PlotFontSize)
plt.ylabel('Relative spectral radiance', fontsize = PlotFontSize)
plt.xticks(fontsize=PlotFontSize)
plt.yticks(fontsize=PlotFontSize)
plt.legend(fontsize = PlotFontSize)
yourmom = plt.gca()
yourmom.yaxis.grid()
plt.show()


Ttable = np.linspace(Tb, Te3, 1000)
Wmmtable = np.zeros(len(Ttable))

SR = PixelArea/OrbitAltitude

PlanckTbControlUNFILTERED = planck(Waves, Tb, emissivityB, False) + planck(Waves, 5250, 0.000028, False)
WmmTbControlUNFILTERED = np.trapz(PlanckTbControlUNFILTERED, Waves)*SR
PlanckTbControl = planck(Waves, Tb, emissivityB) + planck(Waves, 5250, 0.000028)
WmmTbControl = np.trapz(PlanckTbControl, Waves)*SR
print("The unfiltered integrated WmmTB as control is:", WmmTbControlUNFILTERED)
print("The filtered integrated WmmTB as control is:", WmmTbControl)

for i in range(len(Ttable)):
    PlanckT = planck(Waves, Ttable[i], emissivityB) + planck(Waves, 5250, 0.000028)
    Wmmtable[i] = np.trapz(PlanckT, Waves)*SR
    if i%100 == 0:
        print(i)
print("FINISH")
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
print("b")

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











