import sys
input = sys.stdin.readline

n = int(input())
dp = [[0] * 501 for _ in range(501)]
triangle = [[0]]
for i in range(n):
    triangle.append(list(map(int,input().rstrip().split())))

for i in range(1,n+1):
    dp[i][1] = dp[i-1][1] + triangle[i][0]
    dp[i][i] = dp[i-1][i-1] + triangle[i][i-1]
    for j in range(2,i):
        dp[i][j] = max(dp[i-1][j-1],dp[i-1][j]) + triangle[i][j-1]
print(max(dp[n]))

# input으로 받는 배열 하나로 가능