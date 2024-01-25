import sys
input = sys.stdin.readline

n = int(input())
dp = [0 for _ in range(31)]
dp[0], dp[2] = 1, 3

for i in range(4,31,2):
    dp[i] += dp[i-2]*3 + 2
    for j in range(2,i-3,2):
        dp[i] += dp[j] * 2

print(dp[n])