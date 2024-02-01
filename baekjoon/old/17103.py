# 에라토스테네스 100만까지 1 => 0
# 0인 것들 제거
# 각 숫자의 절반까지 ?
import sys
input = sys.stdin.readline

nums = [1] * 1000001
primes = []
# 소수 모음
for i in range(2,1001): # 2 3 5 7 11 13 17 19 23
    if nums[i] != 0:
        for j in range(i*2,1000001,i):
            nums[j] = 0
nums[0],nums[1] = 0, 0
for i in range(2,1000001):
    if nums[i] == 1:
        primes.append(i)

for _ in range(int(input())):
    n = int(input())
    ans = 0
    for i in primes:
        if i > n/2:
            break
        if nums[n-i] == 1:
            ans+=1
    print(ans)