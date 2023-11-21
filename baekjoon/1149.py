import sys
input = sys.stdin.readline

n = int(input())

color_cost = [list(map(int,input().split())) for _ in range(n)]
dp = [[0] * 3 for _ in range(1000)]

for i in range(n):
    for j in range(3):
        dp[i][j] = min(dp[i-1][j-1] + color_cost[i][j], dp[i-1][j-2] + color_cost[i][j])

print(min(dp[n-1]))