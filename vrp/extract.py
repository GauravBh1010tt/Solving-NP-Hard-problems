import sys
import matplotlib.pyplot as pt

if __name__ == '__main__':
    if len(sys.argv) > 1:
        fileLocation = sys.argv[1].strip()
        inputDataFile = open(fileLocation, 'r')
        inputData = ''.join(inputDataFile.readlines())
        inputDataFile.close()
        e=[]
        f=[]
        x =[]
        y =[]
        
        e=inputData.split('\n');
        
        for i in e:
            p=i.split()
            try:
                f.append((float(p[1]),float(p[2])))
            except:
                continue
        for i in f:
            x.append(i[0])
            y.append(i[1])

        x.remove(x[0])
        y.remove(y[0])
        pt.scatter(x,y,s=10,c='black')
                     
