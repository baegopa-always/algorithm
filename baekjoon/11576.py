import sys
input = sys.stdin.readline

a,b = map(int,input().split())
m = int(input())
aNum = list(map(int,input().split()))
c = 0
for i in aNum:
    c = c*a + i
ans = []
while c != 0:
    ans.append(c % b)
    c //= b
print(*ans[::-1])
