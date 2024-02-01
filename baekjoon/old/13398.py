import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))

dp = nums[:]
for i in range(1,n):
    dp[i] = max(dp[i], nums[i] + dp[i-1])

dp2 = dp[:]

for i in range(1,n):
    dp2[i] = max(dp2[i-1] + nums[i], dp[i-1])

print(max(max(dp2),max(dp)))