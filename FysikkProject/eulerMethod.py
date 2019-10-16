# -*- coding: utf-8 -*-

import bane
import numpy as np
from matplotlib import pyplot as plt


def findStartIdx(yArr, y):
    idx = 0
    while(yArr[idx] > y):
        idx += 1
    return idx

def eulersMethod(steps, time, startPos, v0):
    stepSize = time/steps
    x, y, alpha, kappa = bane.interpolatePath(steps)
    s = np.zeros((2, len(x)))
    v = np.zeros(len(x))
    m = 0.1
    g = 9.81
    v[0] = v0
    
    i0 = findStartIdx(y,startPos)
    s[0][0] = x[i0]
    s[1][0] = y[i0]
    idx = 0
    for i in range(1, len(x)):
        startVal = 0 if(idx<10) else idx-10
        for j in range(startVal,len(x)):
            if(x[j] > s[0][i-1]):
                break
            else: 
                idx = j
        s[0][i] = s[0][i-1] + stepSize*v[i-1]*np.cos(-alpha[idx])
        s[1][i] = s[1][i-1] + stepSize*v[i-1]*np.sin(-alpha[idx])
        v[i] = v[i-1] + stepSize*9.81*np.sin(alpha[idx])/(7/5)
    Fn = m*v**2*kappa + m*g*np.cos(alpha)
    return s, v, Fn


def getValueAtTime(arr,tMax, steps, time):
    return arr[int(time/tMax * steps)]

def main():
    time = 1
    steps = 4000
    s, v = eulersMethod(steps, time,0.30)
    plt.plot(s[0],s[1])
    plt.show()
    plt.plot(s[0],v)
    plt.show()
    plt.plot(np.linspace(0,time,steps),s[1])
    
if __name__ == '__main__':
    main()