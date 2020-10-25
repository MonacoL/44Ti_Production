#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 31 11:15:45 2019

@author: lucamonaco
"""
import ComputeS as YIELDFUNCTION
import datetime

pathCrossSectionFiles=[]
path=[]



#VARIABLES TO PLAY WITH
radius="50cm"
category="LL"
#########################



if category=="H":
    pathCrossSectionFiles.append('../cross_sections/Ti44_Sint_Hch_a_20190717.csv')
    pathCrossSectionFiles.append('../cross_sections/Ti44_Sint_Hch_n_20190717.csv')
    pathCrossSectionFiles.append('../cross_sections/Ti44_Sint_Hch_p_20190717.csv')
    #pathCrossSectionFiles.append('../cross_sections/Ti44_Sint_Hch_piminus_20190717.csv')
    #pathCrossSectionFiles.append('../cross_sections/Ti44_Sint_Hch_piplus_20190717.csv')
elif category=="L":
    pathCrossSectionFiles.append('../cross_sections/Ti44_Sint_Lch_a_20190717.csv')
    pathCrossSectionFiles.append('../cross_sections/Ti44_Sint_Lch_n_20190717.csv')
    pathCrossSectionFiles.append('../cross_sections/Ti44_Sint_Lch_p_20190717.csv')
    #pathCrossSectionFiles.append('../cross_sections/Ti44_Sint_Lch_piminus_20190717.csv')
    #pathCrossSectionFiles.append('../cross_sections/Ti44_Sint_Lch_piplus_20190717.csv')    
else:
    pathCrossSectionFiles.append('../cross_sections/Ti44_Sint_LLch_a_20190717.csv')
    pathCrossSectionFiles.append('../cross_sections/Ti44_Sint_LLch_n_20190717.csv')
    pathCrossSectionFiles.append('../cross_sections/Ti44_Sint_LLch_p_20190717.csv')
    #pathCrossSectionFiles.append('../cross_sections/Ti44_Sint_LLch_piminus_20190717.csv')
    #pathCrossSectionFiles.append('../cross_sections/Ti44_Sint_LLch_piplus_20190717.csv')

now=datetime.datetime.today().strftime("%Yy%mm%dg_%Hh%Mm%Ss")

pathHistogramFiles=[] #one file every primary energy
pathHistogramFiles.append('../histograms/H/'+radius+'/a_30.xml')
pathHistogramFiles.append('../histograms/H/'+radius+'/a_100.xml')
pathHistogramFiles.append('../histograms/H/'+radius+'/a_180.xml')
pathHistogramFiles.append('../histograms/H/'+radius+'/a_300.xml')
pathHistogramFiles.append('../histograms/H/'+radius+'/a_560.xml')
pathHistogramFiles.append('../histograms/H/'+radius+'/a_1000.xml')
pathHistogramFiles.append('../histograms/H/'+radius+'/a_3000.xml')
pathHistogramFiles.append('../histograms/H/'+radius+'/a_10000.xml')
pathHistogramFiles.append('../histograms/H/'+radius+'/a_30000.xml')
pathHistogramFiles.append('../histograms/H/'+radius+'/a_100000.xml')

obj_ComputeS=YIELDFUNCTION.ComputeS(pathCrossSectionFiles, pathHistogramFiles,1, "../yield_functions/44Ti/"+category+"/"+radius+"/", "Ti44",now)#, Composition)
path.append(obj_ComputeS.ComputeSMatrix())

pathHistogramFiles=[]
pathHistogramFiles.append('../histograms/H/'+radius+'/p_30.xml')
pathHistogramFiles.append('../histograms/H/'+radius+'/p_100.xml')
pathHistogramFiles.append('../histograms/H/'+radius+'/p_180.xml')
pathHistogramFiles.append('../histograms/H/'+radius+'/p_300.xml')
pathHistogramFiles.append('../histograms/H/'+radius+'/p_560.xml')
pathHistogramFiles.append('../histograms/H/'+radius+'/p_1000.xml')
pathHistogramFiles.append('../histograms/H/'+radius+'/p_3000.xml')
pathHistogramFiles.append('../histograms/H/'+radius+'/p_10000.xml')
pathHistogramFiles.append('../histograms/H/'+radius+'/p_30000.xml')
pathHistogramFiles.append('../histograms/H/'+radius+'/p_100000.xml')
                                                                                                                                    
obj_ComputeS=YIELDFUNCTION.ComputeS(pathCrossSectionFiles, pathHistogramFiles,1, "../yield_functions/44Ti/"+category+"/"+radius+"/", "Ti44",now)#, Composition)
path.append(obj_ComputeS.ComputeSMatrix())

print(path)

