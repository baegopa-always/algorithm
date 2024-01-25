import sys
input = sys.stdin.readline
# nums[n]이 nums[n-x] (x는 1부터n) 크면 dp[n] = dp[n-x] + num[n]

n = int(input())
nums = list(map(int, input().rstrip().split()))
dp = [0] * 1000
dp[:len(nums)+1] = nums[:]
for i in range(n):
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i] = max(dp[j] + nums[i], dp[i])
print(max(dp))