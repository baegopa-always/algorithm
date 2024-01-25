n,m=map(int,input().split())
t=[]
for i in range(n): t.append(i+1)
for _ in range(m):
    i,j=map(int,input().split())
    k=t[i-1]
    t[i-1]=t[j-1]
    t[j-1]=k
print(*t)