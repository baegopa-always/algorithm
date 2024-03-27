# 백준 - 참외밭
# 실버 2
import sys

input = sys.stdin.readline

n = int(input())
data = [list(map(int, input().split())) for _ in range(6)]
# 방향이 하나 들어가있다. 둘 들어가있다.. ?

t = 0
for i in range(len(data)):
    if data[i - 2][0] == data[i][0] and data[i - 1][0] == data[i - 3][0]:
        y = data[i - 1][1] * data[i - 2][1]
        x = data[i - 4][1] * data[i - 5][1]
        t = x - y

print(n * t)
