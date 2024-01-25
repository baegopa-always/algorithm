# vps 이려면 전부 괄호가 묶음이어야함
# stack에 하나씩 넣으며 쌍이 붙을 경우 제거
import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    data = list(input())
    stack = []
    for i in data[:-1]:
        stack.append(i)
        if len(stack) > 1 and stack[-1] == ")" and stack[-2] == "(":
            stack.pop()
            stack.pop()
    if len(stack) > 0:
        print("NO")
    else:
        print("YES")