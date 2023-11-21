import sys
input = sys.stdin.readline

n = int(input())
cost = [list(map(int,input().split())) for _ in range(n)]
ans = 10**6
for i in range(3):
    dp = [arr[:] for arr in cost]
    dp[0][i-1], dp[0][i-2], dp[-1][i] = 1001, 1001, 10**6
    for j in range(1,n):
        dp[j][0] += min(dp[j-1][1], dp[j-1][2])
        dp[j][1] += min(dp[j-1][0], dp[j-1][2])
        dp[j][2] += min(dp[j-1][0], dp[j-1][1])
    ans = min(ans, min(dp[n-1]))
print(ans)