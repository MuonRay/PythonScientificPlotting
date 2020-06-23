# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 23:16:30 2020

@author: cosmi
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

file0 = 'DJI_0128.JPG'
image = cv2.imread(file0)

_ = plt.hist(image.ravel(), bins = 256, color = 'orange', )
_ = plt.hist(image[:, :, 0].ravel(), bins = 256, color = 'red', alpha = 0.5)
_ = plt.hist(image[:, :, 1].ravel(), bins = 256, color = 'Green', alpha = 0.5)
_ = plt.hist(image[:, :, 2].ravel(), bins = 256, color = 'Blue', alpha = 0.5)
_ = plt.xlabel('Intensity Value')
_ = plt.ylabel('Count')
_ = plt.legend(['Total', 'Red_Channel', 'Green_Channel', 'Blue_Channel'])
plt.show()