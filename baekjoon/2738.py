n,m = map(int,input().split())

vector1 = [list(map(int,input().split())) for i in range(n)]
vector2 = [list(map(int,input().split())) for i in range(n)]

for i in range(n):
    print(*[vector1[i][j]+vector2[i][j] for j in range(m)])