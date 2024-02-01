import sys
input = sys.stdin.readline
n = int(input())
dots = [list(map(int,input().split())) for _ in range(n)]
dots.sort(key=lambda x:(x[1],x[0]))
for i in range(n):
    print(*dots[i])