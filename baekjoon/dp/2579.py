# 계단 오르기
## 실버 3
import sys
input = sys.stdin.readline

nums = [0 for _ in range(301)]
n = int(input())
for i in range(1,n+1):
    nums[i] = int(input())

dp = [0 for _ in range(301)]

dp[1], dp[2],dp[3] = nums[1],nums[1]+nums[2],max(nums[1]+nums[3],nums[2]+nums[3])

for i in range(3,n+1):
    dp[i] = max(nums[i] + nums[i-1] + dp[i-3], nums[i] + dp[i-2])

print(dp[n])