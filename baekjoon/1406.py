import sys
input = sys.stdin.readline
string = list(input().rstrip())
n = int(input())
pos = len(string)
stack = []
for _ in range(n):
    command = list(input().split())
    if command[0] == "P":
        string.append(command[1])
    elif command[0] == "L" and len(string) > 0:
        stack.append(string.pop())
    elif command[0] == "D" and len(stack) > 0:
        string.append(stack.pop())
    elif command[0] == "B" and len(string) > 0:
        string.pop()
print(*string,*stack[::-1],sep="")