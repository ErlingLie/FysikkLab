# -*- coding: utf-8 -*-
from eksternlab import height
import numpy as np
from eksternlab import slope
from eksternlab import curvature



def interpolatePath(steps):
    ''' Funksjonen interpolerer mellom opphengingspunktene
    og returnerer x-, y-koordinater, helningsvinkel og krumningsradius.'''
    x =  np.linspace(0.0, 1.4, 8)
    #y =  [47.1, 30.1, 16.1, 9.4, 16.9, 25.5, 17.0, 9.4]
    y = [0.471, 0.301, 0.161, 0.094, 0.169, 0.255, 0.170, 0.094]
    h = height(x,y)

    x_interp = np.linspace(0.0, 1.4, steps)
    y_interp = h(x_interp)
    alpha = slope(h, x_interp)
    
    kappa = curvature(h, x_interp)
    
    
    return x_interp, y_interp, alpha, kappa
