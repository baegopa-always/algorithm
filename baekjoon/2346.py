from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
arr = deque(enumerate(map(int, input().split())))
answer = []
pop = 0
while arr:
    if pop > 0:
        pop -= 1
        while pop != 0:
            arr.append(arr.popleft())
            pop -= 1
    elif pop < 0:
        while pop != 0:
            arr.appendleft(arr.pop())
            pop += 1
    idx, pop = arr.popleft()
    answer.append(idx + 1)

print(*answer,sep=" ")