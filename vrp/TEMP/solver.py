#!/usr/bin/python
# -*- coding: utf-8 -*-

import math
import random
import matplotlib.pyplot as plt
dic={}

def length(customer1, customer2):
    return math.sqrt((customer1[1] - customer2[1])**2 + (customer1[0] - customer2[0])**2)

def solveIt(inputData):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = inputData.split('\n')

    parts = lines[0].split()
    customerCount = int(parts[0])
    vehicleCount = int(parts[1])
    vehicleCapacity = int(parts[2])
    depotIndex = 0
    points=[]
    #dic={}

    customers = []
    for i in range(1, customerCount+1):
        line = lines[i]
        parts = line.split()
        d=(int(parts[0]), float(parts[1]),float(parts[2]))
        customers.append(d)
        points.append((d[1],d[2]))
        dic[(d[1],d[2])] = (i-2,d[0])

    # build a trivial solution
    # assign customers to vehicles starting by the largest customer demands

    vehicleTours = []

    customerIndexs = set(range(1, customerCount))  # start at 1 to remove depot index
    print customers

    

    initial = points[0]
    points = points[1:]

    #print id_c
    cenp=[]

    for k in range(0,4):
        cen=[]
        cenp,id_c = cluster(points,vehicleCount,cenp)
        for i in cenp:
            cen.append(points[i])
        #print cen
        plt.scatter(initial[0],initial[1],s=500,c='0',marker='*')
        for i in range(0,len(points)):
            #if id_c[i] in cen:
             #   plt.scatter(points[i][0],points[i][1],s=200,c='0')
            if id_c[i]==0:
                plt.scatter(points[i][0],points[i][1],s=40,c='r')
                if points[i] in cen:
                    plt.scatter(points[i][0],points[i][1],s=100,c='r',marker='D')
            elif id_c[i]==1:
                plt.scatter(points[i][0],points[i][1],s=40,c='b')
                if points[i] in cen:
                    plt.scatter(points[i][0],points[i][1],s=100,c='b',marker='D')
            elif id_c[i]==2:
                plt.scatter(points[i][0],points[i][1],s=40,c='g')
                if points[i] in cen:
                    plt.scatter(points[i][0],points[i][1],s=100,c='g',marker='D')
            elif id_c[i]==3:
                plt.scatter(points[i][0],points[i][1],s=40,c='c')
                if points[i] in cen:
                    plt.scatter(points[i][0],points[i][1],s=100,c='c',marker='D')
            elif id_c[i]==4:
                plt.scatter(points[i][0],points[i][1],s=40,c='y')
                if points[i] in cen:
                    plt.scatter(points[i][0],points[i][1],s=100,c='y',marker='D')
            elif id_c[i]==5:
                plt.scatter(points[i][0],points[i][1],s=40,c='k')
                if points[i] in cen:
                    plt.scatter(points[i][0],points[i][1],s=100,c='k',marker='D')
            elif id_c[i]==6:
                plt.scatter(points[i][0],points[i][1],s=40,c='m')
                if points[i] in cen:
                    plt.scatter(points[i][0],points[i][1],s=100,c='m',marker='D')
            elif id_c[i]==7:
                plt.scatter(points[i][0],points[i][1],s=40,c='0.55')
                if points[i] in cen:
                    plt.scatter(points[i][0],points[i][1],s=100,c='0.55',marker='D')
            elif id_c[i]==8:
                plt.scatter(points[i][0],points[i][1],s=40,c='w')
                if points[i] in cen:
                    plt.scatter(points[i][0],points[i][1],s=100,c='w',marker='D')
            elif id_c[i]==9:
                plt.scatter(points[i][0],points[i][1],s=40,c='0.20')
                if points[i] in cen:
                    plt.scatter(points[i][0],points[i][1],s=100,c='0.20',marker='D')
        plt.show()
        temp_cenp,clusters=new(points,id_c,vehicleCount)
        #print cenp
        cenp=[]
        for i in temp_cenp:
            cenp.append(dic[i][0])
        #print "cenp",cenp

    
    for i in temp_cenp:
        print dic[i]
    # prepare the solution in the specified output format
    outputData = str(obj) + ' ' + str(0) + '\n'
    for v in range(0, vehicleCount):
        outputData += str(depotIndex) + ' ' + ' '.join(map(str,vehicleTours[v])) + ' ' + str(depotIndex) + '\n'

    return outputData

def feasible(clusters,points,centroids):
    
    return

def new(points,id_c,V):
    cluster = []
    centroid = []
    sumx=0
    sumy=0
    for i in range(0,V):
        cluster.append([])
    
    for i in range(0,len(points)):
        cluster[id_c[i]].append(points[i])
    #print "cluster",cluster
    #print "points",points
    for i in cluster :
        sumx=0
        sumy=0
        for j in i:
            sumx+=j[0]
            sumy+=j[1]
        sumx/=len(i)
        sumy/=len(i)
       # print "sum",sumx,sumy
        temp=[]
        for j in range(0,len(i)):
            temp.append((length(i[j],(sumx,sumy)),j))
        centroid.append(i[min(temp)[1]])
    return centroid,cluster

def cluster(points,n,cen):
    #print "len",len(points),points
    centroids=[]
    id_c=[]
    if len(cen)==0:
        for i in range(0,n):
            while(1):
                c=random.randint(0,(len(points)-1))
                if c not in centroids:
                    centroids.append(c)
                    break
    else:
        for i in cen:
            centroids.append(i)
    temp=[]
    c=0
    print "cent",centroids
    #centroids = [45,39,34,50,72,92,93,22,100,94]
    for i in points:
        temp=[]
        #print i
        for j in range(0,len(centroids)):
         #   print "j",j,centroids[j],points[centroids[j]]
            temp.append((length(i,points[centroids[j]]),j))
        #print min(temp)[1]
        id_c.append(min(temp)[1])
    return centroids,id_c

import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        fileLocation = sys.argv[1].strip()
        inputDataFile = open(fileLocation, 'r')
        inputData = ''.join(inputDataFile.readlines())
        inputDataFile.close()
        print 'Solving:', fileLocation
        print solveIt(inputData)
    else:

        print 'This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/vrp_5_4_1)'

