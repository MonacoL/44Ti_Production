#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 22 15:06:36 2019

@author: lucamonaco
"""

import XMLFromGeantParse as XMLFile
import matplotlib.pyplot as plt

EnergyFile=XMLFile.XMLFromGeantParse('../histograms/H/90cm/a_30_90cm.xml') #low stat
EnergyFile.Parse()

#Here i retrieve also histogram informations, to catch the right indeces for the points in the meteoroide that are required
#If you try HistrogramInformation[index], you retrieve a vector similar to the following
#['D195.57_p_noweight',    Depth_primary_weight, so here you can check if your chosen index points to the right place in the meteoroide
# '180',                   Number of bins
# '0.001000000000000000020816682',       min energy in MeV
# '999999.9999999833526089787',          max energy in MeV
# '792345',                              height
# '1204.605253768964303162647',          error
# '2147.32071845167320134351']           weighted mean


HistogramInformation=EnergyFile.HistogramInformations
HistogramBinsCenter=EnergyFile.HistogramBinsCenter
HistogramEntries=EnergyFile.HistogramEntries

#histograms with no weight
Entries_NearCenter_p_noweight=HistogramEntries[-30]
Entries_NearCenter_n_noweight=HistogramEntries[-28]
Entries_NearCenter_piplus_noweight=HistogramEntries[-26]
Entries_NearCenter_piminus_noweight=HistogramEntries[-24]
Entries_NearCenter_a_noweight=HistogramEntries[-22]

Entries2_NearCenter_p_noweight=HistogramEntries2[-30]
Entries2_NearCenter_n_noweight=HistogramEntries2[-28]
Entries2_NearCenter_piplus_noweight=HistogramEntries2[-26]
Entries2_NearCenter_piminus_noweight=HistogramEntries2[-24]
Entries2_NearCenter_a_noweight=HistogramEntries2[-22]

Entries_Halfway_p_noweight=HistogramEntries[-230]
Entries_Halfway_n_noweight=HistogramEntries[-228]
Entries_Halfway_piplus_noweight=HistogramEntries[-226]
Entries_Halfway_piminus_noweight=HistogramEntries[-224]
Entries_Halfway_a_noweight=HistogramEntries[-222]

Entries2_Halfway_p_noweight=HistogramEntries2[-230]
Entries2_Halfway_n_noweight=HistogramEntries2[-228]
Entries2_Halfway_piplus_noweight=HistogramEntries2[-226]
Entries2_Halfway_piminus_noweight=HistogramEntries2[-224]
Entries2_Halfway_a_noweight=HistogramEntries2[-222]


plt.figure(6)
x,y=EnergyFile.PlotSpectra(Entries_NearCenter_p_noweight)
plt.loglog(x,y,label="High stat")
x,y=EnergyFile.PlotSpectra(Entries2_NearCenter_p_noweight)
plt.loglog(x,y,label="Low stat")
plt.legend()
plt.title("120 CM H-CHONDRITE, PROTONS MOLTEPLICITY HALFWAY")
plt.xlabel("Energy $[MeV]$")
plt.ylabel("Molteplicity $[particles]$")
plt.tight_layout()

plt.figure(7)
x,y=EnergyFile.PlotSpectra(Entries_NearCenter_n_noweight)
plt.loglog(x,y,label="High stat")
x,y=EnergyFile.PlotSpectra(Entries2_NearCenter_n_noweight)
plt.loglog(x,y,label="Low stat")
plt.legend()
plt.title("120 CM H-CHONDRITE, NEUTRONS MOLTEPLICITY HALFWAY")
plt.xlabel("Energy $[MeV]$")
plt.ylabel("Molteplicity $[particles]$")
plt.tight_layout()

plt.figure(8)
x,y=EnergyFile.PlotSpectra(Entries_NearCenter_piplus_noweight)
plt.loglog(x,y,label="High stat")
x,y=EnergyFile.PlotSpectra(Entries2_NearCenter_piplus_noweight)
plt.loglog(x,y,label="Low stat")
plt.legend()
plt.title("120 CM H-CHONDRITE, PIPLUS MOLTEPLICITY HALFWAY")
plt.xlabel("Energy $[MeV]$")
plt.ylabel("Molteplicity $[particles]$")
plt.tight_layout()

plt.figure(9)
x,y=EnergyFile.PlotSpectra(Entries_NearCenter_piminus_noweight)
plt.loglog(x,y,label="High stat")
x,y=EnergyFile.PlotSpectra(Entries2_NearCenter_piminus_noweight)
plt.loglog(x,y,label="Low stat")
plt.legend()
plt.title("120 CM H-CHONDRITE, PIMINUS MOLTEPLICITY HALFWAY")
plt.xlabel("Energy $[MeV]$")
plt.ylabel("Molteplicity $[particles]$")
plt.tight_layout()

plt.figure(10)
x,y=EnergyFile.PlotSpectra(Entries_NearCenter_a_noweight)
plt.loglog(x,y,label="High stat")
x,y=EnergyFile.PlotSpectra(Entries2_NearCenter_a_noweight)
plt.loglog(x,y,label="Low stat")
plt.legend()
plt.title("120 CM H-CHONDRITE, ALPHA MOLTEPLICITY HALFWAY")
plt.xlabel("Energy $[MeV]$")
plt.ylabel("Molteplicity $[particles]$")
plt.tight_layout()