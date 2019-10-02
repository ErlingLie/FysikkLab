# -*- coding: utf-8 -*-
import ReadFile

from matplotlib import pyplot as plt

def plotData(fileName):
    t,x,y = ReadFile.readFromFile(fileName)
    for i in range(10):
        plt.plot(t[i],y[i])

    plt.show()
    

def main():
    plotData("..\H1Data.txt")
    plotData("..\H2Data.txt")
    plotData("..\H3Data.txt")
    plotData("..\H4Data.txt")
    plotData("..\H3DataBehandlet.txt")
    plotData("..\destFile.txt")
    plotData("..\destination.txt")
    
main()