# Minimum spanning tree

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
# board[v] = min{w(u,v)|u thuộc S và v thuộc Q}, có thể set board[0]=0 vì bắt đầu duyệt từ đỉnh 0
board=[math.inf for i in range(9)]

#parent
parent=dict()
# Cấu hình khởi tạo ban đầu: S rỗng, Q chứa all vertices
def Adj(v):
    adj=list()
    for i in range(9):
        if gr[v][i]!=0:
            adj.append(i)
    return adj
def findMin(S):
    min_v=math.inf
    for i in range(9):
        if board[i]<min_v and i not in S:
            min_v=board[i]
    return min_v
def MST(u,S,Q):
    while len(Q)>0:
        print(u,S,Q,board)
        Q.pop(Q.index(u))
        S.append(u)
        for v in Adj(u):
            if v in Q and gr[u][v]<board[v]:
                board[v]=gr[u][v]
                parent[v]=u
        # chọn vertex có w nối đến S nhỏ nhất
        min_v=findMin(S)
        if min_v!=math.inf:
            next_u=board.index(min_v)
            MST(next_u,S,Q)
    
MST(0,[],list(range(9)))

print(board)
print(parent)
