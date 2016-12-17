#!/usr/bin/python
# -*- coding: utf-8 -*-
import util
var={}
edges = []

def solveIt(inputData):
    lines = inputData.split('\n')

    firstLine = lines[0].split()
    nodeCount = int(firstLine[0])
    edgeCount = int(firstLine[1])

    for i in range(1, edgeCount + 1):
        line = lines[i]
        parts = line.split()
        edges.append((int(parts[0]), int(parts[1])))

    for i in range(0,nodeCount):
        #var[i]=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,73,75,76,77,78,79,80,81,82,83,84,85]
        #var[i] =[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,73,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150]
        var[i]=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,73,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]
    taken=[]
    closed=[]
    fringe=util.Stack()
    #fringe.push((0,0))
    var[0]=[0]
    closed.append(0)
    lcv=[]
    
    while(1):
        #print "pre",var
        con=arc()
        chk=False
        for i in var.itervalues():
            #print i
            if len(i)>1 or i==[]:
                chk=True
                break
        if chk == False:
            break
        
        #print "con", con, var
        mini=[0,101]
            
        #if node[0] == nodeCount - 1:
         #   end = True
        if con[0]==True:
            for i in range(0,nodeCount):
                if len(var[i])<mini[1] and len(var[i])>1:
                    mini=[i,len(var[i])]
            #print "min", mini,var[mini[0]]
            lcv=[]
            for i in range(0,len(var[mini[0]])):
                #print mini,var[mini[0]],var[mini[0]][i]
                var[mini[0]] = [var[mini[0]][i]]
                lcv.append((arc()[1],i))
                #print "chk",var
                for i in var.iterkeys():
                    if i in closed:
                        continue
                    else:
                        #var[i] = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,72,73,73,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150]
                        var[i]=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,73,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]
                d=arc()
            #print lcv
            #node = (mini[0],var[mini[0]][0])
            node=(mini[0],var[mini[0]][min(lcv)[1]])
            temp=var[mini[0]]
            temp.remove(var[mini[0]][min(lcv)[1]])
            for i in temp:
                fringe.push((node[0],i))
        #print var,mini
        else:
            closed.remove(node[0])
            node = fringe.pop()
        var[node[0]] = [node[1]]
        closed.append(node[0])

        for i in var.iterkeys():
            if i in closed:
                continue
            else:
                #var[i] = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,72,73,73,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150]
                var[i]=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,73,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]
        #print "node",node
        
        #print "succ", successors,fringe.list

    # prepare the solution in the specified output format
    for i in range(0,nodeCount):
        taken.append(var[i][0])
        
    outputData = str(max(taken)+1) + ' ' + str(0) + '\n'
    outputData += ' '.join(map(str, taken))

    return outputData

def check(node,col):
    chk=True
    #print "node",node,col,var
    
    for i in edges:
        if i[0] == node:
            #print type(var[i[1]])
            if col in var[i[1]]:
                var[i[1]].remove(col)
        #print var
    #return chk

def arc():
    val=0
    while(1):
        chk=False
        #print var
        for i in edges:
            #print var[i[0]]
            if len(var[i[0]])>1 and len(var[i[1]])>1:
                continue
            elif len(var[i[0]]) == 1 or len(var[i[1]]) == 1:
                if len(var[i[0]]) == 1:
                    if var[i[0]][0] in var[i[1]]:
                        var[i[1]].remove(var[i[0]][0])
                        val=val+1
                        chk=True
                if len(var[i[1]]) == 1:
                    if var[i[1]][0] in var[i[0]]:
                        var[i[0]].remove(var[i[1]][0])
                        val=val+1
                        chk=True
            if len(var[i[0]]) == 0 or len(var[i[1]]) == 0:
                return False,val
            
        if chk == False:
            return True,val
        #val=0
    
def out(edges,ofile):
    f=open(ofile,'w')
    f.write('graph{\n')
    for e in edges:
        f.write('  ' + str(e[0]) + ' -- ' + str(e[1]) + '\n')
    f.write('}\n')

import sys
if __name__ == '__main__':
    if len(sys.argv) > 1:
        fileLocation = sys.argv[1].strip()
        inputDataFile = open(fileLocation, 'r')
        inputData = ''.join(inputDataFile.readlines())
        inputDataFile.close()
        print solveIt(inputData)
    else:
        print 'This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/gc_4_1)'

