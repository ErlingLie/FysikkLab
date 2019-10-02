import numpy as np

def readFromFile(textFile):
    t_list = []
    x_list = []
    y_list = []
  
    for i in range(10):
        t_list.append([])
        x_list.append([])
        y_list.append([])
    try:
        f = open(textFile, 'r')
    except:
        print("Could not open " + textFile)
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
    
    for lst in t_list:
        lst = np.array(lst)
    for lst in x_list:
        lst = np.array(lst)
    for lst in y_list:
        lst = np.array(lst)
    return t_list, x_list, y_list
        
