#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import namedtuple
Item = namedtuple("Item", ['index', 'value', 'weight'])

def getEstimate(weight, value, capacity, valid, density):
    weights = weight[:]
    values = value[:]
    n = len(values)
    used = 0
    i = 1
    estimate = 0
    while i < n and used + weights[i] <= capacity:
        if valid[i] == 1:
            estimate += values[i]
            used += weights[i]
        i += 1
    if i < n:
        while(i < n and valid[i] == 0):
            i += 1
        if i < n:
            estimate += density[i] * (capacity - used)
    print estimate
    return int(estimate)



def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])

    #   My code starts here

    value = [0]
    weight = [0]
    line = []
    for i in range(1, item_count + 1):
        line = lines[i]
        parts = line.split()
        value.append(int(parts[0]))
        weight.append(int(parts[1]))

    index = [x for x in range(item_count + 1)]
    
    level = 1
    current = [1 for x in range (item_count + 1)]
    best = []
    maxValue = -1
    occupied = 0
    visited = [False for x in range(item_count + 1)]
    curValue = 0

    density = [0]
    for i in range(1, item_count + 1):
        density.append(float(value[i]) / weight[i])

    for j in range(2, item_count + 1):
        d = density[j]
        v = value[j]
        w = weight[j]
        ind = index[j]
        i = j - 1
        while i >= 1 and density[i] < d:
            density[i + 1] = density[i]
            value[i + 1] = value[i]
            weight[i + 1] = weight[i]
            index[i + 1] = index[i]
            i = i - 1
        density[i + 1] = d
        value[i + 1] = v
        weight[i + 1] = w
        index[i + 1] = ind

    curEst = getEstimate(weight, value, capacity, current, density)
    while (True):
        if (level == 0):
            break
        else:
            if (level == item_count):
                if (occupied + weight[level] <= capacity):
                    current[level] = 1
                    curValue += value[level]
                    if (curValue > maxValue):
                        best = current[:]
                        maxValue = curValue
                    curValue -= value[level]
                    
                else:
                    current[level] = 0
                    if (curValue > maxValue):
                        best = current[:]
                        maxValue = curValue
                level -= 1
                
            else:
                if (visited[level] == False):
                    visited[level] = True
                    if (occupied + weight[level] > capacity):
                        current[level] = 0
                        curEst = getEstimate(weight, value, capacity, current, density)
                        if (curEst > maxValue):
                            level += 1
                        else:
                            level -= 1
                            
                    else:
                        current[level] = 1
                        occupied += weight[level]
                        curValue += value[level]
                        level += 1
                else:
                    if (current[level] == 0):
                        level -= 1
                        for i in range(level + 1, item_count + 1):
                            current[i] = current[i]
                        curEst = getEstimate(weight, value, capacity, current, density)
                        while(level > 0 and current[level] == 0 and curEst <= maxValue):
                            level -= 1
                            for i in range(level + 1, item_count + 1):
                                current[i] = current[i]
                            curEst = getEstimate(weight, value, capacity, current, density)
                    else:
                        current[level] = 0
                        curValue -= value[level]
                        occupied -= weight[level]
                        for i in range(level + 1, item_count + 1):
                            current[i] = 1
                        curEst = getEstimate(weight, value, capacity, current, density)
                        if (curEst > maxValue):
                            level += 1
                            for j in range(level, item_count + 1):
                                visited[j] = False
                        else:
                            level -= 1
    

    for j in range(2, item_count + 1):
        b = best[j]
        ind = index[j]
        i = j - 1
        while i >= 1 and index[i] > ind:
            best[i + 1] = best[i]
            index[i + 1] = index[i]
            i = i - 1
        best[i + 1] = b
        index[i + 1] = ind
        
    output_data = str(maxValue) + ' ' + str(1) + '\n'
    for i in range(1, item_count + 1):
        output_data += str(best[i]) + ' '
    return output_data


    

import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        input_data_file = open(file_location, 'r')
        input_data = ''.join(input_data_file.readlines())
        input_data_file.close()
        print solve_it(input_data)
    else:
        print 'This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)'

