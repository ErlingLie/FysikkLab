# -*- coding: utf-8 -*-
import ReadFile
import bane
from matplotlib import pyplot as plt
from eksternlab import height
import numpy as np
from eksternlab import slope
from eksternlab import curvature
def plotData(fileName):
    t,x,y = ReadFile.readFromFile(fileName)
    for i in range(10):
        plt.plot(t[i],y[i])

    plt.show()
   
    
def plotInterp():
    x,y,a,r = bane.interpolatePath(100)
    plt.plot(x,y)
    plt.show()
    plt.plot(x,a)
    plt.show()
    plt.plot(x,r)
    plt.show()


def interpExperimental():
    t, x, y = ReadFile.readFromFile("..\H3DataBehandlet.txt")
    h = height(x[3][4:],y[3][4:])
    
    x_interp = np.linspace(x[0][4],x[0][len(x[0])-1], 50)
    y_interp = h(x_interp)
    alpha = slope(h, x_interp)
    kappa = curvature(h, x_interp)
    plt.plot(x_interp,y_interp)
    plt.show()
    plt.plot(x_interp,alpha)
    plt.show()
    plt.plot(x_interp,kappa)
    plt.show()

def main():
 #  plotInterp()
   #interpExperimental()
    plotData("..\H1Data.txt")
    plotData("..\H2DataBehandlet.txt")
    plotData("..\H3Behandlet.txt")
    plotData("..\H4Data.txt")
    

    
main()
