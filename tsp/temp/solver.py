#!/usr/bin/python
# -*- coding: utf-8 -*-

import math
import random

def length(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def solveIt(inputData):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = inputData.split('\n')

    nodeCount = int(lines[0])
    test=[]

    points = []
    temp_points = {}
    for i in range(1, nodeCount+1):
        line = lines[i]
        parts = line.split()
        points.append((float(parts[0]), float(parts[1])))
        temp_points[i-1]=float(parts[0]), float(parts[1])
        test.append(i-1)

    dis=0
    #print temp_points[0]
    f=0
    path=[f]
    closed=[]
    total=0
    c=0
    pos=0
    point = points[f]
    del temp_points[f]
    #points.remove(point)
    while(1):
        mini = 999999999999999
        #closed.append(point)
        for i in temp_points.keys():
            dis = length(point,temp_points[i])
            if mini > dis:
                mini = dis
                pos = i
        #print c
        c=c+1
        if c == nodeCount:
            break
        else:
            #print "pos",pos,temp_points
            total=total+mini
            path.append(pos)
            point = points[pos]
            del temp_points[pos]
            
    #print  "temp", path
    #t=cal_dis(path,points)
    #print "sum1",t,path

    path.append(f)
    chk=opt2(path,points)
    d=0
    #for i in range(0,500):
    while(1):
        if chk[1] == False:
            break
        else:
            chk=opt2(chk[0],points)
        total=cal_dis(chk[0],points)
        """    #print total
        print "big total",total
        if total < 440:
            d=d+1
            print "piiinnkkyy"
        if d>1:
            print "fuck"
            break
        random.shuffle(test)
        chk=opt2(test,points)"""

    # build a trivial solution
    # visit the nodes in the order they appear in the file
    #solution = range(0, nodeCount)

    # calculate the length of the tour
    #obj = length(points[solution[-1]], points[solution[0]])
    #for index in range(0, nodeCount-1):
     #   obj += length(points[solution[index]], points[solution[index+1]])

    # prepare the solution in the specified output format
    outputData = str(total) + ' ' + str(0) + '\n'
    outputData += ' '.join(map(str, chk[0]))

    return outputData

def opt2(path,points):
    temp=[]
    new_path=[]
    for i in range(0,len(path)-1):
        #print i
        edge1 = (points[path[i]],points[path[i+1]])
        #print "edge1",edge1
        new_path.append(path[i])
        for j in range(i+2,len(path)-1):
            edge2 = (points[path[j]],points[path[j+1]])
            #print "edge2",edge2
            if edge1[0]==points[path[0]] and edge2[1]==points[path[0]]:
                continue            
            else:
                if intersect(edge1[0],edge1[1],edge2[0],edge2[1]):
                    temp=[]
                    for i in path[i+1:j+1]:
                        temp.append(i)
                    temp.reverse()   
                    new_path.extend(temp)
                    new_path.extend(path[j+1:])
                #print "yyyeeeeeeessssssss",temp
                #bre
                #path=new_path
                #print "yes",temp
                    return new_path,True
            #else:
             #   new_path.append()
    new_path.append(path[len(path)-1])         
    return new_path,False

def cal_dis(path,points):
    total=0
    for i in range(0,len(path)-1):
        total=total+length(points[path[i]],points[path[i+1]])
    return total
        
def ccw(A,B,C):
    return (C[1]-A[1])*(B[0]-A[0]) > (B[1]-A[1])*(C[0]-A[0])

def intersect(A,B,C,D):
    #print A,B,C,D
    return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)

    
import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        fileLocation = sys.argv[1].strip()
        inputDataFile = open(fileLocation, 'r')
        inputData = ''.join(inputDataFile.readlines())
        inputDataFile.close()
        print solveIt(inputData)
    else:
        print 'This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/tsp_51_1)'

