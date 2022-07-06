# talks: a list of talk with (name,starting time, ending time, number of attendees joining)

talks=[(1,8,10,15),(2,9,11,20),(3,9.5,13,30),(4,10.5,12,10),(5,11,14,30),(6,13,14,20),(7,8.5,14,30)]
N=len(talks)
# Step 1: arrange talks so that ending time increases

arr_talks=sorted(talks,key=lambda x: x[2])

# Step 2: create a name list, so that name[i]=ten cua talk xep thu i theo arr_talks
name=[arr_talks[i][0] for i in range(N)]

# Step 3: create s (starting time) and e (ending time) based on arr_talks and at (number of attendees)
s=[arr_talks[i][1] for i in range(N)]
e=[arr_talks[i][2] for i in range(N)]
at=[arr_talks[i][3] for i in range(N)]

# Step 4: Create a p list so that p[j]= i sao cho i là số lớn nhất thỏa mãn e[i]<=s[j]. 
#         Tức là i là talk có thời gian kết thúc muộn nhất để vẫn compatible vs talk thứ j
p=[None for i in range(N)]
for i in range(N):
    for j in range(i):
        if e[j]<=s[i]:
            print(i,j)
            p[i]=j

            

kim=[(arr_talks[i][1],arr_talks[i][2]) for i in range(N)]
print(kim)       
 

""""
Giải thích cách làm
T[m]: max lượng người tham gia ở cấu hình tối ưu, xét đến talk thứ m.
OS[m]: cấu hình tối ưu, xét đến talk thứ m
Xét talk thứ j. Khi này có 2 trường hợp xảy ra:
- Talk j thuộc cấu hình tối ưu (Optimal Schedule-OS[j]). Khi đó:
    + Các talks thứ p[j]+1,..n sẽ không thuộc OS[j] (vì không compatible với talk j)
    + OS[j] đang chứa cấu hình tối ưu cho talk 1->p[j]. Vì nếu không, bằng cách thêm talk j vào cấu hình tối ưu của talk 1->p[j], ta sẽ có cấu hình tối ưu hơn
   => T[j]=at[j]+T[p[j]] (1)
- Talk j không thuộc cấu hình tối ưu OS[j]. Khi đó: OS[j]=OS[j-1] và
    => T[j]=T[j-1]  (2)

Từ (1) và (2) suy ra:
    T[j]=max(at[j]+T[p[j]],T[j-1])

"""
print(p)
T=dict()
T[None]=0
T[0]=at[0]

for i in range(1,N):
    T[i]=max(T[i-1],T[p[i]]+at[i])

# pre[i]=None if talk i is the first talk included in OS[i]
# pre[i]=-1 if talk i is not included in OS[i]
#pre[i]=j => talk j is the talk included before talk i
pre=dict()
pre[0]=None
for i in range(1,N):
    if T[p[i]]+at[i]>T[i-1]:
    
        pre[i]=p[i]
    else:
        pre[i]=-1
        

print(T)
# From {0: None, 1: None, 2: 0, 3: None, 4: 1, 5: -1, 6: -1} => OS[6]=OS[4] and OS[4]=4,1