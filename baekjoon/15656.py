import sys
input = sys.stdin.readline

ans = []
def dfs(lst, c):
    if c == m:
        ans.append(lst)
        return
    for i in range(n):
        dfs(lst + [data[i]], c+1)
    return

n, m = map(int,input().split())
data = sorted(list(map(int,input().split())))
visited = [0] * n

dfs([], 0)
for x in ans:
    print(*x)