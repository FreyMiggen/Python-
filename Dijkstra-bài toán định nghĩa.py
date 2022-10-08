#https://chidokun.github.io/2021/09/dijkstra-algorithm/
# Dijkstra: shortest path with no minus value



gr=[[0 for i in range(9)] for i in range(9)]
gr[0][3]=21
gr[0][1]=25
gr[0][2]=20
gr[1][4]=10
gr[2][5]=15
gr[2][4]=6
gr[3][5]=25
gr[4][6]=23
gr[5][6]=19
gr[5][7]=20
gr[6][7]=18
gr[6][8]=17
gr[7][8]=20
for i in range(9):
    for j in range(9):
        if gr[i][j]!=0:
            gr[j][i]=gr[i][j]



import math
board=[math.inf for i in range(9)]
board[0]=0
done=[False for i in range(9)]

def find_next_node(board,stack):
    min=math.inf
    index=0
    for i in stack:
        if board[i]<min:
            min=board[i]
            index=i
    return stack.index(index)
def Dij(v,stack):
    done[v]=True
    for i in range(9):
        if gr[v][i]!=0 and done[i]==False:
            board[i]=min(board[v]+gr[v][i],board[i])
            stack.append(i)
    stack=stack[1:]
    if len(stack)==0:
        return board
    else:
        print(stack[0],'kim')
        Dij(stack[0],stack)
    
    return board

print(Dij(0,[]))


            
    
