# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 15:59:08 2018

@author: zhangjun
"""
import numpy as np
y = np.array([1,1,0,1,0,0,1,0,1,1])
pi = 0.5
q = 0.5
p = 0.5
# fasten xita , solve Q
# pzx = pxz*pz/xigma(pxz*pz)
i = 0
while i < 10:
    pi0 = pi
    q0 = q
    p0 = p    
    wi = pi0*q0**y*(1-q0)**(1-y)/(pi0*q0**y*(1-q0)**(1-y)+
                        (1-pi0)*p0**y*(1-p0)**(1-y))
    # fasten Q , solve xita
    pi = np.mean(wi)
    q = np.sum(wi*y)/np.sum(wi)
    p = np.sum((1-wi)*y)/np.sum(1-wi)
    i = i + 1
    print (i,pi,q,p)
    if (pi-pi0)**2+(q-q0)**2+(p-p0)**2<0.00001:
        break

pyz = (pi*q**y*(1-q)**(1-y)+(1-pi)*p**y*(1-p)**(1-y))
print ('L = ',np.sum(pyz))