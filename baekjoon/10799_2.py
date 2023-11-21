import sys
input = sys.stdin.readline

seg = input().rstrip()
stack = []

ans = 0
for i in range(len(seg)):
    if seg[i] == '(':
        stack.append(seg[i])
    else:
        stack.pop()
        if seg[i-1] == '(':
            ans += len(stack)
        else:
            ans += 1
print(ans)