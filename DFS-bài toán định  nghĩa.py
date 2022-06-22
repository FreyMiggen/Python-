vertex=[(0,1),(1,2),(1,3),(1,4),(3,4)]
graph=[[0 for i in range(5)] for j in range(5)]
graph[0][1]=1
graph[1][2]=1
graph[1][3]=1
graph[1][4]=1

graph[3][4]=1
for i in range(5):
    for j in range(5):
        if graph[i][j]==1:
            graph[j][i]=1
visited=[False for i in range(5)]
track=[0]
def DFS(v,stack):
    visited[v]=True
    stack.append(v)
    
    if len(stack)==0:
        print("kim")
        return True
    else:
        print('count',stack)
        for i in range(5):
            print(v,i)
            if graph[v][i]==1 and visited[i]==False:
                visited[i]=True
        
                track.append(i)
                if DFS(i,stack):
                    return True
                print(stack,'before')
                stack.pop()
                
                
                
                
                print(stack)


    return False


DFS(0,[])
print(track)
print(visited)

    
    