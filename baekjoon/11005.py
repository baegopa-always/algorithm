import sys
input = sys.stdin.readline

n, b = map(int,input().split())
ans = ['']
while n != 0:
    s = n % b
    if s < 10:
        ans+=str(s)
    else:
        ans+=chr(55+s)
    n//=b
print(*ans[::-1],sep="")