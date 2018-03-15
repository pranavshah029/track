# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 18:21:39 2017

@author: Durgesh Reddiyar
"""

import cv2
import numpy as np
import os
import glob

def neg_raw_images():
    pic_num=1
    
    for i in glob.glob('C:/Users/Durgesh Reddiyar/Desktop/temp jobs/hero/ori_neg/*.jpg',):
        try:
            print(i)
            img = cv2.imread('C:/Users/Durgesh Reddiyar/Desktop/temp jobs/hero/ori_neg/'+str(pic_num)+'.jpg',cv2.IMREAD_GRAYSCALE)
            resized_image = cv2.resize(img,(200,200))
            cv2.imwrite('C:/Users/Durgesh Reddiyar/Desktop/temp jobs/hero/base_output/neg/'+str(pic_num)+'.jpg',resized_image)
            pic_num += 1
        except Exception as e:
            print(str(e))
            
            
def pos_raw_images():
    pic_num=1
    
    for i in glob.glob('C:/Users/Durgesh Reddiyar/Desktop/temp haar/tush_watch/*.jpg',):
        try:
            print(i)
            img = cv2.imread('C:/Users/Durgesh Reddiyar/Desktop/temp haar/tush_watch/'+str(pic_num)+'.jpg',cv2.IMREAD_GRAYSCALE)
            resized_image = cv2.resize(img,(200,200))
            cv2.imwrite('C:/Users/Durgesh Reddiyar/Desktop/temp haar/base_output/pos/'+str(pic_num)+'.jpg',resized_image)
            pic_num += 1
        except Exception as e:
            print(str(e))            
            
            
            
            
            
            
neg_raw_images()
#pos_raw_images()       
        
        
       