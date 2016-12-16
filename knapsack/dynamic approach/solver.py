
def solveIt(inputData):
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

    value = 0
    weight = 0
    taken = []
    dic={}
    values.insert(0,0)
    weights.insert(0,0)
    items = len(values)
    
    for i in range(0,capacity+1):
        dic[0,i]=0

    for i in range(1, items):
        for j in range(0, capacity+1):
            if weights[i] > j:
                if weights[i-1] <= capacity:
                    dic[i,j] = dic[i-1,j]
            else:
                dic[i,j] = max(dic[i-1,j], values[i] + dic[i-1,j-weights[i]])

    value = dic[items-1,capacity]
    i=items-1
    j=capacity
    while(i!=0):
        if dic[i-1,j] == dic[i,j]:
            i=i-1
            taken.append(0)
        else:
            taken.append(1)
            j=j-weights[i]
            i=i-1
    taken.reverse()

    # prepare the solution in the specified output format
    outputData = str(value) + ' ' + str(0) + '\n'
    outputData += ' '.join(map(str, taken))
    return outputData

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
