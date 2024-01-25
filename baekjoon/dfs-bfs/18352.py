# 이코테 p339 - q.15
import sys
from collections import deque

input = sys.stdin.readline
n, m, k, x = map(int, input().split())

roads = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    roads[a].append(b)

cities = [-1 for _ in range(n + 1)]
cities[x] = 0
queue = deque([x])


def bfs():
    while queue:
        pos = queue.popleft()
        for i in roads[pos]:
            if cities[i] == -1:
                queue.append(i)
                cities[i] = cities[pos] + 1


bfs()

ans = []
check = 0
for i in range(1, n + 1):
    if cities[i] == k:
        print(i)
        check = 1

if check == 0:
    print(-1)
