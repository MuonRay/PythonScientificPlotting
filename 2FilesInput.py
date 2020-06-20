# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 22:24:16 2019

@author: cosmi
"""

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

graph_data1 = open('ZWB2UVIRFilter.txt','r').read()
graph_data2 = open('BG3InfraVioletFilterV2.txt','r').read()

#mat0 = genfromtxt("ZWB2UVIRFilter.txt");
#mat1 = genfromtxt("BG3InfraVioletFilterV2.txt");

#graph_data = open('ZWB2UVIRFilter.txt','r').read()
lines1 = graph_data1.split('\n')
lines2 = graph_data2.split('\n')

#x1=mat0[:,0]
#y1=mat0[:,1]
#x2=mat1[:,0]
#y2=mat1[:,1]

x1 = []
y1 = []
x2 = []
y2 = []


for line1 in lines1:
    if len(line1) > 1:
        
        xa, ya = line1.split(' ')
        x1.append(float(xa))
        y1.append(float(ya))
        
        
for line2 in lines2:
    if len(line2) > 1:
        
        xb, yb = line2.split(' ')
        x2.append(float(xb))
        y2.append(float(yb))
        

        ax1.clear()
        # setting x and y axis range 
        plt.ylim(0,100) 
        plt.xlim(200,1200) 
        ax1.plot(x1,y1, c='b', label='filter#2 spectrum')
        ax1.plot(x2,y2, c='r', label='filter#1 spectrum')
        leg = ax1.legend()
        ax1.set_title("Transmission Spectrum")    
        ax1.set_xlabel('Wavelength(nm)')
        ax1.set_ylabel('Transmission(%)')