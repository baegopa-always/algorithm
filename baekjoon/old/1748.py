import sys
n = int(sys.stdin.readline())
s = n // 10
ans = 0
t = 0
while s > 0:
    ans += 9 * (10**t) * (t+1)
    t+=1
    s//=10
if t > 0:
    ans += ((n - 10**t) + 1) * (t+1)
    print(ans)
else:
    print(n)
