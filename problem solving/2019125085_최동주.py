# N x N 표 설정
n, m = map(int, input().split())

# 각 좌표에 수 입력
table = []
for _ in range(n):
    table.append(list(map(int, input().split())))

# (0,0)~(i,j) 누적합 저장
# i-1, j-1 음수 방지 위해 한칸 더 큰 배열 생성
tableSum = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        tableSum[i][j] = tableSum[i][j - 1] + tableSum[i - 1][j] + table[i - 1][j - 1] - tableSum[i - 1][j - 1]

# 구간합 계산 및 출력. 겹치는 부분 2번 빼주므로 다시 더함
for _ in range(m):
    a, b, c, d = map(int, input().split())
    s = tableSum[c][d] - tableSum[c][b - 1] - tableSum[a - 1][d] + tableSum[a - 1][b - 1]
    print(s)
    