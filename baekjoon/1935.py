# 
#
import sys
input = sys.stdin.readline

n = int(input())
formula = input().rstrip()
nums = [int(input()) for _ in range(n)]
stack = []

for i in formula:
    if not str(i).isalnum(): # 특문이라면
        y = stack.pop() # 우항
        x = stack.pop() # 좌항
        x = nums[ord(x) - 65] if str(x).isalpha() else x
        y = nums[ord(y) - 65] if str(y).isalpha() else y
        if i == '+':
            stack.append(x+y)
        elif i == '*':
            stack.append(x*y)
        elif i == '-':
            stack.append(x-y)
        elif i == '/':
            stack.append(x/y)
        continue
    stack.append(i)
print("{:.2f}".format(stack.pop()))
# print('%.2f' %stack.pop())