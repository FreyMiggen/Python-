# procedure: Depth First Search (DFS) algorithm traverses a graph in a depthward motion
#  and uses a stack to remember to get the next vertex to start a search, 
# when a dead end occurs in any iteration. As in the example given above, DFS algorithm traverses from S to A to D to G to E to B first, then to F and lastly to C.


# find the path from 0 to 4 according to DFS
vertex=[(1,2),(1,5),(2,3),(2,5),(3,5),(4,5)]
graph=[[0 for i in range(5)] for j in range(5)]
graph[0][1]=1
graph[0][4]=1
graph[1][2]=1
graph[1][4]=1
graph[2][4]=1
graph[3][4]=1
for i in range(5):
    for j in range(5):
        if graph[i][j]==1:
            graph[j][i]=1
for i in range(5):
    print(graph[i])

arr=[True for i in range(5)]
def DFS(v,track):
    arr[v]=False
    if track[-1]==4:
        return True
    else:

        # get a list of all adjacent nodes to v
        # if this node is not visited, then add it to link
        
        for i in range(5):
            if graph[v][i]==1 and arr[i]==True:
                arr[i]=False
                track.append(i)
                if DFS(i,track):
                    return True
                
                vertex=track.pop()
                arr[vertex]=True
                DFS(track[-1],track)
    return False
track=[0]
DFS(0,track)

print(track)

            
            

    