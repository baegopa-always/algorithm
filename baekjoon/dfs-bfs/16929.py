# Two Dots
## 골드 4
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

data = [list(input().rstrip()) for _ in range(n)]
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

def inRange(x, y):
    return x >= 0 and y >= 0 and x < n and y < m

def dfs(visited, ld, i, j): # i, j 는 현재위치, i+dx[d], j+dy[d]는 다음 값
    visited[i][j] = 1
    for d in range(4):
        if ld == d:
            continue
        if inRange(i+dx[d], j+dy[d]) and data[i][j] == data[i+dx[d]][j+dy[d]]:
            if not visited[i+dx[d]][j+dy[d]]:
                dfs(visited, (d+2) % 4, i+dx[d], j+dy[d])
            elif i+dx[d] == row and j+dy[d] == col:
                print("Yes")
                exit()
    visited[i][j] = 0
                

visited = [[0 for _ in range(m)] for _ in range(n)]

for p in range(n):
    for q in range(m):
        row, col = p, q
        dfs(visited, -1, p, q)
print("No")