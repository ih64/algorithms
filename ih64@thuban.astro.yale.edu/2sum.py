import numpy as np

array=np.loadtxt('2sum.txt')
#sort the array
array.sort()

#keep unique values only
uniqarray=np.unique(array).tolist()
#store the uniqe sums in a hash table
uniqsum={}

for j in xrange(0,len(uniqarray)):
    if j%10000==0:
        print j
    x=uniqarray[j]
    ymax= 10000-x
    ymin=-10000-x
    #print(" x is "+str(x))
    i=len(uniqarray)-1
    #print(i)
    y=uniqarray[i]
    while y >= ymin:
        #print(" x ="+str(x)+" y="+str(y)+" ymax ="+str(ymax)+" ymin is "+str(ymin))
        #if highpoint's element is too big, move it over left one
        if y > ymax:
            i-=1
            #print "if tripped"
        else:
            uniqsum[x+y]=1
            i-=1
        y=uniqarray[i]
