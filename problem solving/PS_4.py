def honeycomb(N, M, honey):
    # DP 테이블 초기화
    dp = [[0] * (N + 1) for _ in range(M + 1)]
    
    # DP 연산 0, 1, 1, 2, 2, 3, 3
    for i in range(1, M + 1):
        for j in range(1, N + 1):
            # 현재 칸까지의 꿀의 합과 인접한 칸들의 DP 값 중 최댓값을 선택
            x=int((j+0.5*i)//1)
            y=int((j+0.5*(i-1))//1)
            if x<N+1 and y<N+1:
                dp[i][y] = honey[i - 1][j - 1] + max(dp[i - 1][y], dp[i][y - 1])
                print(dp[i][j])

    # 최대 꿀의 합 출력
    return dp[M][N]

# 입력 받기
N, M = map(int, input().split())
honey = []
for _ in range(M):
    row = list(map(int, input().split()))
    honey.append(row)

# 최대 꿀의 합 계산
result = honeycomb(N, M, honey)

# 결과 출력
print(result)