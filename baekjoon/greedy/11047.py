# 동전 0
## 실버 4
import sys
input = sys.stdin.readline

n, k = map(int,input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

cnt = 0
while k > 0:
    coin = coins.pop()
    if coin <= k:
        cnt += k // coin
        k %= coin

print(cnt)