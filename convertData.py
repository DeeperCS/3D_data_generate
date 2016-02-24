# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 15:27:25 2016

@author: joe

Read tif images and convert them to five tuple 
# samples, frames, height, width, channel
"""

import os
import numpy as np
import cv2

def readAndResize(filePath = None, needResize = False, resize = (100, 100)):
    img = cv2.imread(filePath)
    if needResize:
        img = cv2.resize(img, resize)
    return img


if __name__=='__main__': 
    resizeWidth = 100
    resizeHeight = 100
    channel = 3
    DataPos = np.zeros([20, 5, resizeWidth, resizeHeight, channel], dtype=np.float32)    # samples, frames, height, width
    DataNeg = np.zeros([20, 5, resizeWidth, resizeHeight, channel], dtype=np.float32)
    
    rootDir = './positive'
    for idxSample, folderName in enumerate(os.listdir(rootDir)):
    #    print folderName
        folderPath = os.path.join(rootDir, folderName)
        for idxFrame, fileName in enumerate(os.listdir(folderPath)):
            filePath = os.path.join(folderPath, fileName)
            imgArr = readAndResize(filePath, needResize = True, resize=(resizeWidth, resizeHeight))
            """ fill with DataPos
            """
            DataPos[idxSample, idxFrame, :, :] = imgArr
            print('idxSample, idxFrame ', idxSample, idxFrame)
            print('reading... ', filePath)
    
           
    rootDir = './negative'
    for idxSample, folderName in enumerate(os.listdir(rootDir)):
    #    print folderName
        folderPath = os.path.join(rootDir, folderName)
        for idxFrame, fileName in enumerate(os.listdir(folderPath)):
            filePath = os.path.join(folderPath, fileName)
            imgArr = readAndResize(filePath, needResize = True, resize=(resizeWidth, resizeHeight))
            """ fill with DataNeg
            """
            DataNeg[idxSample, idxFrame, :, :] = imgArr
            print('idxSample, idxFrame ', idxSample, idxFrame)
            print('reading... ', filePath)
        
#        np.save('DataPos.npy', DataPos) 
#        np.save('DataNeg.npy', DataNeg) 
