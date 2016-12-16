#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
dic={}

def solveIt(n):
    # Modify this code to run your puzzle solving algorithm
    
    # define the domains of all the variables (0..n-1)

    sol = []

    for i in range(0,n):
        c=random.randint(0,n-1)
        dic[c,i] = i
        sol.append(-1)

    #dic = {(0,0):0,(2,1):1,(1,2):2,(1,3):3}
    #print dic
    while(1):
        maxi = max_con(n)
        if maxi[0] == 0:
            break
        c = random.randint(0,len(maxi[1])-1) 
        a = dic[maxi[1][c]]
        del dic[maxi[1][c]]
        mini = min_con(a,n)
        c = random.randint(0,len(mini[1])-1)
        dic[mini[1][c]] = mini[1][c][1]
    #print "final",dic

    outputData = str(n) + '\n'

    for key in dic.keys():
        sol[key[1]] = key[0]

    #print sol
    outputData += ' '.join(map(str, sol))+'\n'
    return outputData


# this is a depth first search of all assignments

def max_con(n):
    con = {}
    maxi = [-1,[]]
    for i in dic.keys():
        #print i
        con[i]=0
        if i[0]>0:
            u = i[0]-1
            while(1):
                try:
                    #print "no u",u
                    if u<0:
                        break
                    v = dic[u,i[1]]
                    #print "yes"
                    u-=1
                    con[i]+=1
                except:
                    u-=1
                    continue
        if i[0] < n-1:
            d = i[0] + 1
            while(1):
                try:
                    #print "no d",d
                    if d>n-1:
                        break
                    v = dic[d,i[1]]
                    #print "yes d"
                    con[i]+=1
                    d+=1
                except:
                    d+=1
                    continue

        if i[1] < n-1:
            r = i[1] + 1
            while(1):
                try:
                    #print "no r",r
                    if r>n-1:
                        break
                    v = dic[i[0],r]
                    #print "yes r",r
                    con[i]+=1
                    r+=1
                except:
                    r+=1
                    continue

        if i[1] > 0:
            left = i[1] - 1
            while(1):
                try:
                    #print "no left",left
                    if left < 0:
                        break
                    v = dic[i[0],left]
                    #print "kl"
                    con[i]+=1
                    left-=1
                except:
                    left-=1
            

        if i[1] < n-1:
            urd_x = i[0] - 1
            urd_y = i[1] + 1
            while(1):
                try:
                    if urd_x<0 or urd_y>n-1:
                        break
                    v = dic[urd_x,urd_y]
                    con[i]+=1
                    urd_x -= 1
                    urd_y += 1
                except:
                    urd_x -= 1
                    urd_y += 1
                    continue

        if i[1]>0:
            lrd_x = i[0] + 1
            lrd_y = i[1] - 1
            while(1):
                try:
                    if lrd_y<0 or lrd_x>n-1:
                        break
                    v = dic[lrd_x,lrd_y]
                    con[i]+=1
                    lrd_x += 1
                    lrd_y -= 1
                except:
                    lrd_x += 1
                    lrd_y -= 1
                    continue

        if i[0]>0 and i[1] > 0:
            uld_x = i[0] - 1
            uld_y = i[1] - 1
            while(1):
                try:
                    if uld_x<0 or uld_y<0:
                        break
                    v = dic[uld_x,uld_y]
                    con[i]+=1
                    uld_x -= 1
                    uld_y -= 1
                except:
                    uld_x -= 1
                    uld_y -= 1
                    continue

        if i[0] < n-1 and i[1]>0 :
            lld_x = i[0] + 1
            lld_y = i[1] + 1
            while(1):
                try:
                    if lld_x>n-1 or lld_y>n-1:
                        break
                    v = dic[lld_x,lld_y]
                    con[i]+=1
                    lld_x += 1
                    lld_y += 1
                except:
                    lld_x += 1
                    lld_y += 1
                    continue

        if maxi[0] < con[i]:
            maxi[1] = []
            maxi = [con[i],[i]]
        elif maxi[0] == con[i]:
            maxi[1].append(i)
        
    #print con,maxi
    return maxi



def min_con(pos,n):

    con = {}
    mini =[1000,[]]
    for p in range(0,n):
        i = (p,pos)
        #print i
        con[i] = 0
        if i[0]>0:
            u = i[0]-1
            while(1):
                try:
                    #print "no u",u
                    if u<0:
                        break
                    v = dic[u,i[1]]
                    #print "yes"
                    u-=1
                    con[i]+=1
                except:
                    u-=1
                    continue
        if i[0] < n-1:
            d = i[0] + 1
            while(1):
                try:
                    #print "no d",d
                    if d>n-1:
                        break
                    v = dic[d,i[1]]
                    #print "yes d"
                    con[i]+=1
                    d+=1
                except:
                    d+=1
                    continue

        if i[1] < n-1:
            r = i[1] + 1
            while(1):
                try:
                    #print "no r",r
                    if r>n-1:
                        break
                    v = dic[i[0],r]
                    #print "yes r",r
                    con[i]+=1
                    r+=1
                except:
                    r+=1
                    continue

        if i[1] > 0:
            left = i[1] - 1
            while(1):
                try:
                    #print "no left",left
                    if left < 0:
                        break
                    v = dic[i[0],left]
                    #print "kl"
                    con[i]+=1
                    left-=1
                except:
                    left-=1
            

        if i[1] < n-1:
            urd_x = i[0] - 1
            urd_y = i[1] + 1
            while(1):
                try:
                    if urd_x<0 or urd_y>n-1:
                        break
                    v = dic[urd_x,urd_y]
                    con[i]+=1
                    urd_x -= 1
                    urd_y += 1
                except:
                    urd_x -= 1
                    urd_y += 1
                    continue

        if i[1]>0:
            lrd_x = i[0] + 1
            lrd_y = i[1] - 1
            while(1):
                try:
                    if lrd_y<0 or lrd_x>n-1:
                        break
                    v = dic[lrd_x,lrd_y]
                    con[i]+=1
                    lrd_x += 1
                    lrd_y -= 1
                except:
                    lrd_x += 1
                    lrd_y -= 1
                    continue

        if i[0]>0 and i[1] > 0:
            uld_x = i[0] - 1
            uld_y = i[1] - 1
            while(1):
                try:
                    if uld_x<0 or uld_y<0:
                        break
                    v = dic[uld_x,uld_y]
                    con[i]+=1
                    uld_x -= 1
                    uld_y -= 1
                except:
                    uld_x -= 1
                    uld_y -= 1
                    continue

        if i[0] < n-1 and i[1]>0 :
            lld_x = i[0] + 1
            lld_y = i[1] + 1
            while(1):
                try:
                    if lld_x>n-1 or lld_y>n-1:
                        break
                    v = dic[lld_x,lld_y]
                    con[i]+=1
                    lld_x += 1
                    lld_y += 1
                except:
                    lld_x += 1
                    lld_y += 1
                    continue

        if mini[0] > con[i]:
            mini[1] = []
            mini = [con[i],[i]]
        elif mini[0] == con[i]:
            mini[1].append(i)

    #print con,mini
    return mini


import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            n = int(sys.argv[1].strip())
        except:
            print sys.argv[1].strip(), 'is not an integer'
        print 'Solving Size:', n
        print(solveIt(n))

    else:
        print('This test requires an instance size.  Please select the size of problem to solve. (i.e. python queensSolver.py 8)')

