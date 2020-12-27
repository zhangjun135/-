# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 20:06:37 2020

@author: zhangjun
"""

import numpy as np

class perceptron:
    def __init__(self):
        self.w = None
        self.b = None
    
    def train(self, x, y, learning_rate=1):
        self.w = np.zeros(x.shape[1])
        self.b = np.zeros(1)      
        while True:
            index_ms = 0    
            for index,x_i in enumerate(x):
                index_s = y[index]*(np.sum(self.w*x_i) + self.b)                
                if index_s<=0:
                    self.w = self.w + learning_rate*y[index]*x_i
                    self.b = self.b + learning_rate*y[index]
                    break
                index_ms = index_ms + 1                
            print (self.w,self.b)    
            if index_ms==x.shape[0]:
                break            
            
    def prediction(self,x_pred):
        y_pred = np.zeros(x_pred.shape[0])
        for index,x_i in enumerate(x_pred):
            y_pred[index] = np.sum(self.w*x_i) + self.b
            if y_pred[index]>0:
                y_pred[index] = 1
            else:
                y_pred[index] = -1
        return y_pred

if __name__ == '__main__':
    x = np.array([[3,3],[4,3],[1,1]])
    y = np.array([1,1,-1])
    Model = perceptron()
    Model.train(x,y,learning_rate=0.1)
    y_pred = Model.prediction(x)
    print ('w,b=',Model.w,Model.b)
            