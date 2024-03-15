# 프로그래머스 - 연속된 부분 수열의 합
def solution(sequence, k):
    answer = [0,10000000]
    dp = [0 for _ in range(len(sequence) + 1)]
    s = 0
    for i in range(1, len(sequence) + 1):
        dp[i] = dp[i-1] + sequence[i-1]
        while dp[i] > k:
            if dp[i] - dp[s] <= k:
                break
            s += 1
        if dp[i] - dp[s] == k and answer[1] - answer[0] > i-1-s:
            answer = [s, i-1]
    return answer