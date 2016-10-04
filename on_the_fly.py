# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13

@author: fangren

"""

import os.path
import time
import imp
import numpy as np
import random


# import modules
reduction = imp.load_source("data_reduction", "data_reduction.py")
Qchi = imp.load_source("save_Qchi", "save_Qchi.py")
oneDplot = imp.load_source("save_1Dplot", "save_1Dplot.py")
oneDcsv = imp.load_source("save_1Dcsv", "save_1Dcsv.py")
max_ave = imp.load_source("extract_max_ave_intensity", "extract_max_ave_intensity.py")
peak_num = imp.load_source("extract_peak_num", "extract_peak_number.py")
add_feature = imp.load_source("add_feature_to_master", "add_feature_to_master.py")
save_texture = imp.load_source("save_texture_plot_csv", "save_texture_plot_csv.py")
extract_texture = imp.load_source("extract_texture_extent", "extract_texture_extent.py")


def file_index(index):
    """
    formatting the index of each file
    """
    if len(str(index)) == 1:
        return '000' + str(index)
    elif len(str(index)) == 2:
        return '00' + str(index)
    elif len(str(index)) == 3:
        return '0' + str(index)
    elif len(str(index)) == 4:
        return str(index)

def on_the_fly(folder_path, base_filename, index, last_scan, master_index, attribute1 = [], attribute2 = [], attribute3 = []):
    """
    run when starting to collect XRD images, and finish when finishing measuring the whole library
    """    
    while (index <= last_scan):
        imageFilename = base_filename+ file_index(index) + '.tif'
        imageFullname = folder_path + imageFilename        
        print("\r")    
        # wait until an image is created, and process the previous image, to avoid crashing
        print 'waiting for image', imageFullname+' to be created...'
        print("\r")    
        while not os.path.exists(imageFullname):
            time.sleep(1)
	  #print 'sleeping'
        print 'processing image '+ imageFullname
        print("\r")
        
        while (1):
            try: 
                # data_reduction to generate Q-chi and 1D spectra, Q
                Q, chi, cake, Qlist, IntAve = reduction.data_reduction(imageFullname, \
                d_in_pixel, Rot, tilt, lamda, x0, y0, PP)
                # save Qchi as a plot *.png
                Qchi.save_Qchi(Q, chi, cake, imageFilename, save_path)
                # save 1D spectra as a *.csv
                oneDcsv.save_1Dcsv(Qlist, IntAve, imageFilename, save_path)
                # extract maximum/average intensity from 1D spectra as feature 1
                newRow1 = max_ave.extract_max_ave_intensity(IntAve, index)
                attribute1.append(newRow1)
                # save 1D texture spectra as a plot (*.png) and *.csv
                Qlist_texture, texture = save_texture.save_texture_plot_csv(Q, chi, cake, imageFilename, save_path)
                # extract texture square sum from the 1D texture spectra as feature2
                newRow2 = extract_texture.extract_texture_extent(Qlist_texture, texture, index)
                attribute2.append(newRow2)
                # extract composition information if the information is available
                #
                # extract the number of peaks in 1D spectra as feature 3
                newRow3, peaks = peak_num.extract_peak_num(Qlist, IntAve, 10, index)
                attribute3.append(newRow3)
                # add features (floats) to master metadata
                attributes = np.concatenate((attribute1, attribute2, attribute3), axis = 1)
                add_feature.add_feature_to_master(attributes, base_filename, folder_path, save_path, master_index)
                # save 1D plot with detected peaks shown in the plot
                oneDplot.save_1Dplot(Qlist, IntAve, peaks, imageFilename, save_path)                
                break
            except (OSError, IOError):
                # The image was being created but not complete yet
                print 'waiting for image', imageFullname+' to be ready...'
                time.sleep(1)
        index += 1    # next file
        

# input calibration parameters (make sure the correct calibration is entered)
d_in_pixel = 2309.54007395     # distance from sample to detector plane along beam direction in pixel space
Rot = (np.pi*2-4.72973064797)/(2*np.pi)*360  #detector rotation
tilt = 0.531406930485/(2*np.pi)*360   # detector tilt
lamda = 0.9762  # wavelength
x0 = 1034.81496248     # beam center in pixel-space
y0 = 2309.54007395    # beam center in pixel-space
PP = 0.95   # beam polarization, decided by beamline setup

# user input
folder_path = 'C:\\Research_FangRen\\Meeting notes\\20160930 Meeting with Citrine\\Data_to_be_shared_with_Citrine\\'
base_filename = 'Sample1_24x24_t30_'
index = 1   # starting from which scan#
last_scan = 441  # end with which scan# 

# generate a folder to put processed files
save_path = folder_path + 'Processed\\'
if not os.path.exists(save_path):
    os.makedirs(save_path)

# generate a random series of numbers, in case restart the measurement from the middle, the new master file will not overwrite the previous one
master_index = str(int(random.random()*100000000))

on_the_fly(folder_path, base_filename, index, last_scan, master_index)
