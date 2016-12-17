import util
ratio=[]
values = []
weights = []
	
def solveIt(inputData):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = inputData.split('\n')

    firstLine = lines[0].split()
    items = int(firstLine[0])
    capacity = int(firstLine[1])

    #Capacity = capacity
    #print "chk",Capacity, capacity

    for i in range(1, items+1):
        line = lines[i]
        parts = line.split()

        values.append(int(parts[0]))
        weights.append(int(parts[1]))

    # a trivial greedy algorithm for filling the knapsack
    # it takes items in-order until the knapsack is full
    estimate = 0
    chk=0
    #for i in values:  #loose bound
    #    estimate=estimate+i

    #ratio = []
    items = len(values)

    for i in range(0,items):
        ratio.append((float(values[i])/float(weights[i]),i))

    ratio.sort()
    ratio.reverse()

    #print ratio
    
    for i in ratio:
        if (chk+weights[i[1]]) <= capacity:
            estimate = estimate + values[i[1]]
            chk=chk+weights[i[1]]
        else:
            estimate = estimate + i[0]*(capacity-chk)
            break

    #print estimate
    
    taken1=[]
    taken=[]
    cur_estimate=0
    fringe=util.Stack()# creating stack

    
    fringe.push((0,capacity,estimate,0,-2)) #pushing the 1st node
    #print values, weights
    #print capacity,estimate
    while (1):
        if fringe.isEmpty() == True : # when all nodes are consumed
            break
        
        #if node not in closed:
        successors=[]
        node=fringe.pop()
        if node[4]>-1:
            #print taken1
            if cur_estimate>0:
                taken1 = taken1[0:node[3]-1]
                taken1.append(node[4])
                #print "no",taken1
            else:
                #print "yes",taken1
                taken1.append(node[4])
        estimate  = calc_estimate(taken1,capacity)
        #print estimate,cur_estimate,taken1,node
        
        #print node[4]
            #else:
        take=False
        end=False
        chk=0
        #print node
        if node[3] == items:
            end = True
        elif (node[1]-weights[ratio[node[3]][1]]) >= 0:
            take = True
        if end==False and take == True and node[2]>cur_estimate :
            successors.append([values[ratio[node[3]][1]]+node[0],node[1]-weights[ratio[node[3]][1]],node[2],node[3]+1, 1])
            #taken.append(1)
            #print "yes",successors
        if end == False and take == True and node[2]>cur_estimate :
            #print "no"
            #node[2]  = calc_estimate(taken1,capacity)
            successors.append([node[0],node[1],estimate,node[3]+1,0])
            #print "no",successors[1]
        elif end == False and take == False and node[2]>cur_estimate :
            #node[2]  = calc_estimate(taken1,capacity)
            successors.append([node[0],node[1],estimate,node[3]+1,0])
            #print "no",successors[0]
            #taken.append(0)

        if cur_estimate <= node[0]:
            cur_estimate = node[0]
            #print "taken1",taken1
            taken = []
            for i in taken1:
                taken.append(i)
            #taken1 = []
            #parent = (node[0],node[1],node[2])
            #print "es",cur_estimate, parent
            
        successors.reverse()
        #print "yes",node[3]
        for child in successors:
            fringe.push(child)
    temp_taken=[]
    for i in range(0,items):
        temp_taken.append(0)
    for i in range(0,len(taken)):
        if taken[i] == 1:
            temp_taken[ratio[i][1]]=1
        
    #for i in range(len(taken),len(values)):
     #   taken.append(0)
        
    outputData = str(cur_estimate) + ' ' + str(0) + '\n'
    outputData += ' '.join(map(str, temp_taken))
    #print "rex hi",cur_estimate
    return outputData
    # prepare the solution in the specified output format

def calc_estimate(taken1,Capacity):
    taken=[]
    for i in taken1:
        taken.append(i)
    taken.append(0)
    estimate = 0
    chk=0
    c=0
    #print taken
    for i in ratio:
        if c < len(taken):
            #print "in taken",weights[ratio[i][1]], ratio[i][1], Capacity
            if taken[c] == 1:
                if (chk+weights[i[1]]) <= Capacity:
                    estimate = estimate + values[i[1]]
                    chk=chk+weights[i[1]]
                else:
                    estimate = estimate + i[0]*(Capacity-chk)
                    break
            c=c+1
        else:
            if (chk+weights[i[1]]) <= Capacity:
                estimate = estimate + values[i[1]]
                chk=chk+weights[i[1]]
            else:
                estimate = estimate + i[0]*(Capacity-chk)
                break
    #print "es", estimate
    return estimate

import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        fileLocation = sys.argv[1].strip()
        inputDataFile = open(fileLocation, 'r')
        inputData = ''.join(inputDataFile.readlines())
        inputDataFile.close()
        print solveIt(inputData)
    else:
        print 'This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)'

