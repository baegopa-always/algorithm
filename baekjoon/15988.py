import sys
input = sys.stdin.readline

dp = [0] * (10**6+1)
dp[1], dp[2], dp[3] = 1, 2, 4

for i in range(4,10**6+1):
    dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % 1000000009

for i in range(int(input())):
    print(dp[int(input())])