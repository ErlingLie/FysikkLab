# -*- coding: utf-8 -*-
import ReadFile
import bane
from matplotlib import pyplot as plt
from eksternlab import height
import numpy as np
from eksternlab import slope
from eksternlab import curvature
from eksternlab import Lane

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


def interpExperimental(stepsize):
   t, x, y = ReadFile.readFromFile("..\H2DataBehandlet.txt")
   vTopp = [[],[]]
   for i in range(len(t)):
       x_Cs = height(t[i], x[i])
       y_Cs = height(t[i], y[i])
       t_interp = np.linspace(0.0, t[i][len(t[i])-1], stepsize)
       
       y_interp = y_Cs(t_interp)
       ymax = 0
       index = 0
       for j in range(int(stepsize*0.6),len(t_interp)):
           if(y_interp[j]>ymax):
               ymax = y_interp[j]
               index = j
       
       vy = y_Cs(t_interp, 1)
       vx = x_Cs(t_interp, 1)
       vxMax = vx[index]
       vyMax = vy[index]
       vTopp[0].append([vxMax])
       vTopp[1].append([vyMax])
       print(format(ymax,'.3f'), format(vxMax,'.3f', ), format(vyMax,'.3f'))
       print()
   return vTopp


def plotLane():
    t,x,y = ReadFile.readFromFile("..\H4Data.txt")
    
    lane = Lane(x[0],y[0])
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(x, y, 'o', mfc='none', label='Datapunkter', markersize=5)
    height = lane.height()
    ax.plot(x, height(x), label='Tilpasset')
    ax.set_xlabel('x posisjon (m)')
    ax.set_ylabel('y posisjon (m)')
    ax.legend()
    plt.show()

def main():
 #  plotInterp()
   #interpExperimental()
   # plotData("..\H1Data.txt")
   # plotData("..\H2DataBehandlet.txt")
    #plotData("..\H3Behandlet.txt")
    #plotData("..\H4Data.txt")
   # plotInterp()
    interpExperimental(1000)
   #plotLane()
    

    
main()
