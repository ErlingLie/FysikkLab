# -*- coding: utf-8 -*-
import ReadFile
import numpy as np
def cleanData(string):
    f = open(string,"r")
    w = open("..\destination.txt","w")
    for line in f:
        for s in line.split():
            val = 0
            try:
                val = float(s)
            except:
                lst = s.split("E")
                val = float(lst[0])* 10**int(lst[1])
            w.write(str(val).strip()+ "\t")
        w.write("\n")
    f.close()
    w.close()
    return



def timeShiftData(fileName):
    t,x,y = ReadFile.readFromFile(fileName)
    
    for i in range(len(t)):
        while(abs(y[i][1]-y[i][0]) < 0.000065):
            x[i] = x[i][1:]
            y[i] = y[i][1:]
    f = open("..\destFile.txt", "w")
    for i in range(len(y[0])):
        for j in range(10):
            if(i<len(y[j])):
                f.write(str(t[j][i]) + " ")
                f.write(str(x[j][i]) + " ")
                f.write(str(y[j][i]) + "\t")
            else:
                f.write(str(t[0][i]) + " ")
                f.write(str(0) + " ")
                f.write(str(0) + "\t")
        f.write("\n")
    f.close()
            


def fixData2():
    t,x,y = ReadFile.readFromFile("..\H3Behandlet.txt")
    f = open("..\cleanedFile.txt","w")
    for i in range(len(t[0])):
        for j in range(10):
            f.write(format(t[j][i],'.5f') + "\t")
            f.write(format(x[j][i],'.5f') + "\t")
            f.write(format(y[j][i],'.5f') + "\t\t")
        f.write("\n")
    f.close()

fixData2()

