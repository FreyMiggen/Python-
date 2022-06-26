vertex=[(0,1),(0,2),(0,4),(1,2),(1,3),(3,4)]
graph=[[0 for i in range(5)] for i in range(5)]
graph[0][1]=1
graph[0][2]=1
graph[0][4]=1
graph[1][2]=1
graph[1][3]=1
graph[2][4]=1
graph[3][4]=1
for i in range(5):
    for j in range(5):
        if graph[i][j]==1:
            graph[j][i]=1

visited=[False for i in range(5)]
trace=[]
def BFS(v,track):
    visited[v]=True
    trace.append(v)
    for i in range(5):
        if graph[v][i]==1 and visited[i]==False:
            track.append(i)
            visited[i]=True
    
    track=track[1:]
    if len(track)==0:
        print('kim')
        return True
    else:
        BFS(track[0],track)

    return False

BFS(0,[0])

    
        
print(trace)
    





    
    
    