def fun(inputData):
    #a=''.join(inputData.readlines())
    e=inputData.split('\n')
    for i in e:
        p=i.split()
        try:
            f.append((float(p[1]),float(p[2])))
        except:
            continue
    for i in f:
        #print(i)
        try:
            x.append(i[0])
            y.append(i[1])
        except:
            continue

    x.remove(x[0])
    y.remove(y[0])
    pt.scatter(x,y,s=10,c='black')
                     
