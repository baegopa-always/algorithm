# 도키도키 간식드리미
## 실버3
import sys

n = int(input())
lst = list(map(int,input().split()))
stack = []
target = 1
for i in range(n):
    if lst[i] == target:
        target+=1
    else:
        stack.append(lst[i])
    while stack:
        if stack[-1] == target:
            target += 1
            stack.pop()
        else:
            break

print("Sad" if stack else "Nice")