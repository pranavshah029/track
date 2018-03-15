# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 19:22:43 2017

@author: Durgesh Reddiyar
"""

import numpy as np
import cv2
import os


def create_pos_n_neg():
    for file_type in ['/home/dee/track/project/gait_haar/base_output/neg']:
        
        for img in os.listdir(file_type):
            if file_type == 'neg':
                line = file_type+'/'+img+'\n'
                with open('bg.txt','a') as f:
                    f.write(line)
        """            
           elif file_type == 'pos': 
                 line = file_type+'/'+img+' 1 0 0 200 200\n'
                 with open('info.dat','a') as f:
                     f.write(line)
           """          
create_pos_n_neg()
