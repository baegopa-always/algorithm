import sys
input = sys.stdin.readline

dp = [0] * 1001
n = int(input())
dp[1:n+1] = list(map(int,input().rstrip().split()))
for i in range(2,n+1):
    for j in range(1,i):
        dp[i] = min(dp[i], dp[i-j] + dp[j])
print(dp[n])