import sys
import csv
import math
import random
import pickle
import numpy
import matplotlib.pyplot as plt
dic={}
points = []
no_of_clusters = 4

def length(point1, point2):
    #print 'pts1',point1
    #print 'pts2',point2
    difference = 0
    for i in range(0,len(point1)):
        difference += ((point1[i] - point2[i])**2)
    return math.sqrt(difference)

def solveIt(inputData):

    customerCount = len(inputData)
    #print customerCount
    #no_of_clusters = 4
    for i in inputData:
        points.append(i)
    
    #for i in range(0, customerCount):
     #   dic[(points[i][0],points[i][1])] = i    
    

    #dic={}
   
    centroids=[]
    #length([1,2,1],[2,4,6])
    #bre

    print points
    for k in range(0,3):
        centroids,id_points = cluster(centroids)
        
        ###########   no_of_clusters = # of clusters i.e. 'k' in k means   ####
        ###########    points are just the position values in a list  #######

        #for i in centroids:
        #    cen.append(points[i])
        #print centroids,id_points
        #print "1st point",points[0]
        #print "distance 0", length(points[0],centroids[0]),"dis 1",length(points[0],centroids[1]),"dis 2",length(points[0],centroids[2]),"dis 3",length(points[0],centroids[3])
        #plotting(points,id_points,initial,cen)

        temp_centroids,clusters,dic_cen = mean(id_points)
        
        ##################      mean() is mean heuristic     ###########
      
        centroids=[]
        for i in temp_centroids:
            centroids.append(dic[(i[0],i[1])][0])
        #print "centroids",centroids

    #print dic_cen
    bre
    
    while(1):
        temp=[]
        for i in dic_cen.keys():
            temp.append((len(dic_cen[i]),i))
        mini=min(temp)
        maxi=max(temp)
        av_hold = len(points)/no_of_clusters
        #print "average",av_hold,temp_centroids
        high = av_hold+4
        low = av_hold-4   
        #print "minimax",mini,maxi,high,low,temp_centroids,centroids
        if mini[0]<low and maxi[0]>high:
            temp_centroids.remove(mini[1])
            while(1):
                c=random.randint(0,(len(dic_cen[maxi[1]])-1))
                if c not in centroids:
                    temp=dic_cen[maxi[1]][c]
                    break
            temp_centroids.append(temp)
            centroids=[]
            #print temp_centroids
            for i in temp_centroids:
                centroids.append(dic[(i[0],i[1])][0])
            for i in range(0,3):
                centroids,id_points = cluster(centroids)
                #cen=[]
                #for i in centroids:
                 #   cen.append(points[i])
                #plotting(points,id_points,initial,cen)

                temp_centroids,clusters,dic_cen = mean(id_points)
                #print centroids
                centroids=[]
                for i in temp_centroids:
                    centroids.append(dic[(i[0],i[1])][0])
        else:
            break

def cluster(old_centroids):
    print '..............cluster....................'
    size = len(points) - 1
    print size,no_of_clusters
    #print "len",len(points),points
    #centroids = []
    id_points = []
    if len(old_centroids)==0:
        for i in range(0,no_of_clusters):
            while(1):
                c = random.randint(0,size)
                if c not in old_centroids:
                    old_centroids.append(points[c])
                    break
    #else:
     #   for i in old_centroids:
      #      centroids.append(i)
    #print "cent",old_centroids
    
    #centroids = [45,39,34,50,72,92,93,22,100,94]
    for i in points:
        temp=[]
        #print i
        for j in old_centroids:
         #   print "j",j,centroids[j],points[centroids[j]]
            temp.append(length(i,j))
        #print min(temp)[1]
        id_points.append(numpy.argmin(temp))
    return old_centroids,id_points


def mean(id_points):
    print ':::::::::::::  mean  ::::::::::::::::::::'
    print id_points
    cluster = []
    centroid = []
    dic_cen = {}
    for i in range(0,no_of_clusters):
        cluster.append([])
    
    for i in range(0,len(points)):
        cluster[id_points[i]].append(points[i])
    #print "cluster",cluster[0]
    #print "points",points
    sum_dim = []
    print len(points[1])-1
    for i in range(0,len(points[1])-1):
        sum_dim.append(0)
    for i in cluster :
        print i
        for k in i:
            for count in range(0,len(points[1])-1):
                sum_dim[count] = sum_dim[count] + k[count]
                
        print sum_dim
        #        print "sum",sumx,sumy
        temp = []
        for j in range(0,len(i)):
            temp.append((length(i[j],(sumx,sumy)),j))
        centroid.append(i[min(temp)[1]])
        dic_cen[i[min(temp)[1]]] = i
        #print dic_cen
    return centroid,cluster,dic_cen

if __name__ == '__main__':
    if len(sys.argv) > 1:
        fileLocation = sys.argv[1].strip()
        inputDataFile = open(fileLocation, 'r')
        inputData = ''.join(inputDataFile.readlines())
        inputDataFile.close()
        d=[]
        e=[]

        x= inputData.find(',')
        if x==1:
            for i in inputData.split('\n'):
                d.append(i)

            d.remove(d[len(d)-1])
        else:
            d=inputData.split('\n')
        print x,len(d)
        if x==1:
            for i in d:
                print(i)
                nums = i.split(',')
                nums = map(float, nums)
                e.append(nums)
        elif x==-1:
            for i in range(0,len(d)-1):
                line = d[i]
                parts = line.split() 
                print parts
                nums = map(float,nums)
                
            #print(nums)
        if x==1:
            for i in e:
                i.remove(i[0])
            
        print 'Solving:',e    
        print solveIt(e)
    else:

        print 'This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/vrp_5_4_1)'

