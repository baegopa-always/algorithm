import math

n, m = map(int, input().split())
maze = [list(map(int, input())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
ans = math.inf
def dfs(x, y, distance):
    global ans
    if not (x > -1 and y > -1 and x < n and y < m) or maze[x][y] == 0 or visited[x][y] == 1:
        return 0
    else:
        distance += 1
        visited[x][y] = 1
        if x == n-1 and y == m-1:
            ans = min(ans, distance)
        else:
            dfs(x+1, y, distance)
            dfs(x-1, y, distance)
            dfs(x, y+1, distance)
            dfs(x, y-1, distance)

for i in range(n):
    for j in range(m):
        if maze[i][j] == 1:
            dfs(i,j,0)
print(ans)