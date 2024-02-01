n = int(input())
c = 2
while True:
    if n == 1:
        break
    if n % c == 0:
        print(c)
        n//=c
    else:
        c+=1