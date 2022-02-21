# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 22:19:20 2022

@author: ChrisZeThird
"""

import numpy as np
import matplotlib.pyplot as plt
import glob

"""Loading numpy files"""

dic = {}

for file in glob.glob("*.npy"):
    dic[str(file)] = (np.load(file))[:,1]
    
wavelength = (np.load(file))[:,0]

Files = {}
for key, val in dic.items():    
    new_key = input('Please enter a new key: ')
    Files[key] = new_key
    
for old, new in Files.items():
    dic[new] = dic.pop(old)
        

"""Ploting the datas"""

plt.figure(figsize=(16,9))
plt.suptitle('Intensité diffusée sous lumière blanche', fontsize=18)
plt.title('Milieu diffusant: Lait', fontsize=11)


for key in dic:
    plt.plot(wavelength, dic[key], label = key)
plt.legend()
plt.show()
    