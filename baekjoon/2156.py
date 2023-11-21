import sys
input = sys.stdin.readline

n = int(input())
num = [0] * 10001
for i in range(1,n+1):
    num[i] = int(input())
dp = [0] * 10001
dp[1] = num[1]
dp[2] = dp[1] + num[2]
for i in range(3,n+1):
    dp[i] = max(num[i-1] + dp[i-3] + num[i], dp[i-2] + num[i], dp[i-1])
print(dp[n])