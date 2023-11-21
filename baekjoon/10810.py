n,m=map(int,input().split())
a=[0]*n
for _ in range(m):
     i,j,k=map(int,input().split())
     for x in range(i-1,j):
          a[x]=k
print(*a)