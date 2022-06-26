graph=[[0 for i in range(7)] for i in range(7)]
graph[0][1]=1
graph[0][3]=1
graph[1][0]=1
graph[1][4]=1
graph[2][1]=1
graph[2][6]=1
graph[4][3]=1
graph[5][4]=1
graph[5][2]=1
graph[6][5]=1
visited=[False for i in range(7)]
def findCon(v,track):
    visited[v]=True
    for i in range(7):
        if graph[v][i]==1 and visited[i]==False:
            track.append(i)
            findCon(i,track)
    
    return track
result=list()
checked=[False for i in range(7)]
for i in range(7):
    if checked[i]==False:
        visited=[False for i in range(7)]
        tem=findCon(i,[i])
        result.append(tem)
        for j in tem:
            checked[j]=True

print(result)
    

    
    