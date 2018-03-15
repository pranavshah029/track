# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 19:22:43 2017

@author: Durgesh Reddiyar
"""

import numpy as np
import cv2
import os
import glob

def create_pos_n_neg():
    for file_type in ['neg']:
        
        for img in os.listdir(file_type):
            if file_type == 'neg':
                line = file_type+'/'+img+'\n'
                with open ('bg.txt', 'a') as f:
                     f.write(line)
                     f.close
                     
"""
            elif file_type == 'pos': 
                 line = file_type+'/'+img+' 1 0 0 200 200\n'
                 with open ('info.dat', 'a') as f:
                      f.write(line)
                      f.close
                      
"""
                    
def stack_code():
    WD = "C:\\Users\\Durgesh Reddiyar\\Desktop\\temp haar\\base_output\\neg"

    files = glob.glob ('*.jpg')
    with open ('bg.txt', 'w') as in_files:
        for eachfile in files: in_files.write(eachfile+'\n')
 


#stack_code()                   
create_pos_n_neg()