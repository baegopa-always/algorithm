import sys
n = int(input())
ans = sys.maxsize
for i in range(n//5+1):
    if (n-i*5) % 3 == 0:
        ans = min(ans,i+((n-i*5) // 3))

if ans == sys.maxsize:
    ans = -1
print(ans)