x = [list(map(int,input().split())) for _ in range(9)]
s = max(x[0])
n, m = 1, x[0].index(s)+1
for i in range(8):
    if s<max(x[i+1]):
        s=max(x[i+1])
        n=i+2
        m=x[i+1].index(s)+1
print(s)
print(n,m)