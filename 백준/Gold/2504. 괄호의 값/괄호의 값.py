import sys

input = sys.stdin.readline

data = input().rstrip()
stack = []
for x in data:
    while len(stack) > 1 and stack[-1].isdigit() and stack[-2].isdigit():
        a = stack.pop()
        b = stack.pop()
        stack.append(str(int(a) + int(b)))
    if x == "]":
        if stack and stack[-1] == "[":
            stack.pop()
            stack.append("3")
        elif len(stack) > 1 and stack[-1].isdigit() and stack[-2] == "[":
            n = stack.pop()
            stack.pop()
            stack.append(str(int(n) * 3))
        else:
            stack.append(x)
    elif x == ")":
        if stack and stack[-1] == "(":
            stack.pop()
            stack.append("2")
        elif len(stack) > 1 and stack[-1].isdigit() and stack[-2] == "(":
            n = stack.pop()
            stack.pop()
            stack.append(str(int(n) * 2))
        else:
            stack.append(x)
    else:
        stack.append(x)

while len(stack) > 1 and stack[-1].isdigit() and stack[-2].isdigit():
    a = stack.pop()
    b = stack.pop()
    stack.append(str(int(a) + int(b)))

print(stack[0] if len(stack) == 1 and stack[0].isdigit() else 0)