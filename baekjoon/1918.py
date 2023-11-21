import sys
input = sys.stdin.readline

string = input().rstrip()
stack = []
ans = []
for x in string:
    print(ans)
    print(stack)
    if 'A' <= x <= 'Z':
        ans.append(x)
    else: # 읽어들이는 게 연산 문자일 경우
        if (x == '-' or x == '+') and stack: # +, -
            while stack and stack[-1] != '(':
                ans.append(stack.pop())
            stack.append(x)
        elif x == ')': # 닫는괄호일 경우
            while stack and stack[-1] != '(':
                ans.append(stack.pop())
            stack.pop()
        elif x == '*' or x == '/' : #  곱, 나눗셈
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                ans.append(stack.pop())
            stack.append(x)
        else: # 여는 괄호, -, +
            stack.append(x)

while stack: # 스택에 남은 것 모두 추출
    ans.append(stack.pop())

print(*ans,sep="")