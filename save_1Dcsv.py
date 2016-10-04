# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13

@author: fangren

"""

import csv

def save_1Dcsv(Qlist, IntAve, imageFilename, save_path):
    """
    Qlist and IntAve are data. They are two 1D arrays created by 1D integrate function. 
    The function takes the two arrays and write them into two columns in a csv file
    imageFilename has the fomart of "*_0100.tif", the 1D csv will have the format of "_0100_1D.csv"
    """
    rows = zip(Qlist, IntAve)
    with open(save_path + imageFilename[:-4]+'_1D.csv', 'a') as csvoutput:
        writer = csv.writer(csvoutput, delimiter = ',', lineterminator = '\n')
        for row in rows:
            writer.writerow(row)
        csvoutput.close()

