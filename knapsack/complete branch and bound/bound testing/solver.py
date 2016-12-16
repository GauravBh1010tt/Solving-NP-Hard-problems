import util
def solveIt(inputData):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = inputData.split('\n')

    firstLine = lines[0].split()
    items = int(firstLine[0])
    capacity = int(firstLine[1])

    values = []
    weights = []
	
    for i in range(1, items+1):
        line = lines[i]
        parts = line.split()

        values.append(int(parts[0]))
        weights.append(int(parts[1]))

    # a trivial greedy algorithm for filling the knapsack
    # it takes items in-order until the knapsack is full
    estimate = 0
    for i in values:
        estimate=estimate+i
    taken = []
    items = len(values)

    cur_estimate=0
    fringe=util.Stack()# creating stack
    
    dic={} # dic will help to store each node status, so as to trace back    
    fringe.push((0,capacity,estimate,0)) #pushing the 1st node
    #print values, weights
    #print capacity,estimate
    while (1):
        if fringe.isEmpty() == True : # when all nodes are consumed
            while(1): # tracing back the path
                if(parent == (0,capacity,estimate,0)):# when the start state is reached
                    break
                taken.append(dic[parent][0])
                parent = dic[parent][1]
                #print taken
            taken.reverse()# getting path in correct order
            outputData = str(cur_estimate) + ' ' + str(0) + '\n'
            outputData += ' '.join(map(str, taken))
            return outputData
        #if node not in closed:
        successors=[]
        node=fringe.pop()
        take=False
        end=False
        #closed.add(node)
        #print node
        if node[3] == items:
            end = True
        elif (node[1]-weights[node[3]]) >= 0:
            take = True
        if end==False and take == True :
            successors.append((values[node[3]]+node[0],node[1]-weights[node[3]],node[2],node[3]+1))
            #cur_estimate = node[2] - value[node[3]]
            #parent = successor[0]
        if end == False and take == True and node[2]>cur_estimate :
            successors.append((node[0],node[1],node[2]-values[node[3]],node[3]+1))
        elif end == False and take == False and node[2]>cur_estimate :
            successors.append((node[0],node[1],node[2]-values[node[3]],node[3]+1))

        if end == True and cur_estimate < node[0]:
            cur_estimate = node[0]
            parent = node
            #print "es",cur_estimate, parent
            
        successors.reverse()
        for child in successors:
        #if child[0] not in closed:
            #print child, node,
            if node[2] == child[2]:
                dic[child]=(1,node)
            else:
                dic[child]=(0,node)
            fringe.push(child)            

    # prepare the solution in the specified output format


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

