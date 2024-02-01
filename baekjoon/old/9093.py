import sys
input = sys.stdin.readline

n = int(input())
stack = []
for _ in range(n):
    stack = list(map(list,input().split()))
    for i in range(len(stack)):
        for _ in range(len(stack[i])):
            print(stack[i].pop(),end="")
        print(" ",end="")
    print()