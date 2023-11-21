import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))
dp = [1] * n

for i in range(n):
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i] = max(dp[i],dp[j]+1)

t = max(dp)
arr = []
for i in range(n-1,-1,-1):
    if dp[i] == t:
        arr.append(nums[i])
        t-=1
print(max(dp))
print(*reversed(arr))