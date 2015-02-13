import numpy as np


'''
read in and sanatize the input data
return 2mX2 numpy array representing edges
'''
def nodePairs(filename):
	#read in the file and make a nested list with the data in it
	#the first element in each nested list represents the node number
	#ie graph[0][0] is eq to 1, graph[0][1] is eq to 2, etc
	with open(filename, 'r') as f:
		filetxt=f.read().splitlines()
	
	graph=[[int(y) for y in x] for x in [i.strip().split() for i in filetxt]]
	pairs=[]

	#store the data in a 2mX2 numpy array edges
	#each row of edges represents an edge between the i,j nodes in the row array
	#for example, if edges[2] is [1,2] this means there is an edge betwwen
	#node 1 and two. you expect to also have [2,1] as a row somewhere in there too
	for node in graph:
	    for i in range(1,len(node)):
	        pairs.append((node[0],node[i]))
	edges=np.array(pairs)

	return edges

def randContract(edges):
	#how many iterations do we need to preform?
	numNodes=np.unique(edges).shape[0]

	#initialize counter to 0
	#keep track of how many times we select an edge
	count=0
	while (numNodes - count > 2):
		#now we must pick an edge uniformly at random
		#to do this we only need to pick a row
		randPick=np.random.randint(low=0,high=edges.shape[0])
		nodeA,nodeB=edges[randPick]
		#print(randPick,nodeA,nodeB)

		#fuse nodeB into node A
		#making nodeBs edges join to A instead
		#everywhere we see nodeB, switch to nodeA
		edges[edges==nodeB]=nodeA

		#identify any self loops
		selfloop=np.where((edges[:,0]==nodeA) & (edges[:,1]==nodeA))[0]

		#print count
		#print selfloop
		#print edges
		#print '---'
		#remove the self loops
		#this automatically will remove the edge we randomly selected
		edges=np.delete(edges,selfloop,axis=0)
		count+=1
		

	#when the loop finishes, we have two nodes
	#the edges that cross the cut is half the length of the left over edges array


	return edges.shape[0]/2

def wrapper(filename):
	#read in data
	edges=nodePairs(filename)

	#how many times do we need to run the contraction algorithm to get 1/n chance?
	numNodes=edges.shape[0]
	ntries=int(numNodes**2*np.log(numNodes))

	#remember the min cuts we get from different trials
	minCutList=[]

	for i in range(0,ntries):
		#make sure we are passing the master graph to the algorithm
		trialEdges=edges
		#pass the graph to the contraction algorithm
		#update the minCutList array
		minCutList.append(randContract(trialEdges))

	return minCutList

