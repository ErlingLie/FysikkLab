import numpy as np

def readFromFile(textFile):
    t_list = []
    x_list = []
    y_list = []
    s_list = []
    for i in range(10):
        t_list.append([])
        x_list.append([])
        y_list.append([])
        
    f = ""
    try:
        f = open(textFile, 'r')
    except:
        print("Could not open " + textFile)
        return [],[],[], []
    for line in f:
        splitted = line.split()
        i = 0
        while(i < len(splitted)):
            t_list[i//3].append(float(splitted[i].strip()))
            i +=1
            x_list[i//3].append(float(splitted[i].strip()))
            i +=1
            y_list[i//3].append(float(splitted[i].strip()))
            i += 1
    
    f.close()
    for i in range(10):
        s_list.append(np.sqrt((np.array(x_list[i])+1)**2 + np.array(y_list[i])**2))
    return t_list, x_list, y_list, s_list
        
