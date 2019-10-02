import numpy as np

def readFromFile(textFile):
    t = []
    x = []
    y = []
    
    try:
        f = open(textFile, 'r')
    except:
        print("Could not open " + textFile)
    for line in f:
        splitted = line.split()
        t.append(float(splitted[0]))
        x.append(float(splitted[1]))
        y.append(float(splitted[2]))
        
