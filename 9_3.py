# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 16:18:25 2018

@author: zhangjun
"""
import numpy as np
y = np.array([-67,-48,6,8,14,16,23,24,28,29,41,49,56,60,75])
k = 3
w = np.random.random(k)
w = w/np.sum(w)
u = np.random.random(k)*30
xigma = np.random.random(k)*10
print (0,w,u,xigma)
# fasten xita , solve Q
# pzx = pxz*pz/xigma(pxz*pz)
i = 0
while i < 10:
    w_ = w
    u_ = u
    xigma_ = xigma
    wi = 0
    for j in np.arange(k):
        wi = wi + w_[j]/np.sqrt(2*np.pi*xigma_[j])*np.exp(-(y-u_[j])**2/2/xigma_[j])        
    for j in np.arange(k):
        wk = w_[j]/np.sqrt(2*np.pi*xigma_[j])*np.exp(-(y-u_[j])**2/2/xigma_[j])/wi
#        print (wk[0])
        w[j] = np.mean(wk)
        u[j] = np.sum(wk*y)/np.sum(wk)
        xigma[j] = np.sum(wk*(y - u_[j])**2)/np.sum(wk)
    i = i + 1
    print (i,w,u,xigma)
    if np.mean((w-w_)**2+(u-u_)**2+(xigma-xigma_)**2)<3*0.00001:
        break
# maximum likelihood estimation
print ('MLE',np.sum(wi))