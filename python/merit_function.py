#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 17:09:13 2019

@author: lucamonaco
"""

from scipy.optimize import minimize
import math
import numpy as np
import re
from scipy.interpolate import interp1d

def Read_Phi_Series(pathPHIdata):
    file_data = []
    time=[]
    phi=[]
    for path in pathPHIdata:
        file_object  = open(path, "r")
        for val in file_object.readlines():
            file_data.append(val.replace('\n','').replace('\t'," "))
    temp=sorted(file_data, key = lambda x: (float(x.split(" ")[0])))
    for row in temp:
        rowsplit=re.sub(' +', ' ',row).split(" ")
        time.append(float(rowsplit[0]))
        phi.append(float(rowsplit[1]))
    f = interp1d(time, phi)
    t=np.linspace(time[0],time[-1], 3600)
    p=[]
    for T in t:
        p.append(f(T))
    return t.tolist(), p

SpectraNumber=1
T_BM, PHI_BM=Read_Phi_Series(["../phi_series/Fi_temp.txt"])
f1 = interp1d(T_BM, PHI_BM)
T_TOCONVERT, PHI_TOCONVERT=Read_Phi_Series(["../phi_series/phi_composite_20170719.csv"])
f2 = interp1d(T_TOCONVERT, PHI_TOCONVERT)

PHI1=[]
PHI2=[]
for t in np.linspace(1405,1900,500*12):
    PHI1.append(f1(t))
    PHI2.append(f2(t))
    
def Jlis_Vos(E): #E in GeV
    #unmodulated spectra by Vos and Potgieter
    Jlis=2.70*(E**1.12)*((E+0.67)/1.67)**(-3.93)
    #v=0.0
    c=299792458
    E=E*(1.60218*1e-10) #converts energy in J
    m=1.6726219*1e-27 #kilograms
    betaSquare=1-((m*(c**2))/(E+m*(c**2)))**2 
    return Jlis/betaSquare
 
def Jlis_Burger(E): #E in GeV
    #unmodulated spectra by Burger 2000
    E0=0.938
    P_T=math.sqrt(E*(E + 2*E0))
    Jlis=1.9*1e4*(P_T**(-2.78))/(1 + 0.4866*(P_T**(-2.51)))
    return Jlis
   
def J(E, phi, SpectraNumber):
    factorUnitMeasure=1.0
    Unmodulated=1.0
    ForceField=1.0       
    Tr=0.938 #Gev/nucleon       
    phi_i=phi
    if SpectraNumber==1: 
        #Spectra by Usoskin 2011
        factorUnitMeasure=1/10
        phi_i=phi_i*1e-3 #to convert in GeV
        Unmodulated=Jlis_Vos(E+phi_i)
    elif SpectraNumber==2: 
        #Spectra by Burger et al. [2000]:
        factorUnitMeasure=1e-4
        phi_i=phi_i*1e-3 #to convert in GeV
        Unmodulated=Jlis_Burger(E+phi_i)
    ForceField=(E*(E + 2*Tr))/((E+phi_i)*(E + 2*Tr + phi_i))            
    return factorUnitMeasure*Unmodulated*ForceField  
    
def MeritFunction(x):
    return sum(np.array([J(1,x[0]*PHI2[i]+x[1],SpectraNumber)/J(1,PHI1[i],SpectraNumber)-1])**2 for i in range(0,len(PHI2)))

x0=[1,1]
myoptions={'disp':True}
results=minimize(MeritFunction,x0,options=myoptions)
#print("Solution: x=%f"%results.x)