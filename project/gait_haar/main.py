# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 06:39:10 2017

@author: Durgesh Reddiyar
"""

import cv2
import numpy as np

obj_cascade=cv2.CascadeClassifier('C:\\Users\\Pranav\\Desktop\\temp jobs\\hero\\data\\cascade.xml')

cap = cv2.VideoCapture(2)

while True:
    ret, img = cap.read()
    if ret is True:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        objects = obj_cascade.detectMultiScale(gray)
        for (x,y,w,h) in objects:
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img,'HERO found',(x-w, y-h), font,0.5, (0,255,255), 1,cv2.LINE_AA)
            cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
        
        cv2.imshow('Detecting', img)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break

cap.release()
cv2.destroyAllWindows()