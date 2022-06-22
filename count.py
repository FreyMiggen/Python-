board=[[True for i in range(8)] for j in range(8)]
def rcross(i,j):
    while (j-7)*(i-7)>0:      
        j+=1
        i+=1
        board[i][j]=False

def lcross(i,j):
    while (7-i)*j>0:
        j-=1
        i+=1
        board[i][j]=False
        
def rstore(i,j):
    while (j-7)*(i-7)>0:        
        j+=1
        i+=1
        board[i][j]=True
        
def lstore(i,j):
    while (7-i)*j>0:        
        j-=1
        i+=1
        board[i][j]=True
track=[True for i in range(8)]
lt=list()

def arrangeQueen(i,lt):
    if len(lt)==8 and i==8:
        
        return True
    else:
        for j in range(8):
            if track[j]== True and board[i][j]==True:
                board[i][j]=1
                rcross(i,j)
                lcross(i,j)
                track[j]=False
                lt.append([i,j])
                print(lt)
                if arrangeQueen(i+1,lt):
                    return True
    
    
                cell=lt.pop()
                m=cell[0]
                n=cell[1]
                lstore(m,n)
                rstore(m,n)
                track[n]=True
                board[m][n]=True
                
                       
    return False

arrangeQueen(0,lt)
for i in range(8):
    print(board[i])
    

    

arrangeQueen(0,lt)
# lcross(0,7)
# lstore(0,7)
for i in range(8):
    print(board[i])
print(lt)
