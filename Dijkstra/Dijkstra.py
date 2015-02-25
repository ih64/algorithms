import numpy as np 

def graphDataStructure(filename):
	
	with open(filename,'r') as f:
		filetext=f.read().splitlines()

    #clean up the data and restructure it
	#pairs is a dictionary. Every node is a key
	#the values are lists that have the node number,
	#a second node that forms an  with it edge, and the edge weight
	pairs={}
	for row in filetext:
		cleanrow=row.split()
		pairs[int(cleanrow[0])]=[]
		for i in range(1,len(cleanrow)):
			tail,weight=cleanrow[i].split(',')
			pairs[int(cleanrow[0])].append((int(cleanrow[0]),int(tail),int(weight)))

	#turn all the lists into numpy arrays.
	for i in pairs:
		pairs[i]=np.array(pairs[i])

	return pairs

def shortPath(filename):

	pairs=graphDataStructure(filename)
	#initialize our housekeeping variables. 
	#X is a list that has the conqured nodes
	#A is a dict, each key is a node, and the value is the distance to that node
	#The source node is node 1, and the path length to it is the empty path
	X=[1]
	A={}
	A[1]=0

	#find the edges that have one node in X, and one node not in X
	#first list all the [nodestart,nodeend, edgelength] for all the nodes in X
	#stack them into a numpy array
	#then iterate over the stacked array and only select edges if they have an end that is not in X
	#this is basically a double for loop, and why this algorithm is O(nm) runtime
	crossing=np.array([j for j in np.vstack([pairs[i] for i in X]) if j[1] not in X])

	numloops=0
	while len(crossing) > 0:
		#for all the crossing edges, find the total distance from the source node to thier head nodes
		crossingTotDist=np.hstack((crossing,np.vstack([A[i[0]] + i[2] for i in crossing])))

		#find the smallest length of these
		#extract its node which is in X, node outside of X, and edge legth
		conqnode, newnode, length, distance=crossingTotDist[crossingTotDist[:,3].argmin()]

		#the path length to the new node is the lenght to the node in X which shares an edge with it, plus the edge length
		#Dijkstra's greedy formula, from the lectures
		A[newnode]=distance

		#the new node is now in our explored territory
		X.append(newnode)

		#recalculate the edges that cross the cut btwn conqured graph and unexplored graph
		crossing=np.array([j for j in np.vstack([pairs[i] for i in X]) if j[1] not in X])
		numloops+=1
		print numloops

	return A

