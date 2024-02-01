import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))

dp = [1 for _ in range(n)]
for i in range(n):
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i] = max(dp[i], dp[j] + 1)

dp2 = [0 for _ in range(n)]
for i in range(n-1,-1,-1):
    for j in range(n-1,i,-1):
        if nums[i] > nums[j]:
            dp2[i] = max(dp2[i], dp2[j] + 1)
    dp[i] += dp2[i]
print(max(dp))
