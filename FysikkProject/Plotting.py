# -*- coding: utf-8 -*-
import ReadFile
import bane
import eulerMethod
import Gjennomsnitt
from matplotlib import pyplot as plt
from eksternlab import height
import numpy as np
from eksternlab import slope
from eksternlab import curvature
from eksternlab import Lane


def plotXY(fileName):
    t,x,y = ReadFile.readFromFile(fileName)
    for i in range(10):
        plt.plot(np.array(x[i])+1,y[i])

def plotTimeY(fileName):
    t,x,y = ReadFile.readFromFile(fileName)
    for i in range(10):
        plt.plot(t[i],y[i])
    
def plotInterp():
    x,y,a,r = bane.interpolatePath(100)
    plt.plot(x,y)
    plt.show()
    plt.plot(x,a)
    plt.show()
    plt.plot(x,r)
    plt.show()




def interpExperimental(steps, filename):
   t, x, y, s = ReadFile.readFromFile(filename)
   vTopp = [[],[]]
   m = 0.1
   g = 9.81
   #t is two dimentional and this function finds vMax for all iterations
   vX2D = []
   vY2D = []
   N2D = []
   xLane =  np.linspace(-1, 0.4, 8)
   yLane = np.array([0.471, 0.301, 0.161, 0.094, 0.169, 0.255, 0.170, 0.094])
   h = height(xLane,yLane)
   for i in range(len(t)): 
       x_Cs = height(t[i], x[i])
       y_Cs = height(t[i], y[i])
       t_interp = np.linspace(0.0, t[i][len(t[i])-1], steps)
       y_interp = y_Cs(t_interp)
       x_interp = x_Cs(t_interp)
       alpha = slope(h,x_interp)
       kappa = curvature(h, x_interp)
       
       vy = y_Cs(t_interp, 1)
       vx = x_Cs(t_interp, 1)
       vsquared = vx**2 + vy**2
       N = m*vsquared*kappa + m*g*np.cos(alpha)
       N2D.append(N)
       vX2D.append(vx)
       vY2D.append(vy)
       
       ymax = 0
       index = 0
       for j in range(int(steps*0.6),len(t_interp)): #Find yMax index
           if(y_interp[j]>ymax):
               ymax = y_interp[j]
               index = j
       
    
       vxMax = vx[index]
       vyMax = vy[index]
       vTopp[0].append([vxMax])
       vTopp[1].append([vyMax])
       #print(format(ymax,'.3f'), format(vxMax,'.3f', ), format(vyMax,'.3f'))
       #print()
   return vTopp, vX2D, vY2D, t_interp, N2D


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


def meanList(dataList):
    newList = []
    for i in range(len(dataList[0])):
        tempList = [lst[i] for lst in dataList]
        newList.append(Gjennomsnitt.mean(tempList))
    return newList


def standardDeviationList(dataList):
    newList = []
    for i in range(len(dataList[0])):
        tempList = [lst[i] for lst in dataList]
        newList.append(Gjennomsnitt.standardDeviation(tempList))
    return newList


def plotTimeN(fileName, steps, Fn):
    vt, vx, vy, t, N = interpExperimental(steps, fileName)
    nMean = meanList(N)
    nStdDiv = standardDeviationList(N)
    fig = plt.figure("Normal-time-plot" + fileName)
    ax = fig.add_subplot(1,1,1)
    ax.errorbar(t,nMean,yerr = nStdDiv, errorevery = len(nMean)//10, 
                ecolor = 'black', uplims = True, lolims = True, 
                label = "Experimental data" + fileName,
                color = "orange", linewidth = 2.5)
    ax.plot(t, Fn, label = "Normal force numerical")
    ax.set_xlabel('t (s)', fontsize = 20)
    ax.set_ylabel('Fn (N)', fontsize = 20)
    ax.legend(fontsize = 15)
    plt.show()
    
    
def plotMeanXY(fileName, sNumerical):
    t,x,y, s = ReadFile.readFromFile(fileName)
    fig = plt.figure("XY-plot" + fileName)
    ax = fig.add_subplot(1, 1, 1)
    
    xMean = meanList(x)
    yMean = meanList(y)
    yStdDiv = standardDeviationList(y)
    ax.errorbar(np.array(xMean) + 1, yMean, yerr = yStdDiv, errorevery = len(yMean)//10, ecolor = 'black', uplims = True, lolims = True, label = fileName, color = 'orange', linewidth = 2.5)
    ax.plot(sNumerical[0],sNumerical[1], label = "Numerical", linewidth = 2.5)
    ax.set_xlabel('x-posisjon (m)', fontsize = 20)
    ax.set_ylabel('y-posisjon (m)', fontsize = 20)
    ax.legend(fontsize = 15)
    plt.show()
    

def plotMeanTimeY(fileName, sNumerical):
    t,x,y,s = ReadFile.readFromFile(fileName)
    fig = plt.figure("Time, Y-pos plot" + fileName)
    ax = fig.add_subplot(1, 1, 1)
    tMean = meanList(t)
    yMean = meanList(y)
    yStdDiv = standardDeviationList(y)
    
    ax.errorbar(tMean, yMean, yerr = yStdDiv, errorevery = len(yMean)//10,
                ecolor = 'black', uplims = True, lolims = True,
                label = fileName, linewidth = 2.5, color = 'orange')
    ax.plot(np.linspace(0,t[0][-1],4000), sNumerical[1], label = "Numerical", linewidth = 2.5)
    ax.set_xlabel('t (s)', fontsize = 20)
    ax.set_ylabel('y-posisjon (m)', fontsize = 20)
    ax.legend(fontsize = 15)
    plt.show()
    
def plotMeanTimeS(fileName, sNumerical):
    t,x,y, s = ReadFile.readFromFile(fileName)
    fig = plt.figure("Time, S-pos plot" + fileName)
    ax = fig.add_subplot(1, 1, 1)
    tMean = meanList(t)
    sMean = meanList(s)
    sStdDiv = standardDeviationList(s)
    
    ax.errorbar(tMean, sMean, yerr = sStdDiv, errorevery = len(sMean)//10,
                ecolor = 'black', uplims = True, lolims = True,
                label = fileName, linewidth = 2.5, color = 'orange')
    ax.plot(np.linspace(0,t[0][-1],4000), np.sqrt(sNumerical[0]**2 + sNumerical[1]**2),
            label = "Numerical", linewidth = 2.5)
    ax.set_xlabel('t (s)', fontsize = 20)
    ax.set_ylabel('S-posisjon (m)', fontsize = 20)
    ax.legend(fontsize = 15)
    plt.show()

def plotTimeVelocity(fileName, steps):
    vTopp, vX, vY, t, N = interpExperimental(steps, fileName)
    v = []
    for i in range(len(vX)):
        v.append(np.sqrt(vX[i]**2 + vY[i]**2))
    for i in range(len(v)):    
        plt.plot(t,v[i])
    sNumerical, v, Fn = eulerMethod.eulersMethod(steps, t[-1], 0.40, np.sqrt(vX[0][0]**2 + vY[0][0]**2))
    plt.plot(t,v)
    plt.show()

def plotMeanTimeVelocity(fileName, steps):
    vTopp, vX, vY, t, N = interpExperimental(steps, fileName)
    v = []
    for i in range(len(vX)):
        v.append(np.sqrt(vX[i]**2 + vY[i]**2))
    vMean = meanList(v)
    vStdDiv = standardDeviationList(v)
    fig = plt.figure("Time velocity plot" + fileName)
    ax = fig.add_subplot(1, 1, 1)
    ax.errorbar(t,vMean, yerr = vStdDiv, errorevery = steps//10,
                ecolor = 'black', uplims = True, lolims = True,
                label =  fileName + " mean velocity", linewidth = 2.5,
                color = 'orange')
    v0 = vMean[0]
    if(fileName == "..\H4Data.txt"):
        v0 -= 0.12
    sNumerical, v, Fn = eulerMethod.eulersMethod(steps, t[-1], 0.40, v0)
    ax.plot(t,v, label = "Numerical velocity", linewidth = 2.5)
    ax.set_xlabel('t (s)', fontsize = 20)
    ax.set_ylabel('velocity (m/s)', fontsize = 20)
    ax.legend(fontsize = 15)
    plt.show()  


def plotAllData(fileName, steps, h0):
    vTopp, vX, vY, t, N = interpExperimental(steps, fileName)
    v0 = np.sqrt(vX[0][0]**2 + vY[0][0]**2)
    if fileName == "..\H4Data.txt":
        v0 -= 0.12
    sNumerical, v, Fn = eulerMethod.eulersMethod(steps, t[-1],h0, v0)
    #plotMeanXY(fileName, sNumerical)
    #plotMeanTimeVelocity(fileName, 4000)
    #plotMeanTimeY(fileName, sNumerical)
    #plotMeanTimeS(fileName, sNumerical)
    plotTimeN(fileName, steps, Fn)

def main():   
    filenames = ["..\H1DataJukset.txt", "..\H2DataBehandlet.txt", "..\H3Behandlet.txt", "..\H4Data.txt"]
    heights = [0.213, 0.2925, 0.365, 0.390]
   #Plot velocity against time
   #Experimental
    #plotTimeVelocity("..\H4Data.txt", 4000)
    steps = 4000
    for i in range(4):
        plotAllData(filenames[i], steps, heights[i])



main()
