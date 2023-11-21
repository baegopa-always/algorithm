n,m=map(int,input().split())
x=[i for i in range(n+1)]
for _ in range(m):
    i,j=map(int, input().split())
    x[i:j+1]=x[i:j+1][::-1]
print(*x[1:])