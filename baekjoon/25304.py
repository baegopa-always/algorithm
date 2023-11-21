s=int(input())
for _ in range(int(input())):
    a,b=map(int,input().split())
    s-=a*b
print("Yes" if s==0 else "No")