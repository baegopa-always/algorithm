def fac(n):
    if n <= 0:
        return 1
    return n * fac(n-1)
x = fac(int(input()))
ans = 0
while x%10 == 0:
    ans+=1
    x//=10
print(ans)