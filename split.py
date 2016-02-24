# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 16:21:18 2016

@author: joe

read five tuple data and split them to training set
"""
import numpy as np
import random

def splitData(test_split, data, label, dataset_size):
    Y_train = label[0:(1-test_split)*dataset_size, ...]
    X_train = data[0:(1-test_split)*dataset_size,]
    Y_test = label[(1-test_split)*dataset_size:, ...]
    X_test = data[(1-test_split)*dataset_size:,]
    return X_train, Y_train,X_test, Y_test
    
def shuffleData(test_split, DataPos, DataNeg, dataset_size):
    rp = list(range(dataset_size))
    random.shuffle(rp)
    
    DataPos = DataPos[rp,...]
    LabelPos = np.ones([dataset_size,], dtype=np.uint8)
    
    DataNeg = DataNeg[rp,...]
    LabelNeg = np.zeros([dataset_size,], dtype=np.uint8)
    
    X_train_pos, Y_train_pos, X_test_pos, Y_test_pos = splitData(test_split, DataPos, LabelPos, dataset_size)
    X_train_neg, Y_train_neg, X_test_neg, Y_test_neg = splitData(test_split, DataNeg, LabelNeg, dataset_size)
    
    # concatenate Pos and Neg
    X_train = np.concatenate((X_train_pos, X_train_neg))
    Y_train = np.concatenate((Y_train_pos, Y_train_neg))
    X_test = np.concatenate((X_test_pos, X_test_neg))
    Y_test = np.concatenate((Y_test_pos, Y_test_neg))

    # shuffle again
    rpTrain = list(range(X_train.shape[0]))
    random.shuffle(rpTrain)
    
    rpTest = list(range(X_test.shape[0]))
    random.shuffle(rpTest)
    
    
    X_train = X_train[rpTrain, ...]
    Y_train = Y_train[rpTrain,]
    X_test = X_test[rpTest, ...]
    Y_test = Y_test[rpTest,]
    return X_train, Y_train, X_test, Y_test 


if __name__ == '__main__':
    test_split = 0.2
    dataset_size = 20
    patch_size = 100
    
    DataPos = np.load('DataPos.npy')
    DataNeg = np.load('DataNeg.npy')

    X_train, Y_train, X_test, Y_test = shuffleData(test_split, DataPos, DataNeg, dataset_size)
    
    np.save('X_train', X_train)
    np.save('Y_train', Y_train)
    np.save('X_test', X_test)
    np.save('Y_test', Y_test)
    