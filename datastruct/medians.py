'''

'''

from heapq import *

#if need be we rebalance the heaps so they are close to even
def balance(minheap,maxheap):
    diff=len(minheap)-len(maxheap)
    #if minheap is two elements or more larger than max heap
    #pluck out its max value and push it in minheap
    if diff >=2:
        heappush(maxheap,-heappop(minheap))
        return (minheap,maxheap)
    #if maxheap is two elements or more larger than minheap
    #pluck out its min value and push it in maxheap
    elif diff <=-2: 
        heappush(minheap,-heappop(maxheap))
        return (minheap,maxheap)
    else:
        return (minheap,maxheap)

def pushnext(minheap,maxheap,new):
	#figure our if the new element should go to the max heap or min heap
    low=-minheap[0]
    high=maxheap[0]
    if new >= low:
        return 'append maxheap'
    else:
        return 'append minheap'

def sumMedMod(filename):
	with open(filename) as f:
		intlist=f.readlines()
	intlist=[int(i.strip()) for i in intlist]

    #initialize first elements in minheap and maxheap
	minheap=[]
	maxheap=[]
	medians=[]

	#no matter what the first element is the first we see so it must be a 'median'
	medians.append(intlist[0])

	#if the second element is smaller, it will be median acording to our scheme
	if intlist[0] > intlist[1]:
		heappush(maxheap,intlist[0])
		heappush(minheap,-intlist[1])
		medians.append(intlist[1])
	#other wise the second median is the first element again
	else:
		heappush(maxheap,intlist[1])
		heappush(minheap,-intlist[0])
		medians.append(intlist[0])

	#now loop over the rest of the elements
	for i in xrange(2,len(intlist)):
		#grab the next element. we're pretending to recieve these as a 'stream'
		new=intlist[i]

		#determine which heap it should go to
		whosnext=pushnext(minheap,maxheap,new)
		if whosnext == 'append maxheap':
			heappush(maxheap,new)
		else:
			heappush(minheap,-new)

		#balance the heaps if need be
		minheap,maxheap=balance(minheap,maxheap)

		#figure out where the median is now
		#if its the kth median, k...n
		#if the heaps are even, its the max in the min list
		#if the min heap is one bigger, it is still the max in the min list
		#otherwise if the max heap is bigger, its the min element in the max heap
		lenminheap=len(minheap)
		lenmaxheap=len(maxheap)
		if lenminheap == lenmaxheap or lenminheap > lenmaxheap:
			#print "k = %s minheap = %s maxheap = %s median = %s" %(i+1,minheap,maxheap,-minheap[0])
			medians.append(-minheap[0])
		else:
			#print "k = %s minheap = %s maxheap = %s median = %s" %(i+1,minheap,maxheap,maxheap[0])
			medians.append(maxheap[0])
	#we're asked to return the sum modulo 10000
	return sum(medians)%10000