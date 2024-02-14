# 스택 2
## 실버 4
import sys

input = sys.stdin.readline
n = int(input())

stack = []
for _ in range(n):
    cmd = input().split()
    c = int(cmd[0])
    if c == 1:
        stack.append(cmd[1])
    elif c == 2:
        if len(stack) > 0:
            print(stack.pop())
        else:
            print(-1)
    elif c == 3:
        print(len(stack))
    elif c == 4:
        print(1 if len(stack) == 0 else 0)
    elif c == 5:
        if len(stack) > 0:
            print(stack[-1])
        else:
            print(-1)
