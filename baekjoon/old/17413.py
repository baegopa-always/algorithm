import sys
from collections import deque
input = sys.stdin.readline

string = input().rstrip()
deq = deque()
ans = []
for i in string:
    if (i == ' ' and '<' not in deq) or i == '<':
        while deq:
            ans.append(deq.pop())
        if i == '<':
            deq.append('<')
        elif i == ' ':
            ans.append(' ')
    elif i == '>':
        while deq:
            ans.append(deq.popleft())
        ans.append('>')
    else:
        deq.append(i)
while deq:
    ans.append(deq.pop())
print(*ans,sep="")