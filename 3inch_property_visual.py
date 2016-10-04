# -*- coding: utf-8 -*-
"""
Created on Wed July 13 2016

@author: fangren
"""


import numpy as np
import matplotlib.pyplot as plt
import glob
import os
from os.path import basename
import imp

plotTernary = imp.load_source("plt_ternary_save", "plotTernary.py")


path = 'C:\Research_FangRen\Data\July2016\CoVZr_ternary\masterfiles\high\plotting\\'

def twoD_visualize(path):
    """
    create three lists for plotting: plate_x, plate_y, ROI1, ROI2, ROI3...
    """
    for filename in glob.glob(os.path.join(path, '*.csv')):
        if basename(filename)[-5] == 'a':
            print basename(filename)
            data = np.genfromtxt(filename, delimiter=',', skip_header = 1)
            plate_x = data[:,1]
            plate_y = data[:,2]
            ROI1 = data[:,15]
            ROI2 = data[:,16]
            ROI3 = data[:,17]
            ROI5 = data[:,19]
            crystallinity = data[:,51]
            texture = data[:,53]
            metal1 = data[:,54]
            metal2 = data[:,55]
            metal3 = data[:,56]
            peak_num = data[:,58]
#            peak_position = data[:,57]
#            peak_width = data[:,58]
#            peak_intensity = data[:,59]
#    return plate_x, plate_y, ROI1, ROI2, ROI3, ROI5, crystallinity, texture, metal1, metal2, metal3, peak_position, peak_width, peak_intensity
    return plate_x, plate_y, ROI1, ROI2, ROI3, ROI5, crystallinity, texture, metal1, metal2, metal3, peak_num
                 
           

#plate_x, plate_y, ROI1, ROI2, ROI3, ROI5, crystallinity, texture, metal1, metal2, metal3, peak_position, peak_width, peak_intensity = twoD_visualize(path)
plate_x, plate_y, ROI1, ROI2, ROI3, ROI5, crystallinity, texture, metal1, metal2, metal3, peak_num = twoD_visualize(path)

area = [500]*len(plate_x)


plt.figure(1, figsize = (12, 9))
plt.title('Cobalt beta')
plt.scatter(plate_y, plate_x, c = ROI3, s = area, marker = 's')
plt.colorbar()
plt.xlim((-36, 36))
plt.ylim((-36, 36))
plt.xlabel('plate_y')
plt.ylabel('plate_x(flat)')
plt.savefig(path+'Cobalt beta.png')

plt.figure(2, figsize = (12, 9))
plt.title('Chromium alpha Valladium beta')
plt.scatter(plate_y, plate_x, c = ROI5, s = area, marker = 's')
plt.colorbar()
plt.xlim((-36, 36))
plt.ylim((-36, 36))
plt.xlabel('plate_y')
plt.ylabel('plate_x(flat)')
plt.savefig(path+'Chromium alpha Valladium beta.png')

plt.figure(3, figsize = (12, 9))
plt.title('Cobalt Iron alpha')
plt.scatter(plate_y, plate_x, c = ROI2, s = area, marker = 's')
plt.colorbar()
plt.xlim((-36, 36))
plt.ylim((-36, 36))
plt.xlabel('plate_y')
plt.ylabel('plate_x(flat)')
plt.savefig(path+'Cobalt and Iron alpha.png')


plt.figure(4, figsize = (12, 9))
plt.title('Vanadium alpha')
plt.scatter(plate_y, plate_x, c = ROI1, s = area, marker = 's')
plt.colorbar()
plt.xlim((-36, 36))
plt.ylim((-36, 36))
plt.xlabel('plate_y')
plt.ylabel('plate_x(flat)')
#plt.clim((500, 900))
plt.savefig(path+'Vanadium alpha.png')

plt.figure(5, figsize = (12, 9))
plt.title('crystallinity analysis')
plt.scatter(plate_y, plate_x, c = np.log(crystallinity), s = area, marker = 's')
plt.xlim((-36, 36))
plt.ylim((-36, 36))
plt.colorbar()
plt.xlabel('plate_y')
plt.ylabel('plate_x(flat)')
plt.clim((0.2, 1.4))
plt.savefig(path+'crystallinity analysis')

plt.figure(6, figsize = (12, 9))
plt.title('texture analysis')
plt.scatter(plate_y, plate_x, c = np.log(texture), s = area, marker = 's')
plt.xlim((-36, 36))
plt.ylim((-36, 36))
plt.colorbar()
plt.xlabel('plate_y')
plt.ylabel('plate_x(flat)')
plt.clim((-11.1, -10.3))
plt.savefig(path+'texture analysis')

#plt.figure(7, figsize = (12, 9))
#plt.title('peak position')
#plt.scatter(plate_y, plate_x, c = peak_position, s = area, marker = 's')
#plt.colorbar()
#plt.xlim((-36, 36))
#plt.ylim((-36, 36))
#plt.xlabel('plate_y')
#plt.ylabel('plate_x(flat)')
#plt.savefig(path+'peak position.png')
#
#plt.figure(8, figsize = (12, 9))
#plt.title('peak width')
#plt.scatter(plate_y, plate_x, c = peak_width, s = area, marker = 's')
#plt.colorbar()
#plt.xlim((-36, 36))
#plt.ylim((-36, 36))
#plt.clim((0, 0.3))
#plt.xlabel('plate_y')
#plt.ylabel('plate_x(flat)')
#plt.savefig(path+'peak width.png')
#
#plt.figure(9, figsize = (12, 9))
#plt.title('peak intensity')
#plt.scatter(plate_y, plate_x, c = peak_intensity, s = area, marker = 's')
#plt.colorbar()
#plt.xlim((-36, 36))
#plt.ylim((-36, 36))
#plt.xlabel('plate_y')
#plt.ylabel('plate_x(flat)')
#plt.savefig(path+'peak intensity.png')

plt.figure(9, figsize = (12, 9))
plt.title('peak num')
plt.scatter(plate_y, plate_x, c = peak_num, s = area, marker = 's')
plt.colorbar()
plt.xlim((-36, 36))
plt.ylim((-36, 36))
plt.xlabel('plate_y')
plt.ylabel('plate_x(flat)')
plt.clim((1, 20))
plt.savefig(path+'peak num.png')

#ternary_data = np.concatenate(([metal1],[metal2],[metal3],[peak_width]), axis = 0)
#ternary_data = np.transpose(ternary_data)
#
#plotTernary.plt_ternary_save(ternary_data, tertitle='',  labelNames=('Co','V','Zr'), scale=100,
#                       sv=True, svpth=path, svflnm='peak_width_ternary',
#                       cbl='Scale', vmin=0, vmax=0.3, cmap='jet', cb=True, style='h')

plt.close("all")