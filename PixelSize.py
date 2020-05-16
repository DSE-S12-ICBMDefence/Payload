## -*- coding: utf-8 -*-
#"""
#Created on Sat May  9 13:04:50 2020

#@author: Luuk Hendriksen
#"""
#import numpy as np
#import matplotlib.pyplot as plt


#Steps = 1000
#LowFreqLim = 0.1
#HighFreqLim = 10

#C1 =  3.743 * np.power(10,8)
#C2 =  1.4387  * np.power(10,4)


#def Emmision(Emmissivity, Wavelenght, Temp):
#    if Temp > 3000:
#        print("The SUN")
#    E = Emmissivity*((C1*np.power(Wavelenght,-5))/(np.exp(C2/(Wavelenght*Temp))-1))
#    return E

#def TotalEmmision(Emmissivity,Temp,LowFreq,HighFreq, Graph = False):
#    print("Doing total emmision")
#    WavelenghtArray = np.linspace(start=LowFreq, stop=HighFreq, num=Steps, dtype = 'double')
#    EArray = Emmision(Emmissivity, WavelenghtArray, Temp) 
#    print("EArray 1 is", EArray)
#    EArray = EArray + + Emmision(0.000028, WavelenghtArray, 5525)
#    print("EArray 2 is", EArray)
#    IntegralE = np.trapz(EArray, WavelenghtArray)
#    if Graph == True:
#        fig = plt.figure()
#        ax = fig.add_subplot(111)
#        ax.set_title('')
#        ax.set_xlabel('Wavelenght [um]')
#        ax.set_ylabel('E [W/m^2 * um]')
#        ax.plot(WavelenghtArray,EArray, 'b')
#        #ax.plot(WavelenghtArray,Emmision(EmissivityE,WavelenghtArray,Te), 'r')
#        plt.show()
#    return IntegralE


#H = 500
#W = 500                       #Pixel width
#Ae = 55                                 #Exhaust plume area
#NETD = 0.04                             #NETD

#sigma =  5.670374419 * 10**(-8)         #Stefan Boltzman constant
#Te = 2400                               #Exhaust temperature
#Tb = 30 + 273.15  
#EmissivityE = 0.1
#EmissivityB = 0.8                      #Background temperature
           
#                                          #Background radiation per unit time per area

#Je2 = TotalEmmision(EmissivityE,Te,LowFreqLim,HighFreqLim, Graph = True) 
#Jb2 = TotalEmmision(EmissivityB, Tb, LowFreqLim, HighFreqLim, Graph = True) + TotalEmmision(0.000028, 5525,LowFreqLim,HighFreqLim,Graph = True)

#Pe = Je2 * Ae                            #Exhaust radiation per unit time
#Ab = (H * W) - Ae                       #Background area = pixel area - exhaust plume area
#Pb = Jb2 * Ab                            #Background radiation per unit time

#Ap = H * W                              #Area pixel
#Jap = (Pe + Pb)/Ap   

#print("Je is:", Je2)
#print("Jb is:", Jb2)
#print("Jap is:", Jap)

#Tlist = np.linspace(Tb, Te, 10000)               
#Jlist = np.zeros(len(Tlist))
#index = 0



#for temp in Tlist:
#    Jlist[index] = TotalEmmision(EmissivityB, temp, LowFreqLim, HighFreqLim, Graph = False) + TotalEmmision(0.000028, 5525,LowFreqLim,HighFreqLim,Graph = False)
#    index += 1

#print("Jlist is:", Jlist[0:20])
#print("Jlist is:", Jlist[::100])

#index2 = 0
#minimum = 100000000
#for i in range(len(Jlist)):
#    if abs(Jap - Jlist[i]) < minimum:
#        minimum = Jap - Jlist[i] 
#        index2 = i
        
#Tap = Tlist[index2]
    
       
##Tap = ((Jap)/(sigma))**(0.25)           #Average pixel temperature
#print("Index 2 is", index2)
#print("TAP is", Tap)
#print("Tb is", Tb)

#Tdiff = Tap - Tb                        #Should be larger than NETD
#SNR = Jap/Jb2                            #Signal to noise ratio

#print("Average pixel temperature", Tap)
#print("Background temperature", Tb)
#print("Tdiff", Tdiff)
#print("SNR", SNR)

#if Tdiff > NETD:
#    print("Pixel colour changed due to presence of missile exhaust")
    






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


Te = 2000 
Tb = 303.15
Ae = 55
emissivityE = 0.1
emissivityB = 0.8
h = 6.63 * 10**(-34)
c = 3* 10**(8)
k = 1.38 * 10**(-23)

VisualLambs = np.array([0.413,0.443,0.490,0.520,0.565,0.620,0.665,0.682,0.750,0.820,0.865,0.905,0.940,0.980]) * 10**(-6)
NetDs = np.array([390,515,557,556,555,467,399,273,302,203,255,138,100,59])

A,B,C,D = np.polyfit(VisualLambs,NetDs,3)

#Input
LowerLamb = 0.8 * 10**(-6) 
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
H = 700
W = 700
Ab = (H*W) - Ae

Waves = np.linspace(LowerLamb, UpperLamb, 1000)
PlanckTe = planck(Waves, Te, emissivityE)
PlanckTb = planck(Waves, Tb, emissivityB) + planck(Waves, 5250, 0.000028)

Ttable = np.linspace(Tb, Te, 10000)
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
print(FluxR)
Tdiff = Tav - Tb

print("Tdiff: ", Tdiff)

TbNetD = Tb + NetD
TdiffN = Tav/TbNetD


    
    











