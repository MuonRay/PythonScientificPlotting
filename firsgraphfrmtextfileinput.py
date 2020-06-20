# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 04:06:28 2019

@author: cosmi
"""

# importing the required module 
import matplotlib.pyplot as plt
from matplotlib import style
import os
# Open in the working directory
cwd = os.getcwd()

style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

#ZWB2UVIRFilter.txt
#BG3InfraVioletFilterV2.txt

graph_data = open('ZWB2UVIRFilter.txt','r').read()
lines = graph_data.split('\n')
xs = []
ys = []
for line in lines:
    if len(line) > 1:
        x, y = line.split(' ')
        xs.append(float(x))
        ys.append(float(y))
        ax1.clear()
        ax1.plot(xs,ys, c='b', label='filter#2 spectrum')
        leg = ax1.legend()
        ax1.set_title("Transmission Spectrum")    
        ax1.set_xlabel('Wavelength(nm)')
        ax1.set_ylabel('Transmission(%)')