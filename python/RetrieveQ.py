#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 28 18:12:29 2019

@author: lucamonaco
"""
import datetime
import ComputeQ as PRODUCTION
import matplotlib.pyplot as plt
import ComputeS as YIELDFUNCTION
import numpy as np
import math

def MNfit(phi):
    return 0.8 + 2.07 * np.exp(-0.00319*np.array(phi))

def YieldFunctionDepth(Ymatrix, EnergyRow):
    mat=np.array(Ymatrix)    
    n,m=np.shape(mat) #rows,columns
    Y=[]
    for j in range(0,m):
        Y.append(Ymatrix[EnergyRow][j])
    return Y

def YieldFunctionEnergy(Ymatrix, DepthColumn):
    mat=np.array(Ymatrix)    
    n,m=np.shape(mat) #rows,columns
    Y=[]
    for i in range(0,n):
        Y.append(Ymatrix[i][DepthColumn])
    return Y

def smooth(x,window_len,window='hanning'):
    """smooth the data using a window with requested size.
    
    This method is based on the convolution of a scaled window with the signal.
    The signal is prepared by introducing reflected copies of the signal 
    (with the window size) in both ends so that transient parts are minimized
    in the begining and end part of the output signal.
    
    input:
        x: the input signal 
        window_len: the dimension of the smoothing window; should be an odd integer
        window: the type of window from 'flat', 'hanning', 'hamming', 'bartlett', 'blackman'
            flat window will produce a moving average smoothing.

    output:
        the smoothed signal
        
    example:

    t=linspace(-2,2,0.1)
    x=sin(t)+randn(len(t))*0.1
    y=smooth(x)
    
    see also: 
    
    numpy.hanning, numpy.hamming, numpy.bartlett, numpy.blackman, numpy.convolve
    scipy.signal.lfilter
 
    TODO: the window parameter could be the window itself if an array instead of a string
    NOTE: length(output) != length(input), to correct this: return y[(window_len/2-1):-(window_len/2)] instead of just y.
    """

    if x.ndim != 1:
        raise (ValueError, "smooth only accepts 1 dimension arrays.")

    if x.size < window_len:
        raise (ValueError, "Input vector needs to be bigger than window size.")


    if window_len<3:
        return x


    if not window in ['flat', 'hanning', 'hamming', 'bartlett', 'blackman']:
        raise (ValueError, "Window is on of 'flat', 'hanning', 'hamming', 'bartlett', 'blackman'")


    s=np.r_[x[window_len-1:0:-1],x,x[-2:-window_len-1:-1]]
    #print(len(s))
    if window == 'flat': #moving average
        w=np.ones(window_len,'d')
    else:
        w=eval('np.'+window+'(window_len)')

    y=np.convolve(w/w.sum(),s,mode='valid')
#    return y
    if window_len % 2 == 0:
        return y[(int(window_len/2)-1):-(int(window_len/2))]
    else:
        return y[(int(window_len/2)):-(int(window_len/2))]

now=datetime.datetime.today().strftime("%Yy%mm%dg_%Hh%Mm%Ss")

################ METEORITES ARTICLE TARICCO #######################

# #26al
# csH=[]
# csH.append('../cross_sections/Al26_Sint_H_a_20190829.csv')
# csH.append('../cross_sections/Al26_Sint_H_n_20190829.csv')
# csH.append('../cross_sections/Al26_Sint_H_p_20190829.csv')
# csH.append('../cross_sections/Al26_Sint_H_piminus_20190909.csv')
# csH.append('../cross_sections/Al26_Sint_H_piplus_20190909.csv')
# csL=[]
# csL.append('../cross_sections/Al26_Sint_L_a_20190829.csv')
# csL.append('../cross_sections/Al26_Sint_L_n_20190829.csv')
# csL.append('../cross_sections/Al26_Sint_L_p_20190829.csv')
# csL.append('../cross_sections/Al26_Sint_L_piminus_20190909.csv')
# csL.append('../cross_sections/Al26_Sint_L_piplus_20190909.csv')
# csLL=[]
# csLL.append('../cross_sections/Al26_Sint_LL_a_20190829.csv')
# csLL.append('../cross_sections/Al26_Sint_LL_n_20190829.csv')
# csLL.append('../cross_sections/Al26_Sint_LL_p_20190829.csv')
# csLL.append('../cross_sections/Al26_Sint_LL_piminus_20190909.csv')
# csLL.append('../cross_sections/Al26_Sint_LL_piplus_20190909.csv')

# chosencs=[csH,"H"] #change csLL csL csH to provide production curve for every class
# meteorites=[['40cm',chosencs[0],[1,3,5,10,15,20,30,40,50,60,70,80,90,100,110,120,130,135,141.6], "AlbaretoNew"],
#             ['50cm',chosencs[0],[1,3,5,10,15,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,186], "Mooresfort"],
#             ['85cm',chosencs[0],[1,3,5,10,15,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250,260,270,280,290,300,310,316.2], "CharsonvilleNew"],
#             ['120cm',chosencs[0],[1,3,5,10,15,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250,260,270,280,290,300,310,320,330,340,350,360,370,380,400,410,420,430,446.4], "Agen"],            
#             ['75cm',chosencs[0],[1,3,5,10,15,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250,260,270,279], "Gruneberg"],
#             ['35cm',chosencs[0],[1,3,5,10,15,20,30,40,50,60,70,80,90,100,110,124.6], "Alfaniello"],
#             ['23cm',chosencs[0],[1,3,5,10,15,20,30,40,50,60,70,85.56], "Lancon"],
#             ['20cm',chosencs[0],[1,3,10,20,30,40,50,60,71.6], "TurinH6"]]

# for meteorite in meteorites:
#     pathYFiles=[]
#     pathHistogramFiles=[] #one file every primary energy
#     pathHistogramFiles.append('../histograms/'+meteorite[-1]+'/a_10_'+meteorite[-1]+'.xml')
#     pathHistogramFiles.append('../histograms/'+meteorite[-1]+'/a_30_'+meteorite[-1]+'.xml')
#     pathHistogramFiles.append('../histograms/'+meteorite[-1]+'/a_100_'+meteorite[-1]+'.xml')
#     pathHistogramFiles.append('../histograms/'+meteorite[-1]+'/a_180_'+meteorite[-1]+'.xml')
#     pathHistogramFiles.append('../histograms/'+meteorite[-1]+'/a_300_'+meteorite[-1]+'.xml')
#     pathHistogramFiles.append('../histograms/'+meteorite[-1]+'/a_560_'+meteorite[-1]+'.xml')
#     pathHistogramFiles.append('../histograms/'+meteorite[-1]+'/a_1000_'+meteorite[-1]+'.xml')
#     pathHistogramFiles.append('../histograms/'+meteorite[-1]+'/a_3000_'+meteorite[-1]+'.xml')
#     pathHistogramFiles.append('../histograms/'+meteorite[-1]+'/a_10000_'+meteorite[-1]+'.xml')
#     pathHistogramFiles.append('../histograms/'+meteorite[-1]+'/a_30000_'+meteorite[-1]+'.xml')
#     pathHistogramFiles.append('../histograms/'+meteorite[-1]+'/a_100000_'+meteorite[-1]+'.xml')
#     obj_ComputeS=YIELDFUNCTION.ComputeS(meteorite[1], pathHistogramFiles,1, "../yield_functions/26Al/"+chosencs[1]+"/"+meteorite[0]+"/", "26Al",now,meteorite[2])#, Composition,9)
#     pathYFiles.append(obj_ComputeS.ComputeSMatrix())
    
#     pathHistogramFiles=[] #one file every primary energy
#     pathHistogramFiles.append('../histograms/'+meteorite[-1]+'/p_10_'+meteorite[-1]+'.xml')
#     pathHistogramFiles.append('../histograms/'+meteorite[-1]+'/p_30_'+meteorite[-1]+'.xml')
#     pathHistogramFiles.append('../histograms/'+meteorite[-1]+'/p_100_'+meteorite[-1]+'.xml')
#     pathHistogramFiles.append('../histograms/'+meteorite[-1]+'/p_180_'+meteorite[-1]+'.xml')
#     pathHistogramFiles.append('../histograms/'+meteorite[-1]+'/p_300_'+meteorite[-1]+'.xml')
#     pathHistogramFiles.append('../histograms/'+meteorite[-1]+'/p_560_'+meteorite[-1]+'.xml')
#     pathHistogramFiles.append('../histograms/'+meteorite[-1]+'/p_1000_'+meteorite[-1]+'.xml')
#     pathHistogramFiles.append('../histograms/'+meteorite[-1]+'/p_3000_'+meteorite[-1]+'.xml')
#     pathHistogramFiles.append('../histograms/'+meteorite[-1]+'/p_10000_'+meteorite[-1]+'.xml')
#     pathHistogramFiles.append('../histograms/'+meteorite[-1]+'/p_30000_'+meteorite[-1]+'.xml')
#     pathHistogramFiles.append('../histograms/'+meteorite[-1]+'/p_100000_'+meteorite[-1]+'.xml')
#     obj_ComputeS=YIELDFUNCTION.ComputeS(meteorite[1], pathHistogramFiles,1, "../yield_functions/26Al/"+chosencs[1]+"/"+meteorite[0]+"/", "26Al",now,meteorite[2])#, Composition,9)
#     pathYFiles.append(obj_ComputeS.ComputeSMatrix())
#     print(meteorite[0], pathYFiles)



###########44TI
#csH=[]
#csLL=[]
#csH.append('../cross_sections/Ti44_Sint_Hch_a_20190717.csv')
#csH.append('../cross_sections/Ti44_Sint_Hch_n_20190717.csv')
#csH.append('../cross_sections/Ti44_Sint_Hch_p_20190717.csv')
##csH.append('../cross_sections/Ti44_Sint_Hch_piminus_20190717.csv')
##csH.append('../cross_sections/Ti44_Sint_Hch_piplus_20190717.csv')
#csL=[]
#csL.append('../cross_sections/Ti44_Sint_Lch_a_20190717.csv')
#csL.append('../cross_sections/Ti44_Sint_Lch_n_20190717.csv')
#csL.append('../cross_sections/Ti44_Sint_Lch_p_20190717.csv')
##csL.append('../cross_sections/Ti44_Sint_Lch_piminus_20190717.csv')
##csL.append('../cross_sections/Ti44_Sint_Lch_piplus_20190717.csv')
#csLL=[]
#csLL.append('../cross_sections/Ti44_Sint_LLch_a_20190717.csv')
#csLL.append('../cross_sections/Ti44_Sint_LLch_n_20190717.csv')
#csLL.append('../cross_sections/Ti44_Sint_LLch_p_20190717.csv')
##csLL.append('../cross_sections/Ti44_Sint_LLch_piminus_20190717.csv')
##csLL.append('../cross_sections/Ti44_Sint_LLch_piplus_20190717.csv')


#meteorites=[['AlbaretoNew',csLL,[1,3,5,10,15,20,30,40,50,60,70,80,90,100,110,120,130,135,141.6]],
#            ['Mooresfort',csH,[1,3,5,10,15,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,186]],
#            ['CharsonvilleNew',csH,[1,3,5,10,15,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250,260,270,280,290,300,310,316.2]],
#            ['Agen',csH,[1,3,5,10,15,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250,260,270,280,290,300,310,320,330,340,350,360,370,380,400,410,420,430,446.4]],            
#            ['Cereseto',csH,[1,3,5,10,15,20,30,40,50,60,70,80,90,100,110,120,130,140,148.8]],
#            ['Gruneberg',csH,[1,3,5,10,15,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250,260,270,279]],
#            ['Kernouve-b',csH,[1,3,5,10,15,20,30,40,50,60,70,80,90,100,110,120,130.2]],
#            ['Alfaniello',csL,[1,3,5,10,15,20,30,40,50,60,70,80,90,100,110,124.6]],
#            ['Bath',csH,[1,3,5,10,15,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,186]],
#            ['Lancon',csH,[1,3,5,10,15,20,30,40,50,60,70,85.56]],
#            ['Holbrook-RioNegro-Monze',csL,[1,3,5,10,15,20,30,40,50,60,70,80,90,100,110,120,130,142.4]],
#            ['Olivenza',csLL,[1,3,5,10,15,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250,260,270,280,290,300.9]],
#            ['Dhajala272',csH,[1,3,5,10,15,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,186]],
#            ['TurinH6',csH,[1,3,10,20,30,40,50,60,71.6]],
#            ['MbaleAT',csL,[1,3,5,10,15,20,30,40,50,60,70,80,90,100,110,128.16]],               
#            ['FermoDergaon1',csH,[1,3,5,10,15,20,30,40,50,60,74.4]]]

#for meteorite in meteorites:
#    pathYFiles=[]
#    pathHistogramFiles=[] #one file every primary energy
#    pathHistogramFiles.append('../histograms/'+meteorite[0]+'/a_10_'+meteorite[0]+'.xml')
#    pathHistogramFiles.append('../histograms/'+meteorite[0]+'/a_30_'+meteorite[0]+'.xml')
#    pathHistogramFiles.append('../histograms/'+meteorite[0]+'/a_100_'+meteorite[0]+'.xml')
#    pathHistogramFiles.append('../histograms/'+meteorite[0]+'/a_180_'+meteorite[0]+'.xml')
#    pathHistogramFiles.append('../histograms/'+meteorite[0]+'/a_300_'+meteorite[0]+'.xml')
#    pathHistogramFiles.append('../histograms/'+meteorite[0]+'/a_560_'+meteorite[0]+'.xml')
#    pathHistogramFiles.append('../histograms/'+meteorite[0]+'/a_1000_'+meteorite[0]+'.xml')
#    pathHistogramFiles.append('../histograms/'+meteorite[0]+'/a_3000_'+meteorite[0]+'.xml')
#    pathHistogramFiles.append('../histograms/'+meteorite[0]+'/a_10000_'+meteorite[0]+'.xml')
#    pathHistogramFiles.append('../histograms/'+meteorite[0]+'/a_30000_'+meteorite[0]+'.xml')
#    pathHistogramFiles.append('../histograms/'+meteorite[0]+'/a_100000_'+meteorite[0]+'.xml')
#    obj_ComputeS=YIELDFUNCTION.ComputeS(meteorite[1], pathHistogramFiles,1, "../yield_functions/"+meteorite[0]+"/26Al/", "26Al",now,meteorite[2])#, Composition,9)
#    pathYFiles.append(obj_ComputeS.ComputeSMatrix())
#    
#    pathHistogramFiles=[] #one file every primary energy
#    pathHistogramFiles.append('../histograms/'+meteorite[0]+'/p_10_'+meteorite[0]+'.xml')
#    pathHistogramFiles.append('../histograms/'+meteorite[0]+'/p_30_'+meteorite[0]+'.xml')
#    pathHistogramFiles.append('../histograms/'+meteorite[0]+'/p_100_'+meteorite[0]+'.xml')
#    pathHistogramFiles.append('../histograms/'+meteorite[0]+'/p_180_'+meteorite[0]+'.xml')
#    pathHistogramFiles.append('../histograms/'+meteorite[0]+'/p_300_'+meteorite[0]+'.xml')
#    pathHistogramFiles.append('../histograms/'+meteorite[0]+'/p_560_'+meteorite[0]+'.xml')
#    pathHistogramFiles.append('../histograms/'+meteorite[0]+'/p_1000_'+meteorite[0]+'.xml')
#    pathHistogramFiles.append('../histograms/'+meteorite[0]+'/p_3000_'+meteorite[0]+'.xml')
#    pathHistogramFiles.append('../histograms/'+meteorite[0]+'/p_10000_'+meteorite[0]+'.xml')
#    pathHistogramFiles.append('../histograms/'+meteorite[0]+'/p_30000_'+meteorite[0]+'.xml')
#    pathHistogramFiles.append('../histograms/'+meteorite[0]+'/p_100000_'+meteorite[0]+'.xml')
#    obj_ComputeS=YIELDFUNCTION.ComputeS(meteorite[1], pathHistogramFiles,1, "../yield_functions/"+meteorite[0]+"/26Al/", "26Al",now,meteorite[2])#, Composition,9)
#    pathYFiles.append(obj_ComputeS.ComputeSMatrix())
#    print(meteorite[0], pathYFiles)



#PRODUCTION.ComputeQ([yield functions path, modulation potential in MV, selected spectra])
#obj_ComputeQ=PRODUCTION.ComputeQ(['../yield_functions/TurinH6-Denser/yf_Ti44_prim_protons_2019y07m17g_11h46m49s.txt', "../yield_functions/TurinH6-Denser/yf_Ti44_prim_alphas_2019y07m17g_13h25m25s.txt"],0,1)
#h=150 #random cm number
#Q_at_certain_depth=obj_ComputeQ.Perform_PowerFunction(h) #just do a cycle in phi or in depth and you have production curves
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
## FROM HERE THERE'S SOME CODE I USED FOR PLOTS... CHECK IF THERE'S SOMETHING USEFUL FOR YOU

#obj_ComputeQ=PRODUCTION.ComputeQ(['../yield_functions/TurinH6-Denser/yf_Ti44_prim_protons_2019y07m17g_11h46m49s.txt', "../yield_functions/TurinH6-Denser/yf_Ti44_prim_alphas_2019y07m17g_13h25m25s.txt"],0,1) #phi in MV
##obj_ComputeQ=PRODUCTION.ComputeQ(['../yield_functions/Agen/yf_Ti44_prim_alphas_2019y07m09g_11h53m30s.txt', '../yield_functions/Agen/yf_Ti44_prim_protons_2019y07m09g_11h53m30s.txt'],0,1) #phi in MV
##obj_ComputeQ=PRODUCTION.ComputeQ(['../yield_functions/MichelNeumann/L/yf_Ti44_prim_alphas_2019y08m04g_22h25m00s.txt', '../yield_functions/MichelNeumann/L/yf_Ti44_prim_protons_2019y08m04g_22h25m00s.txt'],0,3) #phi in MV
#
##print(obj_ComputeQ.YData[1])
#Y=[]
#for h in range(0,len(obj_ComputeQ.YData[0][2])):
#    Y.append(obj_ComputeQ.YData[0][3][0][h])
#
#
##for w in ['flat', 'hanning', 'hamming', 'bartlett', 'blackman']:
##    plt.plot(obj_ComputeQ.YData[0][2],smooth(np.array(Y),window_len=5,window=w), label=w)
#plt.plot(obj_ComputeQ.YData[0][2],Y, label="original")
#plt.ylim([0,0.000050])
#plt.legend()
##
#MN_our_nolim=[2.690482384532718,
# 2.518011505295199,
# 2.3646299801296817,
# 2.2272248049430803,
# 2.1033701343991034,
# 1.9911328464137381,
# 1.8889458247963253,
# 1.7955209181568714,
# 1.7097869169329265,
# 1.6308441095970652,
# 1.5579302389461813,
# 1.4903945274090702,
# 1.4276775495786598,
# 1.3692954260215338,
# 1.3148272646180785,
# 1.2639050782273245,
# 1.216205614902171,
# 1.1714436821164802,
# 1.1293666500250656,
# 1.0897498938132244,
# 1.0523929903408935,
# 1.0171165253393448,
# 0.9837593983331123,
# 0.9521765359857086,
# 0.9222369426434731,
# 0.8938220308631394,
# 0.8668241856588337,
# 0.8411455248264329,
# 0.8166968245411051,
# 0.7933965848820638,
# 0.7711702143227712,
# 0.7499493157667227,
# 0.7296710595861575,
# 0.710277631470377,
# 0.6917157448180737,
# 0.6739362089972533,
# 0.6568935461121425,
# 0.640545650010581,
# 0.6248534821787858,
# 0.6097807999358132,
# 0.595293912983751]
#
# MN_our_lim=[2.476024475305089,
# 2.305715354308334,
# 2.154461047901035,
# 2.0191493209965516,
# 1.8973550754554045,
# 1.7871459153224134,
# 1.6869554301803606,
# 1.5954961547420892,
# 1.511697546535601,
# 1.43466054274434,
# 1.3636235171049789,
# 1.2979363058002313,
# 1.2370400805540553,
# 1.1804515429828364,
# 1.1277503664567983,
# 1.0785691142665692,
# 1.0325850703214245,
# 0.989513563841469,
# 0.9491024730655416,
# 0.9111276680321977,
# 0.8753892076395439,
# 0.8417081472424739,
# 0.8099238439606352,
# 0.7798916703962658,
# 0.7514810655368156,
# 0.7245738656284756,
# 0.6990628687568455,
# 0.6748505954931653,
# 0.6518482148023924,
# 0.6299746098676201,
# 0.6091555628694972,
# 0.5893230413011891,
# 0.570414571276625,
# 0.5523726856390849,
# 0.5351444366048915,
# 0.5186809642661374,
# 0.50293711359216,
# 0.4878710936635913,
# 0.47344417378616166,
# 0.4596204118968822,
# 0.44636641131890475]

##Q_vec=[]
##Q2_vec=[]
Q3_vec=[]
Q3Lim_vec=[]
##Q4_vec=[]
##Q5_vec=[]
##Q6_vec=[]
PHI=[]
h=143.2
for i in range(0,41):
   PHI.append(i*50)
for phi in PHI:
##    obj_ComputeQ=PRODUCTION.ComputeQ(['../yield_functions/Mooresfort/correct_composition/yf_Ti44_prim_alphas_2019y07m19g_14h33m37s.txt', '../yield_functions/Mooresfort/correct_composition/yf_Ti44_prim_protons_2019y07m19g_14h33m37s.txt'],phi, 1) #phi in MV    
##    obj2_ComputeQ=PRODUCTION.ComputeQ(['../yield_functions/CharsonvilleNew/correct_composition/yf_Ti44_prim_alphas_2019y07m22g_20h10m07s.txt', '../yield_functions/CharsonvilleNew/correct_composition/yf_Ti44_prim_protons_2019y07m22g_20h10m07s.txt'],phi, 1)
   obj3_ComputeQ=PRODUCTION.ComputeQ(['../yield_functions/44Ti/MichelNeumann/H/yf_Ti44_prim_protons_2020y06m30g_18h10m04s.txt', '../yield_functions/44Ti/MichelNeumann/H/yf_Ti44_prim_alphas_2020y06m30g_18h10m04s.txt'],phi, 3,0)
   obj3Lim_ComputeQ=PRODUCTION.ComputeQ(['../yield_functions/44Ti/MichelNeumann/H/yf_Ti44_prim_protons_2020y06m30g_18h10m04s.txt', '../yield_functions/44Ti/MichelNeumann/H/yf_Ti44_prim_alphas_2020y06m30g_18h10m04s.txt'],phi, 3,1)

##    obj4_ComputeQ=PRODUCTION.ComputeQ(['../yield_functions/TurinH6/correct_composition/yf_Ti44_prim_alphas_2019y07m19g_14h33m37s.txt', '../yield_functions/TurinH6/correct_composition/yf_Ti44_prim_protons_2019y07m19g_14h33m37s.txt'],phi, 1)
##    obj5_ComputeQ=PRODUCTION.ComputeQ(['../yield_functions/Agen/correct_composition/yf_Ti44_prim_alphas_2019y07m19g_14h33m37s.txt', '../yield_functions/Agen/correct_composition/yf_Ti44_prim_protons_2019y07m19g_14h33m37s.txt'],phi, 1)    
##    obj6_ComputeQ=PRODUCTION.ComputeQ(['../yield_functions/Gruneberg/correct_composition/yf_Ti44_prim_alphas_2019y07m19g_14h33m37s.txt', '../yield_functions/Gruneberg/correct_composition/yf_Ti44_prim_protons_2019y07m19g_14h33m37s.txt'],phi, 1) #phi in MV    
##    Q_vec.append(obj_ComputeQ.Perform_PowerFunction(186))
##    Q2_vec.append(obj2_ComputeQ.Perform_PowerFunction(316.2))
   Q3_vec.append(obj3_ComputeQ.Perform_PowerFunction(140))
   Q3Lim_vec.append(obj3Lim_ComputeQ.Perform_PowerFunction(140))
##    Q4_vec.append(obj4_ComputeQ.Perform_PowerFunction(71.6))
##    Q5_vec.append(obj5_ComputeQ.Perform_PowerFunction(446.4))
##    Q6_vec.append(obj6_ComputeQ.Perform_PowerFunction(279))
##plt.plot(PHI,np.array(Q5_vec), label="120 cm")    
##plt.plot(PHI,np.array(Q2_vec), label="85 cm")
##plt.plot(PHI,np.array(Q6_vec), label="75 cm")
##plt.plot(PHI,np.array(Q_vec), label="50 cm")
##plt.plot(PHI,np.array(Q3_vec), label="MP 40 cm")
##plt.plot(PHI,np.array(Q4_vec), label="20 cm")
# plt.plot(PHI,np.array(Q3_vec), label="Spectra Burger")
# plt.plot(PHI,MN_our_nolim, label="Monaco and Poluianov without MN limitations")
# plt.plot(PHI,MN_our_lim, label="Monaco and Poluianov MN limitations")

fig = plt.figure()
ax = fig.add_subplot(111)   
plt.plot(PHI, MNfit(PHI), label="Usoskin et al. (2006) fit")
plt.plot(PHI,np.array(Q3Lim_vec), label="MP with MN assumptions")
plt.plot(PHI,np.array(Q3_vec), label="MP without MN assumptions")
ax.annotate("$Q(\phi) = 0.8 + 2.07 \cdot e^{-0.00319 \phi}$", xy=(500,1.5), textcoords='data', rotation=0, fontsize=15)
plt.title('PRODUCTION RATE VS PHI FOR 40 CM H-CHONDRITE')
plt.xlabel("Solar modulation parameter $\phi [MV]$")
plt.ylabel("Production rate Q $[\\frac{dpm}{kg}]$")
plt.plot([900,650,620,450,300],[0.92,1.05,1.09,1.27,1.63], 'ro', label="MN points")
#
#plt.axvspan(250, 750, color='yellow', alpha=0.5)
plt.ylim([0,3.5])
plt.xlim([0,PHI[-1]])
plt.legend()
plt.show()
#plt.savefig('prova.png')
#Production per each depth
#Q_vec=[]
#phi=620
#obj_ComputeQ=PRODUCTION.ComputeQ(['../yield_functions/Mooresfort/correct_composition/yf_Ti44_prim_alphas_2019y07m19g_14h33m37s.txt', '../yield_functions/Mooresfort/correct_composition/yf_Ti44_prim_protons_2019y07m19g_14h33m37s.txt'],phi, 1) #phi in MV    
#obj2_ComputeQ=PRODUCTION.ComputeQ(['../yield_functions/CharsonvilleNew/correct_composition/yf_Ti44_prim_alphas_2019y07m22g_20h10m07s.txt', '../yield_functions/CharsonvilleNew/correct_composition/yf_Ti44_prim_protons_2019y07m22g_20h10m07s.txt'],phi, 1)
#obj3_ComputeQ=PRODUCTION.ComputeQ(["../yield_functions/MichelNeumann/1KeV1000GeV/yf_Ti44_prim_alphas_2019y06m20g_13h03m12s.txt","../yield_functions/MichelNeumann/1KeV1000GeV/yf_Ti44_prim_protons_2019y06m20g_13h03m12s.txt"],phi, 1)
#obj4_ComputeQ=PRODUCTION.ComputeQ(['../yield_functions/TurinH6/correct_composition/yf_Ti44_prim_alphas_2019y07m19g_14h33m37s.txt', '../yield_functions/TurinH6/correct_composition/yf_Ti44_prim_protons_2019y07m19g_14h33m37s.txt'],phi, 1)
#obj5_ComputeQ=PRODUCTION.ComputeQ(['../yield_functions/Agen/correct_composition/yf_Ti44_prim_alphas_2019y07m19g_14h33m37s.txt', '../yield_functions/Agen/correct_composition/yf_Ti44_prim_protons_2019y07m19g_14h33m37s.txt'],phi, 1)    
#obj6_ComputeQ=PRODUCTION.ComputeQ(['../yield_functions/Gruneberg/correct_composition/yf_Ti44_prim_alphas_2019y07m19g_14h33m37s.txt', '../yield_functions/Gruneberg/correct_composition/yf_Ti44_prim_protons_2019y07m19g_14h33m37s.txt'],phi, 1) #phi in MV    
#
#plt.figure(1)
#obj=[[obj4_ComputeQ,"20 cm"],[obj_ComputeQ,"50 cm"],[obj6_ComputeQ,"75 cm"],[obj2_ComputeQ,"85 cm"],[obj5_ComputeQ,"120 cm"]]
#for simu in obj:
#    Q_vec=[]
#    depth=simu[0].YData[0][2]
#    for h in depth:
#        Q_vec.append(simu[0].Perform_PowerFunction(h))
#    depth=np.array(depth)/3.72
#    plt.plot(depth,smooth(np.array(Q_vec),6), label=simu[1])
##plt.title('PRODUCTION OVER DEPTH')
#plt.xlabel("Depth $[cm]$")
#plt.ylabel("Production rate Q $[\\frac{dpm}{kg}]$")
#plt.legend()
#plt.ylim([0,1.6])

#Yield function per each depth, for 100 Mev 1 Gev 10 Gev, for both alpha and protons
#for Y in obj_ComputeQ.YData:
#    temp=YieldFunctionDepth(Y[3], 5)
#    plt.figure(obj_ComputeQ.YData.index(Y))
#    plt.plot(Y[2],temp)
##    plt.yscale('log')
#    particle=""
#    if Y[0]=='p':
#        particle="PROTONS "
#    else:
#        particle="ALPHAS "
#    plt.title(particle+'YIELD FUNCTION 10 GEV')
#    plt.xlabel("Depth $[\\frac{g}{cm^{2}}]$")
#    plt.ylabel("Yield function $[\\frac{atoms \cdot sr \cdot cm^{2}}{g}]$")

#Yield function per each energy, for only the outer shell and for 4 cm layer
#from scipy.optimize import curve_fit
#
#def func(x, a, b, c):
#    x=np.array(x)
##    return a * np.exp(-b * x) + c
##    return a*(x**3)+b*(x**2)+c*x+d
##    return a*(x**b)
#    return a*(np.exp(-b*x))+c
##    return a*np.sin(np.arctan(b*x))+c
#
#def chi_square(obs,exp):
#    return sum((obs[i]-exp[i])**2/exp[i] for i in range(0,len(obs)))
#               

#obj_ComputeQ=PRODUCTION.ComputeQ(['../yield_functions/TurinH6/correct_composition/yf_Ti44_prim_alphas_2019y07m19g_14h33m37s.txt', '../yield_functions/TurinH6/correct_composition/yf_Ti44_prim_protons_2019y07m19g_14h33m37s.txt'],0,1) #phi in MV
##obj_ComputeQ=PRODUCTION.ComputeQ(['../yield_functions/Agen/yf_Ti44_prim_alphas_2019y07m09g_11h53m30s.txt', '../yield_functions/Agen/yf_Ti44_prim_protons_2019y07m09g_11h53m30s.txt'],0,1) #phi in MV
##obj_ComputeQ=PRODUCTION.ComputeQ(['../yield_functions/MichelNeumann/L/yf_Ti44_prim_alphas_2019y08m04g_22h25m00s.txt', '../yield_functions/MichelNeumann/L/yf_Ti44_prim_protons_2019y08m04g_22h25m00s.txt'],0,3) #phi in MV
##obj_ComputeQ=PRODUCTION.ComputeQ(['../yield_functions/Mooresfort/correct_composition/yf_Ti44_prim_alphas_2019y07m19g_14h33m37s.txt', '../yield_functions/Mooresfort/correct_composition/yf_Ti44_prim_protons_2019y07m19g_14h33m37s.txt'],0, 1) #phi in MV    
##obj_ComputeQ=PRODUCTION.ComputeQ(['../yield_functions/CharsonvilleNew/correct_composition/yf_Ti44_prim_alphas_2019y07m22g_20h10m07s.txt', '../yield_functions/CharsonvilleNew/correct_composition/yf_Ti44_prim_protons_2019y07m22g_20h10m07s.txt'],0, 1) #phi in MV    
#
#for Y in obj_ComputeQ.YData:
##    for i in range(0,4):
#        plt.figure()
##        figManager = plt.get_current_fig_manager()
##        figManager.window.showMaximized()
##        plt.show()
##        plt.tight_layout()
#        index=len(Y[2])-2
#        temp=YieldFunctionEnergy(Y[3],index) #0 and 8
##        labelY=np.append(np.array([0]),Y[2],axis=0)
#        plt.loglog(Y[1][2:],temp[2:],"o-", label=str(Y[2][index])+"g/cm2")
#        #create the weighting array
##        y_weight = np.empty(len(temp))
#        #high pseudo-sd values, meaning less weighting in the fit
##        y_weight.fill(10)
#        #low values for point 0 and the last points, meaning more weighting during the fit procedure 
##        y_weight[0:1] = y_weight[-2:-1] = 0.1        
##        popt, pcov = curve_fit(func, Y[1], temp, sigma = y_weight, absolute_sigma = True)
##        xdata=np.append(np.linspace(0.1,1,80),np.linspace(1,100,80),axis=0)
##        ydata=func(xdata, *popt)
##        ydata[0]=temp[0]
##        plt.plot(xdata,ydata, 'r-', label='fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt))
##        y_obs=popt[0]*(np.array(Y[1])**(popt[1]/popt[2]))
##        plt.loglog(xdata,ydata, "o-", label="fit - chi_square="+str(chi_square(temp,y_obs)))
#        plt.legend()
#        particle=""
#        if Y[0]=='p':
#            particle="PROTONS "
#        else:
#            particle="ALPHAS "
#        plt.title(particle+'YIELD FUNCTION')
#        plt.xlabel("Energy $[\\frac{Gev}{nucleon}]$")
#        plt.ylabel("Yield function $[\\frac{atoms \cdot sr \cdot cm^{2}}{g}]$")
#        plt.ylim([0,1e-3])
##        plt.text(0,-0.000001,"fit=a*x^(b)      a="+str(popt[0])+" b="+str(popt[1]))
##        plt.tight_layout()

#J for phi=0 and J=500 bot protons and alphas
#phi=100
#J1=[]
#J2=[]
#for Y in obj2_ComputeQ.YData[0:1]:
#    particle=""
#    if Y[0]=='p':
#        particle="PROTONS "
#    else:
#        particle="ALPHAS "
#    J=[]
#    for energy in Y[1]:
#        J1.append(obj2_ComputeQ.J(Y[0],energy,phi)*10)
#    
#    plt.figure(obj2_ComputeQ.YData.index(Y))
#    plt.loglog(np.array(Y[1])*1000,J1, label="Castagnoli")
#    plt.title(particle+'SPECTRA FOR $\phi='+str(phi)+'$')
#    plt.xlabel("Energy $[\\frac{Mev}{nucleon}]$")
#    plt.ylabel("Spectra $[\\frac{atoms}{sr \cdot sec \cdot cm^{2}}]$")    
#
#for Y in obj_ComputeQ.YData[0:1]:
#    particle=""
#    if Y[0]=='p':
#        particle="PROTONS "
#    else:
#        particle="ALPHAS "
#    J=[]
#    for energy in Y[1]:
#        J2.append(obj_ComputeQ.J(Y[0],energy,phi)*10)
#    plt.loglog(np.array(Y[1])*1000,J2, label="Vos")
#
#plt.legend()
#plt.plot((obj2_ComputeQ.YData[1:2][0][1]),np.array(J1)/np.array(J2))