import sys

input = sys.stdin.readline

n = int(input())
stack = []

data = list(map(int, input().split()))
ans = []
for idx, num in enumerate(data):
    while stack and stack[-1][1] < num:
        stack.pop()
    if stack and stack[-1][1] >= num:
        ans.append(stack[-1][0])
    else:
        ans.append(0)
    stack.append([idx + 1, num])

print(*ans)
