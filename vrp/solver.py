#!/usr/bin/python
# -*- coding: utf-8 -*-

import math
import random
import pickle
import matplotlib.pyplot as plt
dic={}
capacity=0
#dic_cen={}

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

    capacity = vehicleCapacity

    customers = []
    for i in range(1, customerCount+1):
        line = lines[i]
        parts = line.split()
        d=(int(parts[0]), float(parts[1]),float(parts[2]))
        customers.append(d)
        points.append((d[1],d[2]))
        dic[(d[1],d[2])] = (i-2,d[0])


    vehicleTours = []

    customerIndexs = set(range(1, customerCount))  # start at 1 to remove depot index
    #print customers
    
    initial = points[0]
    points = points[1:]

    #print id_c
    cenp=[]
    #plt.scatter(initial[0],initial[1],s=500,c='0',marker='*')
    #for i in range(0,len(points)):
     #   plt.scatter(points[i][0],points[i][1],s=40,c='b')
   # plt.show()
    #bre

    for k in range(0,3):
        cen=[]
        cenp,id_c = cluster(points,vehicleCount,cenp)
        
        ###########   vehicleCount = # of clusters i.e. 'k' in k means   ####
        ###########    points are just the position values in list  #######

        for i in cenp:
            cen.append(points[i])
        print points,vehicleCount
        plotting(points,id_c,initial,cen)

        temp_cenp,clusters,dic_cen=new(points,id_c,vehicleCount)
        
        ################## new() is mean heuristic     ###########
      
        cenp=[]
        for i in temp_cenp:
            cenp.append(dic[i][0])
        #print "cenp",cenp

    #print dic_cen
  
    
    while(1):
        temp=[]
        for i in dic_cen.keys():
            temp.append((len(dic_cen[i]),i))
        mini=min(temp)
        maxi=max(temp)
        av_hold = len(points)/vehicleCount
        #print "average",av_hold,temp_cenp
        high = av_hold+4
        low = av_hold-4
        #print "minimax",mini,maxi,high,low,temp_cenp,cenp
        if mini[0]<low and maxi[0]>high:
            temp_cenp.remove(mini[1])
            while(1):
                c=random.randint(0,(len(dic_cen[maxi[1]])-1))
                if c not in cenp:
                    temp=dic_cen[maxi[1]][c]
                    break
            temp_cenp.append(temp)
            cenp=[]
            #print temp_cenp
            for i in temp_cenp:
                cenp.append(dic[i][0])
            for i in range(0,3):
                cenp,id_c = cluster(points,vehicleCount,cenp)
                cen=[]
                for i in cenp:
                    cen.append(points[i])
                plotting(points,id_c,initial,cen)

                temp_cenp,clusters,dic_cen=new(points,id_c,vehicleCount)
                #print cenp
                cenp=[]
                for i in temp_cenp:
                    cenp.append(dic[i][0])
        else:
            break
    #a,b = is_all_feasible(dic_cen,vehicleCapacity)
    print "........cen........"
    #print dic_cen.keys()
    #print "....chk....",orien(dic_cen.keys()[0],initial,dic_cen.keys())
    dic_cen = feasible(dic_cen,vehicleCapacity,initial)
    #a,b = is_all_feasible(dic_cen,vehicleCapacity)
    #print "........new cen........",a,b
    path,obj = tsp(dic_cen,initial)
    print "||||tsp|||",path

    new_path = []
    #print path
    #path = [[(30.0, 40.0), (20.0, 26.0), (5.0, 25.0), (12.0, 42.0), (17.0, 63.0), (21.0, 47.0), (30.0, 40.0)],[(30.0, 40.0), (37.0, 52.0), (31.0, 62.0), (52.0, 64.0), (49.0, 49.0), (52.0, 33.0), (30.0, 40.0)],[(30.0, 40.0), (31.0, 32.0), (36.0, 16.0), (51.0, 21.0), (40.0, 30.0), (42.0, 41.0), (30.0, 40.0)]]
        
    obj = 0    
    for i in path:
        #print i
        temp_new_path = []
        for j in range(1,len(i)-1):
            temp_new_path.append(dic[i[j]][0]+1)
        obj+=cal_dis(i)
        new_path.append(temp_new_path)

    mini_x=0
    maxi_x=0
    mini_y=0
    maxi_y=0
    for i in path:
        x=[]
        y=[]
        for j in i:
            x.append(j[0])
            y.append(j[1])
        plt.plot(x,y)
        #print x,y
        if mini_x>min(x):
            mini_x = min(x)
        if maxi_x<max(x):
            maxi_x = max(x)
        if mini_y>min(y):
            mini_y=min(y)
        if maxi_y<max(y):
            maxi_y=max(y)
    plt.axis([mini_x-2,maxi_x+2,mini_y-2,maxi_y+4])
    plt.show()
   # print path

    with open("vrp_16.txt","wb") as handle:
        pickle.dump(path,handle)

    #obj = cal_dis(path)
    
    # prepare the solution in the specified output format
    outputData = str(obj) + ' ' + str(0) + '\n'
    
    for v in new_path:
        outputData += str(0) + ' ' + ' '.join(map(str,v)) + ' ' + str(0) + '\n'

    return outputData


def tsp(dic_cen,initial):
    path = []
    total = 0
    for i in dic_cen.keys():
        points = dic_cen[i]
        point = initial
        closed = []
        temp_path=[]
        temp_path.append(initial)
        while(1):
            dis=[]
            closed.append(point)
            for i in points:
                if i not in closed:
                    dis.append((length(point,i),i))
                else:
                    dis.append(('',i))
            x = min(dis)
            if x[0]!='':
                total+=x[0]
                temp_path.append(x[1])
                point = x[1]
            else:
                temp_path.append(initial)
                chk=opt2(temp_path)
                #chk[0].append(initial)
                while(1):
                    #print "yes"
                    if chk[1] == False:
                        break
                    else:
                        chk=opt2(chk[0])
               # print "made",chk[0]
                #chk[0].append(initial)
                path.append(chk[0])
                break
    return path,total

def opt2(path):
    #print "in opt2",path
    temp = []
    new_path = []
    for i in range(0,len(path)-1):
        edge1 = (path[i],path[i+1])
        new_path.append(path[i])
        for j in range(i+2,len(path)-1):
            edge2 = (path[j],path[j+1])
            if edge1[0]==path[0] and edge2[1]==path[0]:
                continue
            else:
                if intersect(edge1[0],edge1[1],edge2[0],edge2[1]):
                    #print "....block...."
                    temp=[]
                    for k in path[i+1:j+1]:
                        temp.append(k)
                    temp.reverse()
                    new_path.extend(temp)
                    new_path.extend(path[j+1:])
                    return new_path,True
    new_path.append(path[len(path)-1])
    return new_path,False

def cal_dis(path):
    total=0
    for i in range(0,len(path)-1):
        total=total+length(path[i],path[i+1])
    return total
        
def ccw(A,B,C):
    return (C[1]-A[1])*(B[0]-A[0]) > (B[1]-A[1])*(C[0]-A[0])

def intersect(A,B,C,D):
    #print A,B,C,D
    return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)
    


def feasible(dic_cen,cap,initial):
    while(1):
        feasible,label = is_all_feasible(dic_cen,cap)
        if label == True:
            return dic_cen
        for i in dic_cen.keys():
            if feasible[i][0] == False:
                #for j in dic_cen.keys():
                 #   if i != j:
                #print i
                o=orien(i,initial,dic_cen.keys())
                o.sort()
                o.reverse()
                for k in o:
                    x = dic_cen.keys()[k[1]]
                    #print "k is",k,"x is",x
                    if feasible[x][0] == True and feasible[x][1] > 0:
                     #   print "feasible",x
                        temp=[]
                        for y in dic_cen[i]:
                            temp.append((dic[y][1],y))
                        temp.sort()
                        temp.reverse()
                      #  print "demand",temp
                        mini = min(temp)[0]
                        for l in temp:
                            if l[0] <= feasible[x][1]:
                       #         print "alter",l
                                feasible[x][1] -= l[0]
                                dic_cen[i].remove(l[1])
                                dic_cen[x].append(l[1])
                            if feasible[x][1] < mini:
                                break
                        feasible,label=is_all_feasible(dic_cen,cap)
                        if label == True:
                            return dic_cen
                        if feasible[i][0] == True:
                            break


def orien(current,initial,others):
    temp=[]
    #print others
    f=0
    for i in others:
        if  i != current:
            #print i,current,initial
            a=length(current,initial)
            b=length(i,initial)
            c=length(current,i)
            d=math.acos((a*a + b*b - c*c) / (2*a*b))
            temp.append((d,f))
        else:
            temp.append((0,f))
        f+=1
    return temp

def is_all_feasible(dic_cen,capacity):
    #print dic_cen
    chk=True
    feasible={}
    for i in dic_cen.keys():
        #print i,capacity
        temp=0
        for j in dic_cen[i]:
            #print j,dic[j]
            temp+=dic[j][1]
        if temp > capacity:
            chk=False
            feasible[i]=[False,temp-capacity]
        else:
            feasible[i]=[True,capacity-temp]
    return feasible,chk
    

def plotting(points,id_c,initial,cen):
    #plt.scatter(initial[0],initial[1],s=500,c='0',marker='*')
    for i in range(0,len(points)):
        #plt.scatter(points[i][0],points[i][1],s=40,c='r')
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
        elif id_c[i]==10:
            plt.scatter(points[i][0],points[i][1],s=40,c=(0,0.2,0))
            if points[i] in cen:
                plt.scatter(points[i][0],points[i][1],s=100,c=(0,0.2,0),marker='D')
        elif id_c[i]==11:
            plt.scatter(points[i][0],points[i][1],s=40,c=(0,0.2,0.2))
            if points[i] in cen:
                plt.scatter(points[i][0],points[i][1],s=100,c=(0,0.2,0.2),marker='D')
        elif id_c[i]==12:
            plt.scatter(points[i][0],points[i][1],s=40,c=(1,0.2,1))
            if points[i] in cen:
                plt.scatter(points[i][0],points[i][1],s=100,c=(1,0.2,1),marker='D')
        elif id_c[i]==13:
            plt.scatter(points[i][0],points[i][1],s=40,c=(0.4,0,1))
            if points[i] in cen:
                plt.scatter(points[i][0],points[i][1],s=100,c=(0.4,0,1),marker='D')
        elif id_c[i]==14:
            plt.scatter(points[i][0],points[i][1],s=40,c=(0,0.8,0.6))
            if points[i] in cen:
                plt.scatter(points[i][0],points[i][1],s=100,c=(0,0.8,0.6),marker='D')
        elif id_c[i]==15:
            plt.scatter(points[i][0],points[i][1],s=40,c=(0.3,0.3,0.9))
            if points[i] in cen:
                plt.scatter(points[i][0],points[i][1],s=100,c=(0.3,0.3,0.9),marker='D')
        elif id_c[i]==16:
            plt.scatter(points[i][0],points[i][1],s=40,c=(1,0.9,0.5))
            if points[i] in cen:
                plt.scatter(points[i][0],points[i][1],s=100,c=(1,0.9,0.5),marker='D')
        elif id_c[i]==17:
            plt.scatter(points[i][0],points[i][1],s=40,c=(0.7,0.3,0.4))
            if points[i] in cen:
                plt.scatter(points[i][0],points[i][1],s=100,c=(0.7,0.3,0.4),marker='D')
        elif id_c[i]==18:
            plt.scatter(points[i][0],points[i][1],s=40,c=(0.2,0.2,0.7))
            if points[i] in cen:
                plt.scatter(points[i][0],points[i][1],s=100,c=(0.2,0.2,0.7),marker='D')
        elif id_c[i]==19:
            plt.scatter(points[i][0],points[i][1],s=40,c=(0.5,0.5,0.1))
            if points[i] in cen:
                plt.scatter(points[i][0],points[i][1],s=100,c=(0.5,0.5,0.1),marker='D')
    plt.show()    


def new(points,id_c,V):
    cluster = []
    centroid = []
    dic_cen={}
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
       #print "sum",sumx,sumy
        temp=[]
        for j in range(0,len(i)):
            temp.append((length(i[j],(sumx,sumy)),j))
        centroid.append(i[min(temp)[1]])
        dic_cen[i[min(temp)[1]]] = i
        #print dic_cen
    return centroid,cluster,dic_cen

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
    #print "cent",centroids
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

