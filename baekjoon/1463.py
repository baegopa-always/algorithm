import sys
n = int(sys.stdin.readline())
dp = [0] * (n+1)
# 2부터 n까지 모든 수가 1이 되는 횟수의 최소 구하기

for i in range(2,n+1):
    dp[i] = dp[i-1] + 1 # 이전의 수가 가진 연산 횟수에서 1빼는 연산을 하는 것이 기본값
    # 그것보다 더 나은 방법이 있었는지 확인
    if i % 3 == 0: # 나누어진 수가 가진 연산 횟수와 수가 현재 가진 연산 횟수 비교
        dp[i] = min(dp[i//3]+1,dp[i])
    if i % 2 == 0: # 2로 나눈 값, 3으로 나눈 값 중 더 작은 값이 있을 수 있으므로 if문 따로
        dp[i] = min(dp[i//2]+1,dp[i])
print(dp[n])