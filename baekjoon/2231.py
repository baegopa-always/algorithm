n = input()
c = int(len(n))*9
n = int(n)
ans = 0
for i in range(n-c,n):
    x = i
    j = i
    while i > 0:
        x += i % 10
        i//=10
    if x == n:
        ans = j
        break
print(ans)