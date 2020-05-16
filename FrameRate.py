
from matplotlib import pyplot as plt
import numpy as np
import math
import tkinter as tk



SamplingFrequency = 1   #[Hz]

ThetaD = np.pi/2        #[rad]

Gamma0 = 0.415          #[rad]

MECOAcceleration = 2    #[g_force]

#----------------
EarthGravCTE = 3.986044418 * math.pow(10,14)
RadiusEarth = 6371000 #m
r0 = RadiusEarth

#def cart2pol(x, y):
#    rho = np.sqrt(x**2 + y**2)
#    phi = np.arctan2(y, x)
#    return(rho, phi)

#def pol2cart(rho, phi):
#    x = rho * np.cos(phi)
#    y = rho * np.sin(phi)
#    return(x, y)

def ComputeTrajectory(V0, Gamma0 = None):
    Lambda = (r0*np.power(V0,2))/EarthGravCTE

    if Gamma0 == None:
        Gamma0 = 1/2*np.arcos(Lambda/(2-Lambda))

    ThetaValues = np.linspace(start=0, stop=2*np.pi, num=250, dtype='double')
    RhoValues = (r0*Lambda*np.power(np.cos(Gamma0),2))/(1-np.cos(ThetaValues)+Lambda*np.cos(ThetaValues+Gamma0))

    XValues = RhoValues * np.cos(ThetaValues)
    YValues = RhoValues * np.sin(ThetaValues)

    Range = 2*r0*np.arctan((Lambda*np.sin(Gamma0)*np.cos(Gamma0))/(1-Lambda*np.power(np.cos(Gamma0),2)))

    return XValues, YValues, Range

def Run():

    V0 = np.int64(np.sqrt(EarthGravCTE*(1-np.cos(ThetaD))/(r0*np.cos(Gamma0)*(np.cos(Gamma0)-np.cos(ThetaD+Gamma0)))))

    XValues1, YValues1, Range1 = ComputeTrajectory(V0,Gamma0)
    DV = float(MECOAcceleration)*9.80665*1/float(SamplingFrequency)
    V0 = np.int64(V0+DV)
    XValues2, YValues2, Range2 = ComputeTrajectory(V0+DV,Gamma0)
    DeltaRange = np.abs(Range2-Range1)
    print("DeltaRange", round(DeltaRange/1000,2), "  [km]")

    ThetaValues = np.linspace(start=0, stop=2*np.pi, num=250)
    XEarth = RadiusEarth * np.cos(ThetaValues) 
    YEarth = RadiusEarth * np.sin(ThetaValues)

    CenterX = 0
    CenterY = 0


    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.set_title('Ballistic trayectory')
    ax1.set_xlabel('X coord')
    ax1.set_ylabel('Y coord')
    ax1.plot(XValues1, YValues1, 'r')
    ax1.plot(XValues2, YValues2, 'g')
    ax1.plot(XEarth, YEarth, 'b')
    ax1.scatter(CenterX, CenterY, s=40)
    ax1.set_aspect(aspect=1)
    plt.show()

Run()


#LabelSpacingX = 250
#LabelSpacingY = 75

#root= tk.Tk()

#canvas1 = tk.Canvas(root, width = 800, height = 800)
#canvas1.pack()


#LabelParameters = tk.Label(root, text="Parameters", fg='red', font=("Helvetica", 16))
#LabelParameters.place(x=100, y=20)


##Sampling frequency
#LabelSamplingFrequency = tk.Label(root, text="Sampling frequency", fg='black', font=("Helvetica", 12))
#LabelSamplingFrequency.place(x=50, y=25+LabelSpacingY)
#EntrySamplingFrequency = tk.Entry(root, textvariable=SamplingFrequency, bd=3)
#EntrySamplingFrequency.insert(0,"2")
#EntrySamplingFrequency.place(x=50+LabelSpacingX, y=25+LabelSpacingY)

#MECO = 2
##MECO acceleration
##LabelMECOaccel = tk.Label(root, text="MECO acceleration", fg='black', font=("Helvetica", 12))
##LabelMECOaccel.place(x=50, y=25+2*LabelSpacingY)
##EntryMECOaccel = tk.Entry(root, textvariable=MECO, bd=3)
##EntryMECOaccel.insert(0,"2")
##EntryMECOaccel.place(x=50+LabelSpacingX, y=25+2*LabelSpacingY)

##Earth angle
#LabelThetaD = tk.Label(root, text="Earth angle", fg='black', font=("Helvetica", 12))
#LabelThetaD.place(x=50, y=25+3*LabelSpacingY)
#EntryThetaD = tk.Entry(root, textvariable=ThetaD, bd=3)
#EntryThetaD.insert(0,"2")
#EntryThetaD.place(x=50+LabelSpacingX, y=25+3*LabelSpacingY)

##Run button
#ButtonRun = tk.Button(root, text="Run", fg="red",command=Run, font=("Helvetica", 14))
#ButtonRun.place(x=50+0.5*+LabelSpacingX, y=25+4*LabelSpacingY)

#root.mainloop()
