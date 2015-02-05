import numpy as np
import math

def divide(intarray):
	size=len(intarray)
	#chop array into two
	if size == 1:
		return intarray
	else:
		if size%2==0:
			a=intarray[:size/2]
			b=intarray[size/2:]
		else:
			a=intarray[:(size+1)/2]
			b=intarray[(size+1)/2:]
		return [a,b]

def merge(twohalves,c,k):

	if len(twohalves) > 1:
		a=twohalves[0]
		b=twohalves[1]
		size=len(c)
		i, j = 0, 0
		sizei=len(a)
		sizej=len(b)

		for z in range(k,size):
			if i < sizei and j < sizej:
				if a[i] < b[j]:
					c[z]=a[i]
					i+=1
				else:
					c[z]=b[j]
					j+=1
				print("a= "+str(a)+" and b= "+str(b)+"i="+str(i)+" and j="+str(j)+" and c="+str(c))
			else:
				print("one is too big")
				if i >= sizei:
					print("a is depleted")
					intarray=b[j:]
					twohalves=divide(intarray)
					if len(twohalves) > 1:
						print("calling merge again")
						return merge(twohalves,c,z)
					else:
						c[z]=twohalves[0]
						return c
				else:
					print("b is depleted")
					intarray=a[i:]
					twohalves=divide(intarray)
					if len(twohalves) > 1:
						print("calling merge again")
						return merge(twohalves,c,z)
					else:
						c[z]=twohalves[0]
						return c
		#print ('loop finished')
		return c

	else:
		#print('recieved one number')
		c[k]=twohalves[0]
		print (c)
		return c

def mergeSort(intarray):
	twohalves=divide(intarray)
	c=np.zeros(len(intarray))
	k=0
	c=merge(twohalves,c,k)
	return c
