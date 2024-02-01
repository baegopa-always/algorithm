def ans(a,b):
    return a*b//gcd(a,b)
def gcd(a,b):
    if a == 0:
        return b
    return gcd(b%a,a)
for _ in range(int(input())):
    a,b = map(int,input().split())
    print(ans(a,b))