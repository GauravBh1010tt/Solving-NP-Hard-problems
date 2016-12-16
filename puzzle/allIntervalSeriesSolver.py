#!/usr/bin/python
# -*- coding: utf-8 -*-

def solveIt(n):
    l=[]
    c = 0 
    l.append(c)
    c=1
    for i in range(1,n):
        if i%2 == 0:
            l.append(c)
            c+=1
        else:
            l.append(n-c)

    outputData = str(n)+'\n'
            
    outputData += ' '.join(map(str, l))+'\n'
    
    return outputData


# this is a depth first search of all assignments
def tryall(assignment, domains):
    # base-case: if the domains list is empty, all values are assigned
    # check if it is a solution, return None if it is not
    if len(domains) == 0:
        if checkIt(assignment):
            return assignment
        else:
            return None
    
    # recursive-case: try each value in the next domain
    # if we find a solution return it. otherwise, try the next value
    else:
        for v in domains[0]:
            sol = tryall(assignment[:]+[v],domains[1:])
            if sol != None:
                return sol


# checks if an assignment is feasible
def checkIt(sol):
    n = len(sol)
    
    items = set(sol)
    if len(items) != n:
        return False
    
    deltas = set([abs(sol[i]-sol[i+1]) for i in range(0,n-1)])
    if len(deltas) != n-1:
        return False
    
    return True


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
        print('This test requires an instance size.  Please select the size of problem to solve. (i.e. python allIntervalSeriesSolver.py 5)')

