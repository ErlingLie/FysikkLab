# -*- coding: utf-8 -*-
from eksternlab import height
import numpy as np
from eksternlab import slope
from eksternlab import curvature



def interpolatePath(steps):
    ''' Funksjonen interpolerer mellom opphengingspunktene
    og returnerer x-, y-koordinater, helningsvinkel og krumningsradius.'''
    x =  np.linspace(0.0, 2.0, 8)
    y =  [47.1, 30.1, 16.1, 9.4, 16.9, 25.5, 17.0, 9.4]
    
    h = height(x,y)

    x_interp = np.linspace(0.0, 2.0, steps)
    y_interp = h(x_interp)
    alpha = slope(h, x_interp)
    
    kappa = curvature(h, x_interp)
    
    r = np.array(kappa)
    
    return x_interp, y_interp, alpha, r
