#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 12:50:09 2019

@author: lucamonaco
"""
def PowerFunction_Integration(y,dx):
    import numpy as np
    import math
    ydx=np.array(y)*np.array(dx)
    diff_ydx=[]
    log_diff_y=[]
    log_diff_dx=[]
    I=[]
    for i in range(0,len(y)-1):
        diff_ydx.append(ydx[i + 1]-ydx[i])
        try:
            log_diff_y.append(math.log(y[i + 1])-math.log(y[i]))
        except:
            log_diff_y.append(0)                 
        log_diff_dx.append(math.log(dx[i + 1])-math.log(dx[i]))
    for i in range(0,len(log_diff_y)):
        if log_diff_dx[i]!=0.0:
            I.append(diff_ydx[i]/((log_diff_y[i]/log_diff_dx[i])+1))
        else:
            I.append(0)
    
    return sum(s for s in I)