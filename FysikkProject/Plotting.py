# -*- coding: utf-8 -*-
import ReadFile
from matplotlib import pyplot as plt

def main():
    t,x,y = ReadFile.readFromFile("..\H2Data.txt")
    for i in range(10):
        plt.plot(t[i],y[i])

    plt.show()
    
main()
