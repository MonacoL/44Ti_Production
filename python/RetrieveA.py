#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 17:02:36 2019

@author: lucamonaco
"""

import ComputeA as ACTIVITY
import ComputeQ as PRODUCTION
import numpy as np
#import matplotlib.pyplot as plt

def isLeapYear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return 1
            else:
                return 0
        else:
            return 1        
    else: 
        return 0
    
def DateToDecimal(day,month,year):
    daysinmonth=0.0
    daysinyear=365
    if month in [1,3,5,7,8,10,12]:
        daysinmonth=31
    elif month in [4,6,9,11]:
        daysinmonth=30
    elif isLeapYear(year)==0:
        daysinmonth=28
    else:
        daysinmonth=29
        daysinyear=366
    return year+((month-1)*daysinmonth+day)/daysinyear



#44TI ACTIVITY FROM JGR

#meteorites=[['AlbaretoNew',135,['../yield_functions/AlbaretoNew/correct_composition/yf_Ti44_prim_alphas_2019y07m19g_14h33m37s.txt', '../yield_functions/AlbaretoNew/correct_composition/yf_Ti44_prim_protons_2019y07m19g_14h33m37s.txt']],            
#            ['AlbaretoNew',135,['../yield_functions/AlbaretoNew/correct_composition/yf_Ti44_prim_alphas_2019y07m19g_14h33m37s.txt', '../yield_functions/AlbaretoNew/correct_composition/yf_Ti44_prim_protons_2019y07m19g_14h33m37s.txt']],
#            ['Mooresfort',170,['../yield_functions/Mooresfort/correct_composition/yf_Ti44_prim_alphas_2019y07m19g_14h33m37s.txt', '../yield_functions/Mooresfort/correct_composition/yf_Ti44_prim_protons_2019y07m19g_14h33m37s.txt']],
#            ['CharsonvilleNew',310,['../yield_functions/CharsonvilleNew/correct_composition/yf_Ti44_prim_alphas_2019y07m22g_20h10m07s.txt', '../yield_functions/CharsonvilleNew/correct_composition/yf_Ti44_prim_protons_2019y07m22g_20h10m07s.txt']],
#            ['Agen',430,['../yield_functions/Agen/correct_composition/yf_Ti44_prim_alphas_2019y07m19g_14h33m37s.txt', '../yield_functions/Agen/correct_composition/yf_Ti44_prim_protons_2019y07m19g_14h33m37s.txt']],
#            ['Cereseto',140,['../yield_functions/Cereseto/correct_composition/yf_Ti44_prim_alphas_2019y07m19g_14h33m37s.txt', '../yield_functions/Cereseto/correct_composition/yf_Ti44_prim_protons_2019y07m19g_14h33m37s.txt']],
#            ['Cereseto',140,['../yield_functions/Cereseto/correct_composition/yf_Ti44_prim_alphas_2019y07m19g_14h33m37s.txt', '../yield_functions/Cereseto/correct_composition/yf_Ti44_prim_protons_2019y07m19g_14h33m37s.txt']],
#            ['Gruneberg',270,['../yield_functions/Gruneberg/correct_composition/yf_Ti44_prim_alphas_2019y07m19g_14h33m37s.txt', '../yield_functions/Gruneberg/correct_composition/yf_Ti44_prim_protons_2019y07m19g_14h33m37s.txt']],
#            ['Kernouve-b',430,['../yield_functions/Agen/correct_composition/yf_Ti44_prim_alphas_2019y07m19g_14h33m37s.txt', '../yield_functions/Agen/correct_composition/yf_Ti44_prim_protons_2019y07m19g_14h33m37s.txt']],
#            ['Alfaniello',110,['../yield_functions/Alfaniello/correct_composition/yf_Ti44_prim_alphas_2019y07m19g_14h33m37s.txt', '../yield_functions/Alfaniello/correct_composition/yf_Ti44_prim_protons_2019y07m19g_14h33m37s.txt']],
#            ['Bath',170,['../yield_functions/Bath/correct_composition/yf_Ti44_prim_alphas_2019y07m19g_14h33m37s.txt', '../yield_functions/Bath/correct_composition/yf_Ti44_prim_protons_2019y07m19g_14h33m37s.txt']],
#            ['Lancon',70,['../yield_functions/Lancon/correct_composition/yf_Ti44_prim_alphas_2019y07m19g_14h33m37s.txt', '../yield_functions/Lancon/correct_composition/yf_Ti44_prim_protons_2019y07m19g_14h33m37s.txt']],
#            ['Holbrook',130,['../yield_functions/Holbrook-RioNegro-Monze/correct_composition/yf_Ti44_prim_alphas_2019y07m19g_14h33m37s.txt', '../yield_functions/Holbrook-RioNegro-Monze/correct_composition/yf_Ti44_prim_protons_2019y07m19g_14h33m37s.txt']],
#            ['Olivenza',290,['../yield_functions/Olivenza/correct_composition/yf_Ti44_prim_alphas_2019y07m19g_14h33m37s.txt', '../yield_functions/Olivenza/correct_composition/yf_Ti44_prim_protons_2019y07m19g_14h33m37s.txt']],
#            ['RioNegro',130,['../yield_functions/Holbrook-RioNegro-Monze/correct_composition/yf_Ti44_prim_alphas_2019y07m19g_14h33m37s.txt', '../yield_functions/Holbrook-RioNegro-Monze/correct_composition/yf_Ti44_prim_protons_2019y07m19g_14h33m37s.txt']],
#            ['Monze',130,['../yield_functions/Holbrook-RioNegro-Monze/correct_composition/yf_Ti44_prim_alphas_2019y07m19g_14h33m37s.txt', '../yield_functions/Holbrook-RioNegro-Monze/correct_composition/yf_Ti44_prim_protons_2019y07m19g_14h33m37s.txt']],
#            ['Dhajala272',170,['../yield_functions/Dhajala272/correct_composition/yf_Ti44_prim_alphas_2019y07m19g_14h33m37s.txt', '../yield_functions/Dhajala272/correct_composition/yf_Ti44_prim_protons_2019y07m19g_14h33m37s.txt']],
#            ['Dhajala272',170,['../yield_functions/Dhajala272/correct_composition/yf_Ti44_prim_alphas_2019y07m19g_14h33m37s.txt', '../yield_functions/Dhajala272/correct_composition/yf_Ti44_prim_protons_2019y07m19g_14h33m37s.txt']],
#            ['TurinH6',50,['../yield_functions/TurinH6/correct_composition/yf_Ti44_prim_alphas_2019y07m19g_14h33m37s.txt', '../yield_functions/TurinH6/correct_composition/yf_Ti44_prim_protons_2019y07m19g_14h33m37s.txt']],
#            ['MbaleA',110,['../yield_functions/MbaleAT/correct_composition/yf_Ti44_prim_alphas_2019y07m19g_14h33m37s.txt', '../yield_functions/MbaleAT/correct_composition/yf_Ti44_prim_protons_2019y07m19g_14h33m37s.txt']],
#            ['MbaleT',110,['../yield_functions/MbaleAT/correct_composition/yf_Ti44_prim_alphas_2019y07m19g_14h33m37s.txt', '../yield_functions/MbaleAT/correct_composition/yf_Ti44_prim_protons_2019y07m19g_14h33m37s.txt']],
#            ['Fermo',60,['../yield_functions/FermoDergaon1/correct_composition/yf_Ti44_prim_alphas_2019y07m19g_14h33m37s.txt', '../yield_functions/FermoDergaon1/correct_composition/yf_Ti44_prim_protons_2019y07m19g_14h33m37s.txt']],
#            ['Dergaon1',60,['../yield_functions/FermoDergaon1/correct_composition/yf_Ti44_prim_alphas_2019y07m19g_14h33m37s.txt', '../yield_functions/FermoDergaon1/correct_composition/yf_Ti44_prim_protons_2019y07m19g_14h33m37s.txt']]]
    


#MeasuredActivity=[2.33, 1.55, 1.75, 1.39, 1.15, 1.65, 1.55, 1.48, 1.39, 1.22, 1.25, 1.3, 0.8, 0.9, 1.3, 1.17, 0.83, 0.82, 1.2, 1.0, 0.8, 1.28, 1.07]
#
#MeasuredActivityError=[0.7,0.69,0.28,0.48,0.68,0.36,0.26,0.33,0.27,0.22,0.2,0.2,0.2,0.18,0.2,0.2,0.15,0.04,0.2,0.1,0.1,0.11,0.17]
#
#DateOfFall=[DateToDecimal(5,9,1814),  #0 Agen
#            DateToDecimal(15,7,1766), #1 Albareto
#            DateToDecimal(15,7,1766), #1a Albareto
#            DateToDecimal(16,2,1883), #2 Alfaniello
#            DateToDecimal(29,8,1892), #3 Bath
#            DateToDecimal(17,7,1840), #4 Cereseto
#            DateToDecimal(17,7,1840), #4a Cereseto
#            DateToDecimal(23,11,1810),#5 Charsonville
#            DateToDecimal(28,1,1976), #6 Dhajala 272
#            DateToDecimal(28,1,1976), #6a Dhajala 272
#            DateToDecimal(25,9,1996), #7 Fermo
#            DateToDecimal(2,3,2001),  #8 Dergaon
#            DateToDecimal(22,3,1841), #9 Gruneberg
#            DateToDecimal(19,7,1912), #10 Holbrook
#            DateToDecimal(21,9,1934), #11 Rio Negro
#            DateToDecimal(5,10,1950), #12 Monze
#            DateToDecimal(22,5,1869), #13 Kernouve-b
#            DateToDecimal(20,6,1897), #14 Lancon
#            DateToDecimal(14,8,1992), #15 Mbale A
#            DateToDecimal(14,8,1992), #15a Mbale T
#            DateToDecimal(15,8,1810), #16 Mooresfort
#            DateToDecimal(19,6,1924), #17 Olivenza
#            DateToDecimal(18,5,1988)] #18 Torino
#DateOfFall.sort()

##############################################################################
#UPDATED JGR DATA NORMALIZED FE+NI:    
MeasuredActivity=[9.95,
                  6.48,
                  6.40,
                  5.57,
                  6.07,
                  6.30,
                  6.70,
                  5.40,
                  5.10,
                  4.85,
                  4.25,
                  4.25,
                  6.30,
                  6.00,
                  5.50,
                  4.50,
                  4.24,
                  4.20,
                  4.15,
                  4.01]
#
MeasuredActivityError=[2.58,
                       1.05,
                       2.20,
                       0.97,
                       0.81,
                       1.40,
                       1.30,
                       1.00,
                       0.76,
                       0.70,
                       0.57,
                       1.00,
                       1.30,
                       1.00,
                       1.00,
                       0.20,
                       0.50,
                       0.28,
                       0.37,
                       0.34]

DateOfFall=[1766.54,
            1810.63,
            1810.89,
            1814.68,
            1840.54,
            1841.22,
            1869.39,
            1883.13,
            1892.66,
            1897.47,
            1912.55,
            1924.46,
            1934.72,
            1950.76,
            1976.08,
            1988.38,
            1992.62,
            1992.62,
            1996.73,
            2001.17]

NormFactJarosewich=[4.83091787439614, #basing on meteorite class
                    3.40251786321878,
                    3.40251786321878,
                    3.40251786321878,
                    3.40251786321878,
                    3.40251786321878,
                    3.40251786321878,
                    4.31648465489705,
                    3.40251786321878,
                    3.40251786321878,
                    4.31648465489705,
                    4.83045116413873,
                    4.31648465489705,
                    4.31648465489705,
                    3.40251786321878,
                    3.40251786321878,
                    4.31648465489705,
                    4.31648465489705,
                    3.40251786321878,
                    3.40251786321878]

#STUFF FOR CALCULATION WITH OUR MODEL
#          [..,[Meteorite Name, depth of calculation in cm, yield functions path vector],..]
# meteorites=[['Albareto',17.7,['../yield_functions/44Ti/AlbaretoNew/correct_composition/yf_Ti44_prim_alphas_2019y07m19g_14h33m37s.txt', '../yield_functions/44Ti/AlbaretoNew/correct_composition/yf_Ti44_prim_protons_2019y07m19g_14h33m37s.txt']],            
#             ['Mooresfort',29.76,['../yield_functions/44Ti/Mooresfort/correct_composition/yf_Ti44_prim_alphas_2019y07m19g_14h33m37s.txt', '../yield_functions/44Ti/Mooresfort/correct_composition/yf_Ti44_prim_protons_2019y07m19g_14h33m37s.txt']],
#             ['Charsonville',26.04,['../yield_functions/44Ti/CharsonvilleNew/correct_composition/yf_Ti44_prim_alphas_2019y07m22g_20h10m07s.txt', '../yield_functions/44Ti/CharsonvilleNew/correct_composition/yf_Ti44_prim_protons_2019y07m22g_20h10m07s.txt']],
#             ['Agen',55.8,['../yield_functions/44Ti/Agen/correct_composition/yf_Ti44_prim_alphas_2019y07m19g_14h33m37s.txt', '../yield_functions/44Ti/Agen/correct_composition/yf_Ti44_prim_protons_2019y07m19g_14h33m37s.txt']],
#             ['Cereseto',29.76,['../yield_functions/44Ti/Cereseto/correct_composition/yf_Ti44_prim_alphas_2019y07m19g_14h33m37s.txt', '../yield_functions/44Ti/Cereseto/correct_composition/yf_Ti44_prim_protons_2019y07m19g_14h33m37s.txt']],
#             ['Gruneberg',37.2,['../yield_functions/44Ti/Gruneberg/correct_composition/yf_Ti44_prim_alphas_2019y07m19g_14h33m37s.txt', '../yield_functions/44Ti/Gruneberg/correct_composition/yf_Ti44_prim_protons_2019y07m19g_14h33m37s.txt']],
#             ['Kernouve-b',26.04,['../yield_functions/44Ti/Agen/correct_composition/yf_Ti44_prim_alphas_2019y07m19g_14h33m37s.txt', '../yield_functions/44Ti/Agen/correct_composition/yf_Ti44_prim_protons_2019y07m19g_14h33m37s.txt']],
#             ['Alfaniello',35.6,['../yield_functions/44Ti/Alfaniello/correct_composition/yf_Ti44_prim_alphas_2019y07m19g_14h33m37s.txt', '../yield_functions/44Ti/Alfaniello/correct_composition/yf_Ti44_prim_protons_2019y07m19g_14h33m37s.txt']],
#             ['Bath',26.04,['../yield_functions/44Ti/Bath/correct_composition/yf_Ti44_prim_alphas_2019y07m19g_14h33m37s.txt', '../yield_functions/44Ti/Bath/correct_composition/yf_Ti44_prim_protons_2019y07m19g_14h33m37s.txt']],
#             ['Lancon',40.92,['../yield_functions/44Ti/Lancon/correct_composition/yf_Ti44_prim_alphas_2019y07m19g_14h33m37s.txt', '../yield_functions/44Ti/Lancon/correct_composition/yf_Ti44_prim_protons_2019y07m19g_14h33m37s.txt']],
#             ['Holbrook',71.2,['../yield_functions/44Ti/Holbrook-RioNegro-Monze/correct_composition/yf_Ti44_prim_alphas_2019y07m19g_14h33m37s.txt', '../yield_functions/44Ti/Holbrook-RioNegro-Monze/correct_composition/yf_Ti44_prim_protons_2019y07m19g_14h33m37s.txt']],
#             ['Olivenza',60.18,['../yield_functions/44Ti/Olivenza/correct_composition/yf_Ti44_prim_alphas_2019y07m19g_14h33m37s.txt', '../yield_functions/44Ti/Olivenza/correct_composition/yf_Ti44_prim_protons_2019y07m19g_14h33m37s.txt']],
#             ['RioNegro',21.36,['../yield_functions/44Ti/Holbrook-RioNegro-Monze/correct_composition/yf_Ti44_prim_alphas_2019y07m19g_14h33m37s.txt', '../yield_functions/44Ti/Holbrook-RioNegro-Monze/correct_composition/yf_Ti44_prim_protons_2019y07m19g_14h33m37s.txt']],
#             ['Monze',71.2,['../yield_functions/44Ti/Holbrook-RioNegro-Monze/correct_composition/yf_Ti44_prim_alphas_2019y07m19g_14h33m37s.txt', '../yield_functions/44Ti/Holbrook-RioNegro-Monze/correct_composition/yf_Ti44_prim_protons_2019y07m19g_14h33m37s.txt']],
#             ['Dhajala272',59.52,['../yield_functions/44Ti/Dhajala272/correct_composition/yf_Ti44_prim_alphas_2019y07m19g_14h33m37s.txt', '../yield_functions/44Ti/Dhajala272/correct_composition/yf_Ti44_prim_protons_2019y07m19g_14h33m37s.txt']],
#             ['TurinH6',52.08,['../yield_functions/44Ti/TurinH6/correct_composition/yf_Ti44_prim_alphas_2019y07m19g_14h33m37s.txt', '../yield_functions/44Ti/TurinH6/correct_composition/yf_Ti44_prim_protons_2019y07m19g_14h33m37s.txt']],
#             ['MbaleA',35.6,['../yield_functions/44Ti/MbaleAT/correct_composition/yf_Ti44_prim_alphas_2019y07m19g_14h33m37s.txt', '../yield_functions/44Ti/MbaleAT/correct_composition/yf_Ti44_prim_protons_2019y07m19g_14h33m37s.txt']],
#             ['MbaleT',85.44,['../yield_functions/44Ti/MbaleAT/correct_composition/yf_Ti44_prim_alphas_2019y07m19g_14h33m37s.txt', '../yield_functions/44Ti/MbaleAT/correct_composition/yf_Ti44_prim_protons_2019y07m19g_14h33m37s.txt']],
#             ['Fermo',18.6,['../yield_functions/44Ti/FermoDergaon1/correct_composition/yf_Ti44_prim_alphas_2019y07m19g_14h33m37s.txt', '../yield_functions/44Ti/FermoDergaon1/correct_composition/yf_Ti44_prim_protons_2019y07m19g_14h33m37s.txt']],
#             ['Dergaon1',26.04,['../yield_functions/44Ti/FermoDergaon1/correct_composition/yf_Ti44_prim_alphas_2019y07m19g_14h33m37s.txt', '../yield_functions/44Ti/FermoDergaon1/correct_composition/yf_Ti44_prim_protons_2019y07m19g_14h33m37s.txt']]]

meteorites=[['Albareto',17.7,['../yield_functions/44Ti/LL/40cm/yf_Ti44_prim_alphas_2020y08m15g_22h19m28s.txt', '../yield_functions/44Ti/LL/40cm/yf_Ti44_prim_protons_2020y08m15g_22h19m28s.txt']],            
            ['Mooresfort',29.76,['../yield_functions/44Ti/H/50cm/yf_Ti44_prim_alphas_2020y09m07g_10h38m04s.txt', '../yield_functions/44Ti/H/50cm/yf_Ti44_prim_protons_2020y09m07g_10h38m04s.txt']],
            ['Charsonville',26.04,['../yield_functions/44Ti/H/90cm/yf_Ti44_prim_protons_2020y08m13g_16h01m50s.txt', '../yield_functions/44Ti/H/90cm/yf_Ti44_prim_alphas_2020y08m13g_16h01m50s.txt']],
            ['Agen',55.8,['../yield_functions/44Ti/H/120cm/yf_Ti44_prim_alphas_2020y08m13g_17h52m35s.txt', '../yield_functions/44Ti/H/120cm/yf_Ti44_prim_protons_2020y08m13g_17h52m35s.txt']],
            ['Cereseto',29.76,['../yield_functions/44Ti/H/50cm/yf_Ti44_prim_alphas_2020y09m07g_10h38m04s.txt', '../yield_functions/44Ti/H/50cm/yf_Ti44_prim_protons_2020y09m07g_10h38m04s.txt']],
            ['Gruneberg',37.2,['../yield_functions/44Ti/H/80cm/yf_Ti44_prim_alphas_2020y08m13g_18h14m37s.txt', '../yield_functions/44Ti/H/80cm/yf_Ti44_prim_protons_2020y08m13g_18h14m37s.txt']],
            ['Kernouve-b',26.04,['../yield_functions/44Ti/H/120cm/yf_Ti44_prim_alphas_2020y08m13g_17h52m35s.txt', '../yield_functions/44Ti/H/120cm/yf_Ti44_prim_protons_2020y08m13g_17h52m35s.txt']],
            ['Alfaniello',35.6,['../yield_functions/44Ti/L/40cm/yf_Ti44_prim_alphas_2020y08m15g_22h09m53s.txt', '../yield_functions/44Ti/L/40cm/yf_Ti44_prim_protons_2020y08m15g_22h09m53s.txt']],
            ['Bath',26.04,['../yield_functions/44Ti/H/50cm/yf_Ti44_prim_alphas_2020y09m07g_10h38m04s.txt', '../yield_functions/44Ti/H/50cm/yf_Ti44_prim_protons_2020y09m07g_10h38m04s.txt']],
            ['Lancon',40.92,['../yield_functions/44Ti/H/20cm/yf_Ti44_prim_alphas_2020y09m07g_10h35m06s.txt', '../yield_functions/44Ti/H/20cm/yf_Ti44_prim_protons_2020y09m07g_10h35m06s.txt']],
            ['Holbrook',71.2,['../yield_functions/44Ti/L/40cm/yf_Ti44_prim_alphas_2020y08m15g_22h09m53s.txt', '../yield_functions/44Ti/L/40cm/yf_Ti44_prim_protons_2020y08m15g_22h09m53s.txt']],
            ['Olivenza',60.18,['../yield_functions/44Ti/LL/90cm/yf_Ti44_prim_alphas_2020y08m15g_22h24m30s.txt', '../yield_functions/44Ti/LL/90cm/yf_Ti44_prim_protons_2020y08m15g_22h24m30s.txt']],
            ['RioNegro',21.36,['../yield_functions/44Ti/L/40cm/yf_Ti44_prim_alphas_2020y08m15g_22h09m53s.txt', '../yield_functions/44Ti/L/40cm/yf_Ti44_prim_protons_2020y08m15g_22h09m53s.txt']],
            ['Monze',71.2,['../yield_functions/44Ti/L/40cm/yf_Ti44_prim_alphas_2020y08m15g_22h09m53s.txt', '../yield_functions/44Ti/L/40cm/yf_Ti44_prim_protons_2020y08m15g_22h09m53s.txt']],
            ['Dhajala272',59.52,['../yield_functions/44Ti/H/50cm/yf_Ti44_prim_alphas_2020y09m07g_10h38m04s.txt', '../yield_functions/44Ti/H/50cm/yf_Ti44_prim_protons_2020y09m07g_10h38m04s.txt']],
            ['TurinH6',52.08,['../yield_functions/44Ti/H/20cm/yf_Ti44_prim_alphas_2020y09m07g_10h35m06s.txt', '../yield_functions/44Ti/H/20cm/yf_Ti44_prim_protons_2020y09m07g_10h35m06s.txt']],
            ['MbaleA',35.6,['../yield_functions/44Ti/L/40cm/yf_Ti44_prim_alphas_2020y08m15g_22h09m53s.txt', '../yield_functions/44Ti/L/40cm/yf_Ti44_prim_protons_2020y08m15g_22h09m53s.txt']],
            ['MbaleT',85.44,['../yield_functions/44Ti/L/40cm/yf_Ti44_prim_alphas_2020y08m15g_22h09m53s.txt', '../yield_functions/44Ti/L/40cm/yf_Ti44_prim_protons_2020y08m15g_22h09m53s.txt']],
            ['Fermo',18.6,['../yield_functions/44Ti/H/20cm/yf_Ti44_prim_alphas_2020y09m07g_10h35m06s.txt', '../yield_functions/44Ti/H/20cm/yf_Ti44_prim_protons_2020y09m07g_10h35m06s.txt']],
            ['Dergaon1',26.04,['../yield_functions/44Ti/H/20cm/yf_Ti44_prim_alphas_2020y09m07g_10h35m06s.txt', '../yield_functions/44Ti/H/20cm/yf_Ti44_prim_protons_2020y09m07g_10h35m06s.txt']]]


CalculatedActivity=[]

#pathPHIData=["../phi_series/Phi_mon_tab_LIS_Burger2000_nohead.txt","../phi_series/phi_all_Wu2018_fig12_nohead.txt","../phi_series/phi_1896_1936_random.txt"]
#pathPHIData=["../phi_series/phi_LLscenario_Fig2_Asvestari2017.txt"]
#pathPHIData=["../phi_series/phi_composite_20170719.csv"]
pathPHIData=["../phi_series/Fi_temp_VOS.txt"]
decaying_constant=1/85.4 #in years, this is for 44Ti
selected_spectra=1 #1 Vos, 2 Castagnoli, 3 Burger
spectras=['VOS','CASTAGNOLI','BURGER']

for meteorite in meteorites:
    date=DateOfFall[meteorites.index(meteorite)]
    obj_Activity2=ACTIVITY.ComputeA(meteorite[2],pathPHIData,decaying_constant,selected_spectra,meteorite[1])
    CalculatedActivity.append(obj_Activity2.GetA(date)*NormFactJarosewich[meteorites.index(meteorite)])

print(CalculatedActivity)
exit()
fig = plt.figure()
ax = fig.add_subplot(111)    
plt.plot(DateOfFall, CalculatedActivity, 'ro',label="Calculated Activity", color="red")
plt.errorbar(DateOfFall, MeasuredActivity, yerr=MeasuredActivityError, fmt='o', label="Measured Activity", color="blue", ecolor='black', elinewidth=0.5, capsize=5, capthick=0.5)
for elem in DateOfFall:
    x=elem - 1.25
    y=MeasuredActivity[DateOfFall.index(elem)]+3.5
    if DateOfFall.index(elem)==0:
        y=y-8.5
    elif DateOfFall.index(elem)==1:
        y=y-7.5
    elif DateOfFall.index(elem)==2:
        y=y+1.5  
    elif DateOfFall.index(elem)==5:
        y=y-7         
    elif DateOfFall.index(elem)==6:
        y=y+1.5              
    ax.annotate(meteorites[DateOfFall.index(elem)][0], xy=(x,y), textcoords='data', rotation=90) # <--

plt.legend()
plt.ylim([0,15]),
plt.xlim([1760,2005])
plt.xlabel("Time $[Year]$")
plt.ylabel("$^{44}$Ti Activity $[\\frac{dpm}{kg (Fe+Ni)}]$")
plt.title(spectras[selected_spectra-1]+" SPECTRA")