# A, B, N 입력
a,b,n = map(int, input().split())
cnt = b-a+1

# 소인수 구하기
factor=2
prime=[]

while factor**2 < n:
    if n%factor==0:
        prime.append(factor)
        while n%factor==0 :
            n//=factor
    factor+=1

if n != 1:
    prime.append(n)
        
# 서로소인 수의 개수, n의 소인수와 관계가 없어야 함
for i in range(a,b+1):
    for j in range(len(prime)):
        if i%prime[j]==0:
            cnt-=1
            break

print(cnt)