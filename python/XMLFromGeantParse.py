#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 22 12:41:25 2019

@author: lucamonaco
"""
from xml.dom import minidom
import math
import numpy as np

class XMLFromGeantParse:
    
    def __init__(self, path):        
        self.path = path
        self.xmldoc = minidom.parse(path) #Set the file to be parsed
        #Here's how i thought: each of the three following vectors have a number of elements
        #that equals the number of histograms in a xml file
        self.HistogramInformations=[] #vector of each histograms info
        self.HistogramBinsCenter=[] #vector of each histograms bin centers (for our purposes, it's rendundant data)
        self.HistogramEntries=[] #vector of each histograms molteplicities
        self.depths=[]
        #remember: we have number of depths * number of secundaries histograms every xml file
        
    def AppendToArray(self,vet1,vet2):    
        for elem in vet2:
            vet1.append(elem)
        return vet1
    
    def Parse(self): #this is the xml parsing, i don't feel like i need to comment it to you too much, it works
        #if you have problems with this code, just tell me. At the end of the procedure you find some useful comments on data structure
        HistogramList = self.xmldoc.getElementsByTagName('histogram1d') #List of the 1D histograms of the file
        #use the histogram list index to enter the following arrays
        for histogram in HistogramList:
            #histrogram info
            actualInfo=[]
            Title=histogram.attributes['title'].value
            NumberOfBins=histogram.getElementsByTagName('axis')[0].attributes['numberOfBins'].value
            Min=histogram.getElementsByTagName('axis')[0].attributes['min'].value
            Max=histogram.getElementsByTagName('axis')[0].attributes['max'].value
            actualInfo=self.AppendToArray(actualInfo,[Title,NumberOfBins,Min,Max])
        
            Statistics=histogram.getElementsByTagName('statistics')[0]
            numberofEntries=Statistics.attributes['entries'].value
            mean=Statistics.getElementsByTagName('statistic')[0].attributes['mean'].value
            rms=Statistics.getElementsByTagName('statistic')[0].attributes['rms'].value
            actualInfo=self.AppendToArray(actualInfo,[numberofEntries,mean,rms])
            self.HistogramInformations.append(actualInfo)
            #histogram bins info
            binsBorder=histogram.getElementsByTagName('axis')[0].getElementsByTagName('binBorder')
            actualBins=[]
            actualBins.append(Min)
            for binBorder in binsBorder:
                actualBins.append(binBorder.attributes['value'].value)
            actualBins.append(Max)
            
            actualCenters=[]
            for i in range(0,len(actualBins)-1): #this is just to write the bins centers like they are reported in the cross section files
                #there must some better way to write this but... for now it suites our goals
                valore=math.sqrt(float(actualBins[i])*float(actualBins[i + 1]))
                if valore<10**(-2):
                    valore=round(valore,9)
                elif valore<10**(-2):
                    valore=round(valore,9)
                elif valore<10**(-1):
                    valore=round(valore,8)
                elif valore<1:
                    valore=round(valore,7)
                elif valore<10:
                    valore=round(valore,6)
                elif valore<10**2:
                    valore=round(valore,5)
                elif valore<10**3:
                    valore=round(valore,4)
                elif valore<10**4:
                    valore=round(valore,3)
                elif valore<10**5:
                    valore=round(valore,2)
                elif valore<10**6:
                    valore=round(valore,1)
                actualCenters.append([actualBins[i],actualBins[i + 1],str(valore)])
            self.HistogramBinsCenter.append(actualCenters)
            
            #histogram entries info
            bins1D=histogram.getElementsByTagName('data1d')[0].getElementsByTagName('bin1d')    
            actualEntries=[]
            for bin1D in bins1D:
                #here i parse only the molteplicities of the physics of our interest, so i avoid underflows and overlows
                if bin1D.attributes['binNum'].value!='UNDERFLOW' and bin1D.attributes['binNum'].value!='OVERFLOW':
                    binNum=bin1D.attributes['binNum'].value
                    entries=bin1D.attributes['entries'].value
                    height=bin1D.attributes['height'].value
                    error=bin1D.attributes['error'].value
                    weightedMean=bin1D.attributes['weightedMean'].value
                    try:
                        weightedRms=bin1D.attributes['weightedRms'].value
                    except:
                        weightedRms=weightedMean
                    actualEntries.append(self.AppendToArray([],[binNum,entries,height,error,weightedMean, weightedRms]))
            self.HistogramEntries.append(actualEntries)

            for i in range(0,len(self.HistogramInformations),10): #here i create the depth file      
                d=self.HistogramInformations[i][0].split("_")[0][1:]
                if not d in self.depths:
                    self.depths.append(d)
            
    
#After the parse, the three vectors defined in the init() have elements defined in the following way
#I take a random histogram with an index "index"

#HistogramInformations[index]=['D195.57_p_noweight',    Depth_primary_weight
#                              '180',                   Number of bins
#                              '0.001000000000000000020816682',       min energy in MeV
#                              '999999.9999999833526089787',          max energy in MeV
#                              '792345',                              Sum of particles in all bins
#                              '1204.605253768964303162647',          error
#                              '2147.32071845167320134351']           weighted mean
#
#HistogramBinsCenter[index]=[['0.001000000000000000020816682', '0.001122018454301963470004511', '0.001059254'],
#                            ['0.001122018454301963470004511', '0.001258925411794167056184213', '0.001188502'],
#                            ['0.001258925411794167056184213', '0.001412537544622753963793893', '0.001333521'],
#                            ...] 
#So a histogram at a certain index, is associated with a vector of [LowerBinValue, HigherBinValue, GeometricalCenter]
#Since we use the same bins for every histogram, there will be the same data for different indeces. I made it up this way in order to be flexible for the future.
#
#HistogramEntries[index]=[...
#                         ['68', '574', '574', '23.95829710142187707333505', '2.670207578362679079475583', '0.08795169844441597106765585'],
#                         ['69', '696', '696', '26.38181191654583912509224', '2.988102120365469627216726', '0.1002680385486264952321633'],
#                         ['70', '842', '842', '29.01723625709381693127398', '3.360687646771639780496344', '0.112026342141240992100748'],
#                         ...]
#So a histogram at a certain index, is associated with a vector of [BinNumber, RawMolteplicity, WeightedMolteplicity, error, WeightedMean, WeightedRMS]
#Of course if the histogram is not weighted, RawMolteplicity=WeighterMolteplicity. The latter is called "height" in the xml file.            
            
    def PlotSpectra(self,entries): #just to plot molteplicity in function of energy and not bins ID
        bins=np.logspace(-3,6,180, base=10)
        height=np.zeros(180)
        for entry in entries:
            height[int(entry[0])-1]=float(entry[2])
        height[-1]=0
        return bins, height