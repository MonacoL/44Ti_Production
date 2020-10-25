#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 14:10:35 2019

@author: lucamonaco
"""
import math
import numpy
import ComputeQ as PRODUCTION
from scipy.integrate import simps
from scipy.integrate import trapz
import matplotlib.pyplot as plt
import re
import mathStuff
from scipy.interpolate import interp1d
import numpy as np

class ComputeA():
    def __init__(self, pathYdata, pathPHIdata, Lambda, spectraNumber, h):
        self.h=h
        self.Lambda=Lambda
        self.pathYdata=pathYdata #vector of yield functions file paths
        self.pathPHIdata=pathPHIdata #vector of phi file paths
        self.TIMEdata=[] 
        self.PHIdata=[]
        self.SpectraNumber=spectraNumber
        if self.pathPHIdata!=[]:
            self.TIMEdata, self.PHIdata = self.Read_Phi_Series() #it fills time vector and phi vector, from the phi files you pass
    
    def Read_Phi_Series(self):
        file_data = []
        time=[]
        phi=[]
        for path in self.pathPHIdata: #I can pass more than 1 file, in that case, data is appended
            file_object  = open(path, "r")
            for val in file_object.readlines():
                file_data.append(val.replace('\n','').replace('\t'," "))
        temp=sorted(file_data, key = lambda x: (float(x.split(" ")[0]))) #sort data in terms of time, it's actually useful when i have more than 1 file
        for row in temp:
            rowsplit=re.sub(' +', ' ',row).split(" ") #nevermind this, it's just to manage the sintax in the string data
            time.append(float(rowsplit[0]))
            phi.append(float(rowsplit[1]))
        #If i'm not satisfied with my phi files, i interpolate data to have a denser series
        f = interp1d(time, phi)
        t=np.linspace(time[0],time[-1], 3600)
        p=[]
        for T in t:
            p.append(f(T))
        return t.tolist(), p
    
    def GetPHI(self,t):
        index=50000000 #index stupidly high to give error if the time t is not found in the Time vectore
        for time in self.TIMEdata:
            if time==t:
                index=self.TIMEdata.index(time)
                break
        return self.PHIdata[index]
    
    def GetA(self,Tmax):           
        t_first=[]
        for time in self.TIMEdata:
            if time<=Tmax:
                t_first.append(time)        

        vec_Q=[]
        vec_exp=[]
        for time in t_first:
            phi=self.GetPHI(time)
            obj_ComputeQ=PRODUCTION.ComputeQ(self.pathYdata,phi,self.SpectraNumber,0)
            for hindex in range(0,len(obj_ComputeQ.YData[0][2])-1):
                if self.h==obj_ComputeQ.YData[0][2][hindex]: #if required depth is in depth grid, just perform production
                    vec_Q.append(obj_ComputeQ.Perform_PowerFunction(self.h))
                if self.h<float(obj_ComputeQ.YData[0][2][hindex+1]) and self.h>float(obj_ComputeQ.YData[0][2][hindex]): #if it is not, take nearest lower and higher depths, perform productions, and interpolate
                    #I did this not to be bound to select the exact depths in the depth grid when computing the production
                    leftProd=obj_ComputeQ.Perform_PowerFunction(obj_ComputeQ.YData[0][2][hindex])
                    rightProd=obj_ComputeQ.Perform_PowerFunction(obj_ComputeQ.YData[0][2][hindex+1])
                    g = interp1d([float(obj_ComputeQ.YData[0][2][hindex]), float(obj_ComputeQ.YData[0][2][hindex+1])], [leftProd, rightProd])
                    vec_Q.append(g(self.h))
            vec_exp.append(math.exp(self.Lambda*(time-Tmax)))
        return self.Lambda*mathStuff.PowerFunction_Integration(numpy.array(vec_Q)*numpy.array(vec_exp), t_first)
    
    def A_vector(self): #unused
        A=[]
        for time in self.TIMEdata:
            A.append(self.GetA(time))
        return self.TIMEdata, A
        