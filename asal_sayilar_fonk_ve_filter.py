def asal_mi(x):
    i =2
    if (x==1):
        return False
    elif (x==2):
        return True
    else:
        while(i<x):
            if (x%i==0):
                return False
            i=i+1
        return True

list(filter(asal_mi,range(1.100)))#1den 100 e kadar olan asal sayılar
