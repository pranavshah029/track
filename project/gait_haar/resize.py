# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 05:15:51 2017

@author: Durgesh Reddiyar
"""

import cv2
import numpy as np
import os
import glob

def resize():
    pic_num=1
    
    for i in glob.glob('1.jpg'):
        try:
            print(i)
            img = cv2.imread(str(pic_num)+'.jpg')
            resized_image = cv2.resize(img,(100,100))
            cv2.imwrite('/home/dee/track/project/gait_haar/base_output/pos/'+str(pic_num)+'.jpg',resized_image)
            #pic_num += 1
        except Exception as e:
            print(str(e))
            
resize()
