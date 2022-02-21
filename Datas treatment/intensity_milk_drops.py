# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 21:14:46 2022

@author: ChrisZeThird

The goal of this programm is to convert "," to "." in a certain amount of files records, in order to use 
them in Numpy and Matplotlib afterwards.
"""

import numpy as np
import glob
import shutil
import os

txtfiles = []
for file in glob.glob("*.txt"):
    txtfiles.append(file)

"""The code below gets files from a directory, clone them and replace the ',' with '.'"""
string = "_copy"
txtfiles_copy = [x[:-4] + "_copy.txt" for x in txtfiles]

n = len(txtfiles)    

for k in range(n):
    file = txtfiles[k]
    if os.path.isfile(file[:-4]+string):
        break
    else:
        shutil.copy(file, txtfiles_copy[k])

for k in range(n):
    f1 = open(txtfiles[k],'r')
    f2 = open(txtfiles_copy[k],'w')
    for line in f1:
        f2.write(line.replace(',','.'))
    f1.close()
    f2.close()    

files = [np.loadtxt(x) for x in txtfiles_copy]
I0 = np.loadtxt("I0.txt")