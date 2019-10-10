# -*- coding: utf-8 -*-

import bane
import numpy as np
from matplotlib import pyplot as plt

def eulersMethod(steps, time):
    stepSize = time/steps
    x, y, alpha, kappa = bane.interpolatePath(steps)
    s = np.zeros((2, len(x)))
    v = np.zeros(len(x))
    plt.plot(x,alpha)
    plt.show()
    
    s[0][0] = x[int(0.1*steps)]
    print(s[0][0])
    s[1][0] = y[int(0.1*steps)]
    print(s[1][0])
    idx = 0
    for i in range(1, len(x)):
        for j in range(idx,len(x)):
            if(x[j] > s[0][i-1]):
                break
            else: 
                idx = j
        s[0][i] = s[0][i-1] + stepSize*v[i-1]*np.cos(-alpha[idx])
        s[1][i] = s[1][i-1] + stepSize*v[i-1]*np.sin(-alpha[idx])
        v[i] = v[i-1] + stepSize*9.81*np.sin(alpha[idx])/(7/5)
    return s, v


def getValueAtTime(arr,tMax, steps, time):
    return arr[int(time/tMax * steps)]

def main():
    time = 1
    steps = 4000
    s, v = eulersMethod(steps, time)
    plt.plot(s[0],s[1])
    plt.show()
    plt.plot(s[0],v)
    plt.show()
    plt.plot(np.linspace(0,time,steps),s[1])
    
main()