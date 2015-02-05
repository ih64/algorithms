import numpy as np

def sort(intarray,count):
	size=len(intarray)
	#chop array into two
	if size == 1:
		return [intarray, count]
	else:
		if size%2==0:
			A=sort(intarray[:size/2],count)
			B=sort(intarray[size/2:],count)
		else:
			A=sort(intarray[:(size+1)/2],count)
			B=sort(intarray[(size+1)/2:],count)
		join = merge(A,B)
		count+= join[1]
		return [join[0],count]

def merge(A, B):
    # Loop through all elements of both lists
    count=A[1]+B[1]
    result = []
    i, j = 0, 0
    while i < len(A[0]) and j < len(B[0]):
        if A[0][i] <= B[0][j]:
            result.append(A[0][i])
            i = i + 1
        else:
            result.append(B[0][j])
            j = j + 1
            count+=len(A[0])-i
    while i < len(A[0]):
        result.append(A[0][i])
        i = i + 1
    while j < len(B[0]):
        result.append(B[0][j])
        j = j + 1

    return [result,count]