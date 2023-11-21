n=int(input())
for i in range(n):
    print(" "*(n-i-1)+"*"*(1+i*2))
for i in range(1,n):
    print(" "*i+"*"*(1+(n-i-1)*2))