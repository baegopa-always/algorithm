import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    dp = [[0],[0]]
    dp[0].extend(list(map(int,input().rstrip().split()))[:])
    dp[1].extend(list(map(int,input().rstrip().split()))[:]) # dp[2][n]
    for i in range(2,n+1):
        dp[0][i] += max(dp[1][i-1], dp[1][i-2])
        dp[1][i] += max(dp[0][i-1], dp[0][i-2])
    print(max(dp[0][-1],dp[1][-1]))