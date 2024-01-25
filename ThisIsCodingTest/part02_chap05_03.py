n, m = map(int, input().split())

iceFrame = [list(map(int,list(input()))) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]


def dfs(iceFrame, i, j):
    if not (i < n and j < m and i > -1 and j > -1):
        return 0
    if visited[i][j] == 0 and iceFrame[i][j] == 0:  # 둘다 방문하지 않음
        visited[i][j] = 1
        dfs(iceFrame, i + 1, j)
        dfs(iceFrame, i - 1, j)
        dfs(iceFrame, i, j + 1)
        dfs(iceFrame, i, j - 1)


ans = 0

for i in range(n):
    for j in range(m):
        if visited[i][j] == 0 and iceFrame[i][j] == 0:
            ans += 1
            dfs(iceFrame, i, j)

print(ans)
