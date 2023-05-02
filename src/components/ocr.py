# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 23:49:25 2023

@author: Md Mamunur Rahman, PH: +1 6474473215
"""

import pytesseract
import cv2

class OCRTesseract:
    def __init__(self):
        self
        
    def image_to_text(self,filepath):
        img = cv2.imread(filepath[0])
        custom_config = r'--oem 3 --psm 6'
        text = pytesseract.image_to_string(img, config=custom_config)
        print(text)
        return text
        
# ocrt=OCRTesseract()
# print(ocrt.image_to_text('C:/Mamun/ML/banyan_tree/Screenshot_2023-04-20-10-32-15-881_com.bumble.app.jpg'))

