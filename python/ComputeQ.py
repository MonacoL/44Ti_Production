#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 28 16:27:32 2019

@author: lucamonaco
"""
import math
import numpy
from scipy.integrate import simps
from scipy.integrate import trapz
import csv

class ComputeQ():
    def __init__(self, pathYFiles, phi, spectraNumber, limitations):
        self.phi=phi #phi time series
        self.YData=[] #vector of yield functions
        self.SpectraNumber=spectraNumber #way to select the wanted spectra
        self.Limitations=limitations
        self.depths=[]
        for file in pathYFiles:
            self.YData.append(self.ReadYieldFunctionFile(file))        
    
    def ReadYieldFunctionFile(self,path): #i take a yield function file and i put it into a matrix
        particle=""
        if "protons" in path:
            particle="p"
        elif "alphas" in path:
            particle="alpha"
        file_object  = open(path, "r")
        file_data = []
        for val in file_object.readlines():
            file_data.append(val)
        file_object.close()
        depth=file_data[2].split(" ")[1:]
        depth[-1]=depth[-1][:-1] #eliminate last /n from last depth
        if self.depths==[]:
            self.depths=depth
        #depth=[float(h) for h in depth]
        energy=[]
        row=len(file_data)-3
        columns=len(depth)
        output = [[0 for x in range(columns)] for y in range(row)]
        if self.Limitations==1:            
            for data in file_data[3:]:
                temp=data.split(" ")
                if float(temp[0])<=10:
                    energy.append(float(temp[0]))
                    for Y in temp[1:]:
                        output[file_data[3:].index(data)][temp[1:].index(Y)]=float(Y.replace("\n",""))
        else:
            for data in file_data[3:]:
                temp=data.split(" ")
                energy.append(float(temp[0]))
                for Y in temp[1:]:
                    output[file_data[3:].index(data)][temp[1:].index(Y)]=float(Y.replace("\n",""))
        return [particle,energy,depth,output]
        #particle is the primary particles
        #energy is the vector of primary energies
        #depth is the vector of depths
        #output is the yield function
    
    def Jlis_VosPotgieter(self, E): #E in GeV
        #unmodulated spectra by Vos and Potgieter
        Jlis=2.70*(E**1.12)*((E+0.67)/1.67)**(-3.93)
        #v=0.0
        c=299792458
        E=E*(1.60218*1e-10) #converts energy in J
        m=1.6726219*1e-27 #kilograms
        betaSquare=1-((m*(c**2))/(E+m*(c**2)))**2 
        return Jlis/betaSquare
 
    def Jlis_Burger(self, E): #E in GeV
        #unmodulated spectra by Burger 2000
        E0=0.938
        P_T=math.sqrt(E*(E + 2*E0))
        Jlis=1.9*1e4*(P_T**(-2.78))/(1 + 0.4866*(P_T**(-2.51)))
        return Jlis
    
    def Jlis_Munoz(self, E): #E in Mev
        #unmodulated spectra by Munoz 1980 something
        A=9.9e8
        m=780*math.exp(E*(-2.5e-4))
        gamma=-2.65
        Jlis=A*((E+m)**gamma)
        return Jlis    
   
    def J(self, partType, E, phi): #we already checked this part together, it is correct
        factorUnitMeasure=1.0
        Unmodulated=1.0
        ForceField=1.0
        factorAlpha=1.0        
        Tr=0.938 #Gev/nucleon
        z=0.0
        a=0.0       
        if partType=="p":
            z=1
            a=1
        else: #alpha particle
            z=2
            a=4
            factorAlpha=0.353   #0.353 from Koldobsiy 2019     
        phi_i=(z/a)*phi
        if self.SpectraNumber==1: 
            #Spectra by Usoskin 2011
            factorUnitMeasure=1/10
            phi_i=phi_i*1e-3 #to convert in GeV
            Unmodulated=self.Jlis_VosPotgieter(E+phi_i)
        elif self.SpectraNumber==2:
            #Spectra by Munoz
            factorUnitMeasure=1/10
            E=E*1e3 #convert in MeV
            Tr=Tr*1e3
            Unmodulated=self.Jlis_Munoz(E+phi_i)
        elif self.SpectraNumber==3: 
            #Spectra by Burger et al. [2000]:
            factorUnitMeasure=1e-4
            phi_i=phi_i*1e-3 #to convert in GeV
            Unmodulated=self.Jlis_Burger(E+phi_i)
        ForceField=(E*(E + 2*Tr))/((E+phi_i)*(E + 2*Tr + phi_i))            
        return factorUnitMeasure*factorAlpha*Unmodulated*ForceField    

    def GetY_atFixedDepth(self,ydata,h): #vector of yield function values at fixed depth
        Y=[]
        for i in range(0,len(ydata[1])): #fixed h, runs over E
            Y.append(float(ydata[-1][i][ydata[2].index(h)]))
        return Y
    
    def Perform(self,h): #integration with python, not good even if i don't know why yet
        Q=0.0        
        for data in self.YData:
            J=[]
            for en in data[1]:
                J.append(float(self.J(data[0],en,self.phi)))
            Q+=math.pi*trapz(numpy.array(self.GetY_atFixedDepth(data,h))*numpy.array(J), data[1])
        return Q*60000 #conversion in dpm/kg
    
    def Perform_PowerFunction(self,h):
        Q=0.0        
        for data in self.YData:
            Y=[]
            J=[]
            YJ=[]
            YJE=[]
            for en in data[1]:
                J.append(float(self.J(data[0],en,self.phi)))
            J=numpy.array(J)
            Y=numpy.array(self.GetY_atFixedDepth(data,h))
            YJ=Y*J
            YJE=YJ*numpy.array(data[1])
            
            dYJE=[]
            log_dYJ=[]
            log_dE=[]
            I=[]
            for i in range(0,len(YJ)-1):
                dYJE.append(YJE[i + 1]-YJE[i])
                try:
                    log_dYJ.append(math.log(YJ[i + 1])-math.log(YJ[i]))
                except:
                    log_dYJ.append(0)                 
                log_dE.append(math.log(data[1][i + 1])-math.log(data[1][i]))
            
            for i in range(0,len(log_dYJ)):
                I.append(dYJE[i]/((log_dYJ[i]/log_dE[i])+1))
                
            Q+=math.pi*sum(q for q in I)
                
        return Q*60000 #conversion in dpm/kg     

    def Perform_PowerFunction_Matrix(self,h,phi):
        Q=0.0        
        for data in self.YData:
            Y=[]
            J=[]
            YJ=[]
            YJE=[]
            for en in data[1]:
                J.append(float(self.J(data[0],en,phi)))
            J=numpy.array(J)
            Y=numpy.array(self.GetY_atFixedDepth(data,h))
            YJ=Y*J
            YJE=YJ*numpy.array(data[1])
            
            dYJE=[]
            log_dYJ=[]
            log_dE=[]
            I=[]
            for i in range(0,len(YJ)-1):
                dYJE.append(YJE[i + 1]-YJE[i])
                try:
                    log_dYJ.append(math.log(YJ[i + 1])-math.log(YJ[i]))
                except:
                    log_dYJ.append(0)                 
                log_dE.append(math.log(data[1][i + 1])-math.log(data[1][i]))
            
            for i in range(0,len(log_dYJ)):
                I.append(dYJE[i]/((log_dYJ[i]/log_dE[i])+1))
                
            Q+=math.pi*sum(q for q in I)
                
        return Q   

    def GetProductionMatrix(self,filename, PHI, radius):
        f = open(filename, 'w+')
        with f:
            writer=csv.writer(f)
            writer.writerow(["Production rate of Ti-44 by GCR (all) in meteoroid "+radius+"."])
            writer.writerow(["Notes: LIS_VosPotgieter 2015"])
            writer.writerow(["Values=Production rates [atoms/gs], X=phi [MV], Y=depth [g/cm2]"])
            depths=[float(h) for h in self.depths]
            depths_row=["phi/depths"]
            for d in depths:
                depths_row.append(d)
            writer.writerow(depths_row)

            for phi in PHI:
                q_atFixedPhi=[phi]
                for d in self.depths:
                    q=self.Perform_PowerFunction_Matrix(d,phi)
                    q_atFixedPhi.append(q)
                writer.writerow(q_atFixedPhi)