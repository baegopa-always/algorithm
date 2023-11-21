# 1. 남은 숫자들로 목표수와 가장 차이가 적은 수를 만들어내야함
# 2. 1보다 목표수와 기본 수의 차이가 더 적은지 확인
import sys

input = sys.stdin.readline
n = int(input())
m = int(input())
notwork = list(map(int,input().split()))
ans = 1000001
for i in range(1000001):
    i = str(i)
    for j in range(len(i)):
        if int(i[j]) in notwork:
            break
        elif j == len(i) - 1:
            ans = min(ans, len(i) + abs(n - int(i)))
print(min(ans, abs(n - 100)))