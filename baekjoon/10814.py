import sys
input = sys.stdin.readline
n = int(input())
people = [list(input().split()) for _ in range(n)]
people.sort(key=lambda x:int(x[0]))
for i in people:
    print(*i)