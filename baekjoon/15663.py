import sys
input = sys.stdin.readline
ans = []
def dfs(lst, c, last):
    if c == m:
        ans.append(lst)
        return
    last = 0
    for i in range(n):
        if not visited[i] and last != data[i]:
            last = data[i]
            visited[i] = 1
            dfs(lst + [data[i]], c+1, last)
            visited[i] = 0
    return
n, m = map(int,input().split())
data = sorted(list(map(int,input().split())))
visited = [0] * n

dfs([], 0, 0)

for x in ans:
    print(*x)