# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 02:30:30 2020

@author: cosmi
"""


import warnings
warnings.filterwarnings('ignore')
from matplotlib import pyplot as plt  # For image viewing

import scipy
import numpy as np
from scipy import misc


from matplotlib import colors
from matplotlib import ticker
from matplotlib.colors import LinearSegmentedColormap





#for batch in a test folder 
#for image in os.listdir('./test/'):
#  img = Image.open('./test/'+image)

file0 = 'DJI_0128.JPG'
img = misc.imread(file0)


ir = (img[:,:,0]).astype('float')
blue = (img[:,:,2]).astype('float')


# Create a numpy matrix of zeros to hold the calculated NDVI values for each pixel
ndvi = np.zeros(blue.size)  # The NDVI image will be the same size as the input image

# Calculate NDVI
ndvi = np.true_divide(np.subtract(ir, blue), np.add(ir, blue))


# Display the results
output_name = 'InfraBlueNDVI3.jpg'

#a nice selection of grayscale colour palettes
cols1 = ['blue', 'green', 'yellow', 'red']
cols2 =  ['gray', 'gray', 'red', 'yellow', 'green']
cols3 = ['gray', 'blue', 'green', 'yellow', 'red']

cols4 = ['black', 'gray', 'blue', 'green', 'yellow', 'red']

def create_colormap(args):
    return LinearSegmentedColormap.from_list(name='custom1', colors=cols1)

#colour bar to match grayscale units
def create_colorbar(fig, image):
        position = fig.add_axes([0.125, 0.19, 0.2, 0.05])
        norm = colors.Normalize(vmin=-1., vmax=1.)
        cbar = plt.colorbar(image,
                            cax=position,
                            orientation='horizontal',
                            norm=norm)
        cbar.ax.tick_params(labelsize=6)
        tick_locator = ticker.MaxNLocator(nbins=3)
        cbar.locator = tick_locator
        cbar.update_ticks()
        cbar.set_label("NDVI", fontsize=10, x=0.5, y=0.5, labelpad=-25)

fig, ax = plt.subplots()
image = ax.imshow(ndvi, cmap=create_colormap(colors))
plt.axis('off')

        # plt.show()

#%SAVI - Soil Reflectance Leveraged

#The SAVI is structured similar to the NDVI but with the addition of a
#“soil reflectance correction factor” L.
#L is a constant (related to the slope of the soil-line in a feature-space plot)
#Hence the value of L varies by the amount or cover of green vegetation: in very high vegetation regions,
#L=0; and in areas with no green vegetation, L=1. Generally, an L=0.5 works
#well in most situations (i.e. mixed vegetation cover)
#So 0.5 (half) is the default value used. When L=0, then SAVI = NDVI.



#SAVI = [((R-B)*(1+L))./(R+B+L)];

L=0.5;
one = 1;

rplusb = np.add(ir, blue)
rminusb = np.subtract(ir, blue)
oneplusL = np.add(one, L)

savi = np.zeros(blue.size)  # The NDVI image will be the same size as the input image

savi = np.true_divide(np.multiply(rminusb, oneplusL), np.add(rplusb, L))


#to use image color data in gaussian kernal density function 
#we need to flatten the data from a 2D pixel array to 1D with length corresponding to elements (Warning! this can take some time)
#the fastest way to do this is to use the python library-level function ravel, which reshapes the array and returns its view.
# Ravel will often be many times faster than the similar function flatten as no computer memory needs to be copied and the original array is not affected. 
# see reference to this at pgs 42-43 @ Numerical Python: A Practical Techniques Approach for Industry By Robert Johansson

#x = np.ndarray.ravel(blue)
#y = np.ndarray.ravel(ir)

x = np.ravel(img[:,:,2])   # blue channel array
y = np.ravel(img[:,:,0])   # nir channel array


plot1 = plt.figure(1)

#compare red and blue pixel data
nbins = 20
plt.hexbin(x, y, gridsize=nbins, cmap=plt.cm.jet)
plt.xlabel('Blue Reflectance')
plt.ylabel('NIR Reflectance')
# Add a title
plt.title('NIR vs Blue Spectral Data')

# Evaluate a gaussian kde on a regular grid of nbins x nbins over data extents
data = [x,y]


k = scipy.stats.gaussian_kde(data)
#k = kde.gaussian_kde(data)
xi, yi = np.mgrid[x.min():x.max():nbins*1j, y.min():y.max():nbins*1j]
zi = k(np.vstack([xi.flatten(), yi.flatten()]))


plot2 = plt.figure(2)

# plot a density
plt.title('Calculate Gaussian KDE')
plt.pcolormesh(xi, yi, zi.reshape(xi.shape), cmap=plt.cm.jet)
 
plot3 = plt.figure(3)

# add shading
plt.title('2D Density with shading')
plt.pcolormesh(xi, yi, zi.reshape(xi.shape), shading='gouraud', cmap=plt.cm.jet)
 
plot4 = plt.figure(4)

# contour
plt.title('Contour')
plt.pcolormesh(xi, yi, zi.reshape(xi.shape), shading='gouraud', cmap=plt.cm.jet)
plt.contour(xi, yi, zi.reshape(xi.shape) )



# threshold line
# Threshold; values above the threshold belong to another class as those below.
thresh = 0.0
clas = ndvi > thresh
#percentage of pixels selected
#imshow(clas, cmap=create_colormap(colors))


plot6 = plt.figure(6)

#size = 100*clas + 30*~clas
plt.pcolormesh(xi, yi, zi.reshape(xi.shape), shading='gouraud', cmap=plt.cm.jet)

plt.contour(xi,yi,clas)

plt.show()






