#!/usr/bin/python
# -*- coding: utf-8 -*-
import util
var={}
edges = []

def solveIt(inputData):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = inputData.split('\n')

    firstLine = lines[0].split()
    nodeCount = int(firstLine[0])
    edgeCount = int(firstLine[1])

    for i in range(1, edgeCount + 1):
        line = lines[i]
        parts = line.split()
        edges.append((int(parts[0]), int(parts[1])))

    d = [0,1,2,3]
    color = ''
    neigh=[]
    #var={}

    out(edges,"./graph")
    
    """for i in edges:
        if         """
    #print edges
    for i in range(0,nodeCount):
        var[i]=[0,1,2,3,4]
    taken=[]
    fringe=util.Stack()
    fringe.push((0,0))
    maxi=0
    
    while(1):
        chk=False
        successors = []
        node = fringe.pop()
        #print "pop",node
        end= False

        domain = []
        domain.append(node[1])
        var[node[0]] = domain
        #print var

        if maxi<node[0]:
            maxi=node[0]

        for i in range(node[0]+1,maxi+1):
            var[i]=[0,1,2,3,4]

        taken = taken[0:node[0]]
        taken.append(node[1])

        check(node[0],node[1])
            
        if node[0] == nodeCount - 1:
            end = True
        if end == False:
            for i in var[node[0]+1]:
                #if check(node[0]+1,i) == True:
                #print "yes",var[node[0]+1],i
                successors.append((node[0]+1,i))
                #else:
                    #print "no",node,node[0]+1,i
        if end==True:
            #print "end",node,taken,successors,fringe.list
            break
        #if len(taken)>16:
         #   bre
        
        successors.reverse()
        #print taken

        for child in successors:
            fringe.push(child)
        #print successors,fringe.list
    #solution = range(0, nodeCount)
    #print type(taken),type(solution)
    # prepare the solution in the specified output format
    outputData = str(22) + ' ' + str(0) + '\n'
    outputData += ' '.join(map(str, taken))

    return outputData

def check(node,col):
    chk=True
    #print "node",node,col,var
    
    for i in edges:
        #print i
        #print "yes"
        #if (var[i[0]][0] !='' or var[i[1]][0] != '') and (i[0]==node or i[1]==node):
            #print "yes",i,node,col
        if i[0] == node:
            #print type(var[i[1]])
            if col in var[i[1]]:
                var[i[1]].remove(col)
        #print var
    #return chk


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

