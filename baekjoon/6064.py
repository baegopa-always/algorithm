import sys
input = sys.stdin.readline

def gcd(a,b):
    if a == 0:
        return b
    return gcd(b%a,a)

for _ in range(int(input())):
    m, n, x, y = map(int,input().split())
    ans = -1
    limit = m * n // gcd(m, n)
    while True:
        if x > limit:
            break
        c = x % n
        if c == 0:
            c = n
        if c == y:
            ans = x
            break
        x+=m
    print(ans)