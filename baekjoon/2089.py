import sys
input = sys.stdin.readline

n = int(input())
ans = []
while True :
    ans.append(n % 2)
    if n % 2 != 0:
        n-=1
    n //= -2
    if n==0:
        break

print(*ans[::-1],sep="")