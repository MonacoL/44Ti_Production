#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 31 13:44:42 2019

@author: lucamonaco
"""
import csv 
import XMLFromGeantParse as XMLFile

class ComputeS():
    def __init__(self, pathCSFiles, pathHisto, weight, pathOutput, aimSpecies, today):
        if weight==0:
            self.weight="noweight"
        else:
            self.weight="weight"
        self.radiuses=[]
        self.depths=[]
        self.pathOutput=pathOutput #where to save output files
        self.aimSpecies=aimSpecies #44Ti or 26Al or anything you need, it's just for writing the output file top string
        self.today=today
        self.EnergyPrimaries=[]
        self.PrimaryParticleType=""
        #For detailed information about histogram files parseing, go to XMLFromGeantParse.py
        #Here these three following vectors are intended to contain data of ALL xml files, every index is a file
        self.HistogramInformations=[]
        self.HistogramEntries=[]
        self.HistogramBinsCenter=[]
        for path in pathHisto: #pathHisto is a vector of xml files paths
            self.ReadHistogramFile(path)
        self.radiuses.append(float(self.depths[-1]))
        for h in self.depths[:-1]: #i convert depths into radiuses, useful when i apply the correcting factor on production
            self.radiuses.append(float(self.depths[-1])-float(h))            
        #this two following vectors have a number of elements equal to the number of cross sections files
        self.CrossSectionSecondaryParticle=[] #every element is the secondary particle associated with a certain cross section file
        self.CrossSectionData=[] #every element contains the data from a certain cross-section file in the form defined by the procedure ReadCrossSectionFile
        for file in pathCSFiles:
            secParticle, data = self.ReadCrossSectionFile(file)
            self.CrossSectionData.append(data)
            self.CrossSectionSecondaryParticle.append(secParticle)
        self.Smatrix=[[0 for x in range(len(self.depths))] for y in range(len(self.EnergyPrimaries))]  #here i just define an all zero yield function matrix, that is filled later

    def ReadCrossSectionFile(self,path):
        datas=[]
        secParticle=path.split("/")[-1].split("_")[3]
        with open (path, newline='', encoding='cp1252') as csvreader:
            reader = csv.reader(csvreader, delimiter='\t')
            datas=list(enumerate(reader))
        bincenter=[]
        cs=[]
        for data in datas[2:]: #avoid first two raws, they're unuseful strings
            bincenter.append(float(data[1][0])) #vector of bin centers
            cs.append(float(data[1][1])) #vector of cross-section values
        return secParticle, [bincenter,cs]
            
    def ReadHistogramFile(self,pathHisto): #pathHisto now here is a local variable with the path of a single xml file
        EnergyFile=XMLFile.XMLFromGeantParse(pathHisto)
        EnergyFile.Parse()
        AvoidExtension=pathHisto.split(".")[-2] #-1 is the extension, -2 is the path+filename
        temp=AvoidExtension.split("_")
        if str(temp[0][-1])=="p":
            self.PrimaryParticleType="protons"
        else:
            self.PrimaryParticleType="alphas"
        self.EnergyPrimaries.append(int(temp[1]))            
        self.HistogramInformations.append(EnergyFile.HistogramInformations)
        self.HistogramEntries.append(EnergyFile.HistogramEntries)
        self.HistogramBinsCenter.append(EnergyFile.HistogramBinsCenter)
        if self.depths==[]:
            self.depths=EnergyFile.depths
            
    def GetHisto(self, primaryEnergy, depth, secondaryParticle): #get the histo of a particular primary energy, at a certain depth, for a certain secondary particle
        IDprimaryEnergy=self.EnergyPrimaries.index(primaryEnergy)
        Histos=self.HistogramInformations[IDprimaryEnergy]
        IDHisto=50000 #index stupidly high, so if the histogram is not found i get an error
        for info in Histos:
            title=info[0].split("_")            
            if title[0][1:]==str(depth) and title[1]==secondaryParticle and title[2]==self.weight:                
                IDHisto=Histos.index(info)                
                break
        return self.HistogramInformations[IDprimaryEnergy][IDHisto], self.HistogramBinsCenter[IDprimaryEnergy][IDHisto], self.HistogramEntries[IDprimaryEnergy][IDHisto]
    
    def FindHeightfromBinNumber(self, histoentries, BinNumber): #provide height of a histogram of a certain bin
        height=0
        for entry in histoentries:
            if int(entry[0])==int(BinNumber):
                height=entry[2] #the height, not the molteplicity, because the histo can be weighted
                break
        return height
    
    def GetMulteplicity(self, SecParticlesNumber, minBin, maxBin): #for every bin, for every depth
        factor=1.0 #to take in account alpha primaries, in case
        if self.PrimaryParticleType=='a':
            factor=1/4 #it's the case
        return float(SecParticlesNumber)*factor/(float(maxBin)-float(minBin))
    

    def GetS(self, primaryEnergy, depth): #for a primary energy, for a depth
        S=0.0
        for secParticles in self.CrossSectionSecondaryParticle: #sum over secondary particles                      
            currentHistoInfo, currentHistoBinCenter, currentHistoEntries=self.GetHisto(primaryEnergy,depth,secParticles)
            csData = self.CrossSectionData[self.CrossSectionSecondaryParticle.index(secParticles)]
            for bincenter in csData[0]: #sum over energy bins of secondary particles
                binvect=currentHistoBinCenter[csData[0].index(bincenter)]
                binMin=binvect[0]
                binMax=binvect[1]
                height=self.FindHeightfromBinNumber(currentHistoEntries,csData[0].index(bincenter)+1)
                S+=self.GetMulteplicity(height, binMin, binMax)*csData[1][csData[0].index(bincenter)]
        return S    
    
    def GetScalingFactor(self, depth): #get scaling factor for a certain depth
        ind=self.depths.index(depth)
        return (float(self.depths[-1])/self.radiuses[ind])**2    
    
    def ComputeSMatrix(self): #filling the yield function matrix defined as zeros in init(). Just call GetS ciclying for every energy and depths
        for i in range(0,len(self.EnergyPrimaries)):
            for h in range(0,len(self.depths)):
                self.Smatrix[i][h]=self.GetScalingFactor(self.depths[h])*self.GetS(self.EnergyPrimaries[i], self.depths[h])
        #write output file
        path=self.pathOutput+"yf_"+self.aimSpecies+"_prim_"+self.PrimaryParticleType+"_"+self.today+".txt"
        file_object  = open(path, "w")
        file_object.write("Yield function of production of Ti44 by protons, neutrons, alphas, [(Ti44 atoms * cm2) / (g * prim. part. nucleon)] (computed with Geant4.10).\n")
        file_object.write("The primaries are "+self.PrimaryParticleType+".\n")
        strToWrite="Energy[GeV/nuc],depths[g/cm2]: "
        for h in self.depths:
            strToWrite+=str(h)+" "
        strToWrite=strToWrite[:-1]
        strToWrite+="\n"
        file_object.write(strToWrite)
        for i in range(0,len(self.EnergyPrimaries)):
            strToWrite=str(float(self.EnergyPrimaries[i]*(10**(-3)))) + " "            
            for h in range(0,len(self.depths)):
                strToWrite+=str("%1.5E"% (self.Smatrix[i][h]))+" "
            strToWrite=strToWrite[:-1]
            strToWrite+="\n"
            file_object.write(strToWrite)
        file_object.close()
        
        return path