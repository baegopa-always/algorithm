# 균형잡힌 세상
## 실버 4
import sys
input = sys.stdin.readline

stack = []
try:
    while True:
        string = input()
        if string[0] == '.':
            exit()
        for x in string:
            if x == '(' or x == '[':
                stack.append(x)
            elif x == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(x)
            elif x == ']':
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    stack.append(x)
            elif x == '.':
                break
        print("no" if stack else "yes")
        stack = []
except:
    exit()