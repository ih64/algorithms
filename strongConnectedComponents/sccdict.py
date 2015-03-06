from scipy.stats import itemfreq
import sys
sys.setrecursionlimit(1000000)

#global variables
t=0
finishTime={}
leader={}
queue=[]
s='Null'


def dfsLoopFirst(graph):
    onoff={}
    #finishTime={}
    nodes=range(1,875715)

    for i in nodes:
        onoff[i]=0
    
    for i in nodes[::-1]:
        if onoff[i]==0:
            depthSearch(graph,i,onoff,direction='backward')
    return


def depthSearch(graph, node, onoff, direction='forward'):
    global t
    global finishTime
    global s
    global leader
    global queue
    onoff[node]=1
    if direction=='forward':
        leader[finishTime[node]]=finishTime[s]
    #print "discovered node "+str(node)
    if direction=='forward':
        childNodes=graph[node]
    elif direction=='backward':
        childNodes=graph[node]
    #print "now node "+str(node)+" children :"+str(childNodes)
    for child in childNodes:
        if onoff[child]==0:
            depthSearch(graph,child,onoff,direction=direction)
    if direction=='backward':
        t+=1
        finishTime[node]=t
        queue.append(node)
    return


def dfsLoopSecond(graph):
    global s
    onoff={}
    #finishTime={}
    
    #nodes = queue.reverse()
    
    for i in reversed(queue):
        onoff[i]=0
    
    for i in reversed(queue):
        if onoff[i]==0:
            s=i
            depthSearch(graph,i,onoff,direction='forward')
    return

def allTogether():
	graph = {}
	revgraph = {}
	with open('SCC.txt') as fhand:
	    for i in range(1,875715):
	        graph[i] = []
	        revgraph[i] = []
	    for line in fhand:
	        tmp_list = [int(num) for num in line.split()]
	        #print tmp_list[0]
	        graph[tmp_list[0]].append(tmp_list[1])
	        revgraph[tmp_list[1]].append(tmp_list[0])

	dfsLoopFirst(revgraph)
	dfsLoopSecond(graph)
    sccarray=np.array([leader[i] for i in leader])
    freq=itemfreq(sccarray)
	return freq