# 알고리즘 수업 - 피보나치 수 1
## 브론즈 1
import sys
input = sys.stdin.readline

dp = [0 for _ in range(41)]
def fibDP(n):
    cnt = 0
    dp[1],dp[2] = 1, 1
    for i in range(3,n+1):
        dp[i] = dp[i-1] + dp[i-2]
        cnt+=1
    return cnt

n = int(input())
cnt = fibDP(n)
print(dp[n], cnt)