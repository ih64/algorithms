'''
quick sort algorightm to, sorts an array A of length r given starting index l
also counts the number of comparisons between the pivot element and other elements
you can choose the pivot one of three ways: by using the left most element, 
the right most element, or the median of the left, right, and center elements
when you run this on the command line, make sure you initialize quicksort.m=0
this way the command line enviornment will know how to talk to the quicksort 
module enviornment, and keep track of m as the algorightm recurses
'''
import numpy as np

def qs(A,l,r,pselect):
	global m
	if (r-l)<=1:
		return
	else:
		part=partition(A,l,r,pivot=pselect)
		pivot=part[1]
		#print("A ="+str(A)+" after partition "+str(part[0])+"l = "+str(l)+" r = "+str(r)+" pivot = "+str(pivot))
		A=part[0]
		m+=(pivot-l)-1
		m+=(r-pivot)
		qs(A,l,pivot,pselect)
		qs(A,pivot+1,r,pselect)



def partition(A,l,r,pivot='left'):
	#make a pivot. p is the value of the pivot element
	if pivot=='median':
		#use the 'median of three' to get the pivot
		medindex=median(A,l,r)
		swap(A,l,medindex)
	if pivot=='right':
		#exchange first and last element
		swap(A,l,r-1)
	p=A[l]
	i=l+1
	for j in range(i,r):
		if A[j] < p:
			swap(A,j,i)
			i+=1
	swap(A,l,i-1)
	return [A,i-1]

#given array, intarray, and indicies i and j
#swap the elements intarray[i] and intarray[j]
def swap(intarray,i,j):
	#print("i = "+str(i)+" j = "+str(j))
	#remember value of ith element, then over write it with jth element
	temp=intarray[i]
	intarray[i]=intarray[j]
	#swap out j for i
	intarray[j]=temp
	return intarray

#given array, A, and the left and right bound
#tell me which element is the median of three
def median(A,l,r):
	x=A[l]
	z=A[r-1]
	subLength=r-l
	if subLength%2==0:
		y=A[((r-l)/2) -1 + l]
	else:
		y=A[(r-l)/2 + l]

	return np.where(A==np.median([x,y,z]))[0][0]
	#the above method usese np.median, if you feel like that's cheating use the method below
#	if (x > y and x < z) or (x > z and x < y):
#		#print(A.index(x))
#		return np.where(A==x)[0][0]
#	elif (y > x and y < z) or (y > z and y < x):
#		#print(A.index(y))
#		return np.where(A==y)[0][0]
#	else:# (z > x and z < y) or (z > y and z < x):
		#print(A.index(z))
#		return np.where(A==z)[0][0]