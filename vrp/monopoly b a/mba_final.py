import sys
import csv
import math
import random
import pickle
import numpy
import time
import matplotlib.pyplot as plt
points = []
no_of_clusters = 4
error_high = 3
error_low = 3

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

    #print points
    for k in range(0,5):
        centroids,id_points = cluster(centroids)
        
        ###########   no_of_clusters = # of clusters i.e. 'k' in k means   ####
        ###########    points are just the position values in a list  #######

        #for i in centroids:
        #    cen.append(points[i])
        #print centroids,id_points
        #print "1st point",points[0]
        #print "distance 0", length(points[0],centroids[0]),"dis 1",length(points[0],centroids[1]),"dis 2",length(points[0],centroids[2]),"dis 3",length(points[0],centroids[3])
        #plotting(id_points,centroids)

        centroids = mean(id_points)
        
        ##################      mean() is mean heuristic     ###########
        #print 'cen  ',centroids
      
        #centroids=[]
        #for i in temp_centroids:
        #   centroids.append(dic[(i[0],i[1])][0])
        #print "centroids",centroids
    print "<<<<<<<<<<<<<<<<<<<<<<<  --------*****----------   >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
    print "<<<<<<<<<<<<<<<<<<<<<<<<<<<  result of k-means  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
    print "<<<<<<<<<<<<<<<<<<<<<<<  --------*****----------   >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
    print ""
    print " spaces/distance between the clusters "
    print ""
    print "          1st              2nd                 3rd              4th                 5th               6th"
    print ""
    c=1
    cum_space = 0
    for i in centroids:
        print c,"st  ",
        for j in centroids:
            if i==j:
                print "                  ",
            else:
                print length(i,j),"   ",
                cum_space += length(i,j)
        print ""
        c+=1
    print "\n\n"
    print "--------CUMULATIVE DISTANCE/SPACES BETWEEN THE CENTROIDS----------"
    print "     ",cum_space," units \n\n"
    print " -------ITEMS IN EACH CLUSTERS--------- "
    print "1st       2nd        3rd        4th       5th       6th"
    clusters = make_clusters(id_points)
    for i in clusters:
        print len(i),"       ",
    print "\n\n"
    print("................PRESS ENTER TO CONTINUE.................\n\n")
    a=raw_input()
    while(1):
        size_of_all=[]
        clusters = make_clusters(id_points)
        for i in clusters:
            size_of_all.append(len(i))
        #print size_of_all
        mini = [clusters[numpy.argmin(size_of_all)],min(size_of_all),centroids[numpy.argmin(size_of_all)]]
        maxi = [clusters[numpy.argmax(size_of_all)],max(size_of_all),centroids[numpy.argmax(size_of_all)]]
        av_hold = len(points)/no_of_clusters
        #print "average",av_hold,temp_centroids
        high = av_hold+error_high
        low = av_hold-error_low   
        #print "mini",mini,"maxi",maxi,"hi lo",high,low
        if mini[1]<low and maxi[1]>high:
            #print "insideeeeeeeeeeeeeeeeeeeeee"
            centroids.remove(mini[2])
            while(1):
                c=random.randint(0,(len(maxi[0]))-1)
                if maxi[0][c] not in centroids:
                    temp=maxi[0][c]
                    break
            centroids.append(temp)
            #centroids=[]
            #print temp_centroids
            #for i in temp_centroids:
             #   centroids.append(dic[(i[0],i[1])][0])
            for i in range(0,3):
                centroids,id_points = cluster(centroids)
                #cen=[]
                #for i in centroids:
                 #   cen.append(points[i])
                #plotting(points,id_points,initial,cen)
                #plotting(id_points,centroids)
                centroids = mean(id_points)
                #print centroids
        else:
            print "<<<<<<<<<<<<<<<<<<<<<<<  --------*****----------   >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
            print "<<<<<<<<<<<<<<<<<<<<<<<<<<<  result of Monopoly Breaker Algorithm  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
            print "<<<<<<<<<<<<<<<<<<<<<<<  --------*****----------   >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
            print ""
            print " spaces/distance between the clusters "
            print ""
            print "          1st              2nd                 3rd              4th                 5th               6th"
            print ""
            c=1
            cum_space = 0
            for i in centroids:
                print c,"st  ",
                for j in centroids:
                    if i==j:
                        print "                  ",
                    else:
                        print length(i,j),"   ",
                        cum_space += length(i,j)
                print ""
                c+=1
            print "\n\n"
            print "CUMULATIVE DISTANCE/SPACES BETWEEN THE CENTROIDS:-"
            print "     ",cum_space," units"
            print ""
            print " -------ITEMS IN EACH CLUSTERS--------- "
            print "1st       2nd        3rd        4th       5th       6th"
            clusters = make_clusters(id_points)
            for i in clusters:
                print len(i),"       ",
            print "\n"            
            #plotting(id_points,centroids)
            break

def cluster(old_centroids):
    #print '..............cluster....................'
    size = len(points) - 1
    #print size,no_of_clusters
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
            #print "j",j,i
            temp.append(length(i,j))
        #print min(temp)[1]
        id_points.append(numpy.argmin(temp))
    return old_centroids,id_points


def mean(id_points):
    #print ':::::::::::::  mean  ::::::::::::::::::::'
    #print id_points
    centroid = []
    dic_cen = {}
    clusters = make_clusters(id_points)
    #print "cluster",clusters
    #print "points",len(points[1])
    sum_dim = []
    #print len(points[1])-1
    for i in range(0,len(points[1])):
        sum_dim.append(0)
    for i in clusters :
        #print i
        for k in i:
            #print 'k',k
            for count in range(0,len(points[1])):
                #print count,'   ',sum_dim[count],'         ', k[count]
                sum_dim[count] = sum_dim[count] + k[count]
        #print len(i),i        
        size=len(i)
        for k in range(0,len(sum_dim)):
            if size != 0:
                sum_dim[k]/=size
            else:
                sum_dim[k] = 0
        #print 'sum_dim',sum_dim
        #        print "sum",sumx,sumy
        temp = []
        for j in i:
            temp.append(length(j,sum_dim))
        #print 'temp',temp
        if size != 0:
            centroid.append(i[numpy.argmin(temp)])
        else:
            centroid.append(i)
        #dic_cen[i[min(temp)[1]]] = i
        #print dic_cen
    #print "checking.....",clusters
    #g_clusters = clusters
    #print "global",g_clusters
    return centroid

def make_clusters(id_points):
    clusters = []
    for i in range(0,no_of_clusters):
        clusters.append([])
    
    for i in range(0,len(points)):
        clusters[id_points[i]].append(points[i])

    return clusters
    

def plotting(id_c,cen):
    #print 'yyyyyyyyyyyeeessss',id_c
    for i in range(0,len(points)):
        if id_c[i]==0:
     #       print 'yeah',points[i][0],points[i][1] 
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
        #print x,len(d),d
        if x>0:
            for i in d:
                #print(i)
                nums = i.split(',')
                #print len(nums)
                if len(nums)>1:
                    nums.remove(nums[4])
                    nums = map(float, nums)
                    e.append(nums)
        elif x==-1:
            for i in range(0,len(d)-1):
                line = d[i]
                parts = line.split() 
                e.append((float(parts[0]),float(parts[1])))
                
            #print(nums)
        #print e
        if x==1:
            for i in e:
                i.remove(i[4])
            
        print 'Solving:'   
        print solveIt(e)
    else:

        print 'This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/vrp_5_4_1)'

