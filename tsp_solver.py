#!/usr/bin/python
# -*- coding: utf-8 -*-

import math
import pickle
import random
import matplotlib.pyplot as pt

class tsp:
    
    def __init__(self,temp = 1.99998,iteration=5000):
        self.temp = temp
        self.iteration = iteration
        
    def opt2(self,path,temperature):
        new_path = []
        #for i in range(0,len(path)-1):
        i = random.randint(0,len(path)-2)
            
        edge1 = (path[i],path[i+1])
        #new_path.append(path[i])
        #for j in range(i+2,len(path)-1):
        while(1):
            j = random.randint(0,len(path)-2)
            if j!=i and j!=i+1 and j+1!=i and j+1!=i+1:
                #print "i an all",i,i+1,j,j+1
                break
            
        edge2 = (path[j],path[j+1])
    
        if i<j:
            small = i
            big = j
        else:
            small = j
            big = i
        new_path = path[0:small+1]
        #print edge1,edge2
        if self.intersect(edge1[0],edge1[1],edge2[0],edge2[1]):
            #print "crossed"
            temp_path = []
            for k in new_path:
                temp_path.append(k)                
            temp=[]
            for k in path[small+1:big+1]:
                temp.append(k)
            temp.reverse()
            temp_path.extend(temp)                 
            temp_path.extend(path[big+1:])
            #new_path.append(path[len(path)-1])
            path = temp_path
            #ploting(path)
        else:
            #print edge1,edge2
            temp_path = []
            for k in new_path:
                temp_path.append(k)
            temp = []
            for k in path[small+1:big+1]:
                temp.append(k)
            temp.reverse()
            temp_path.extend(temp)
            temp_path.extend(path[big+1:])
            #ploting(temp_path)
            """x = cal_dis(temp_path)
            #temp_path.append(path[len(path)-1])
            if x < cal_dis(path):
                path = temp_path
                #if x < mini:
                    #   mini = x
                    #  min_path = temp_path
            elif coinflip(path,temp_path,temperature):
                    #print "le lea",temperature"""
            path = temp_path
            #ploting(path)
            #print "path",path,i
        #print path,new_path,temp_path
        #new_path.append(path[len(path)-1])            
        return path
    
    def cal_dis(self,path):
        total=0
        for i in range(0,len(path)-1):
            total=total+self.length(path[i],path[i+1])
        return total
            
    def ccw(self,A,B,C):
        return (C[1]-A[1])*(B[0]-A[0]) > (B[1]-A[1])*(C[0]-A[0])
    
    def intersect(self,A,B,C,D):
        #print A,B,C,D
        return self.ccw(A,C,D) != self.ccw(B,C,D) and self.ccw(A,B,C) != self.ccw(A,B,D)
    
    def length(self,point1, point2):
        return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)
    
    def ploting(self,d):
        x=[]
        y=[]
        for k in d:
         	x.append(k[0])
         	y.append(k[1])
        pt.plot(x,y)
        pt.axis([min(x)-2,max(x)+2,min(y)-2,max(y)+2])
        pt.show()
    
    def coinflip(self,path,new_path,t):
        #print t, cal_dis(new_path), cal_dis(path)
        #print t
        p = math.exp(-(self.cal_dis(new_path) - self.cal_dis(path)) / t)
        u = random.random()
        if u < p:
            return True
        else:
            return False
    
    def sim_annealing(self,path,temp = 1.99998,iteration=5000):
        mini = self.cal_dis(path)
        min_path = path
        for i in range(0,iteration):
            temp_path = self.opt2(path,temp)
            #temp_path=p[0]
            #print temp,i
            #ploting(temp_path)
            x = self.cal_dis(temp_path)
            if x < self.cal_dis(path):
                path = temp_path
                if x < mini:
                    #print "min",x
                    mini = x
                    min_path = temp_path
            elif self.coinflip(path,temp_path,temp):
                path = temp_path
            temp = 0.9997 * temp
        return min_path
    
    def run(self,i):
        self.ploting(i)
        d=self.sim_annealing(i,self.temp,self.iteration)
        self.ploting(d)
        return self.cal_dis(d),d

