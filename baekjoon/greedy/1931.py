# 회의실 배정
## 실버 1

## 1. 끝나는 시간 기준으로 정렬 -> 시작 시간만 고려하면 됨
## 2. 끝나는 시간 이후에 시작하는 회의 중 끝나는 시간이 가장 빠른 회의 찾기 (반복), 처음은 끝나는 시간 0 이라고 가정
import sys
input = sys.stdin.readline

n = int(input())
data = []

for _ in range(n):
    data.append(list(map(int,input().split())))

data.sort(key=lambda x: (x[1],x[0]))
cnt = 0
lastEnd = 0
for start, end in data:
    if start >= lastEnd:
        cnt += 1
        lastEnd = end

print(cnt)