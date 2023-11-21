import sys
input = sys.stdin.readline
n = int(input())
commands = [list(input().split()) for _ in range(n)]

stack = []
for i in range(n):
    if commands[i][0] == "push":
        stack.append(commands[i][1])
    elif commands[i][0] == "top":
        if len(stack) > 0:
            print(stack[-1])
        else:
            print(-1)
    elif commands[i][0] == "pop":
        if len(stack) > 0:
            print(stack[-1])
            del stack[-1]
        else:
            print(-1)
    elif commands[i][0] == "size":
        print(len(stack))
    elif commands[i][0] == "empty":
        if len(stack) == 0 :
            print(1)
        else:
            print(0)