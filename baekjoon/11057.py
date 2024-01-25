import sys
input = sys.stdin.readline

n = int(input())
dp = [[1] * 10 for _ in range(1000)]

for i in range(1,1000):
    for j in range(10):
        dp[i][j] = sum(dp[i-1][j:10]) % 10007

print(sum(dp[n-1]) % 10007)