import numpy as np

t=0
queue=[]
finishTime={}
s='Null'
leader={}

def dfsLoopFirst(graph):
    onoff={}
    #finishTime={}
    nodes=np.unique(graph[:,0])

    for i in nodes:
        onoff[i]=0
    
    for i in nodes[::-1]:
        if onoff[i]==0:
            depthSearch(graph,i,onoff,direction='backward')
    return finishTime

#depth first search algorithm
#agressively search down graph
#recurse on child nodes that are not yet discoverd
#takes graph, node to start, onoff is a logical dict which tells us which nodes are discovered
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
        childNodes=graph[np.where(graph[:,0]==node)][:,1]
    elif direction=='backward':
        childNodes=graph[np.where(graph[:,1]==node)][:,0]
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

