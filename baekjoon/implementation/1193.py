# 백준 - 분수찾기
# 실버 5
import sys

input = sys.stdin.readline


def find_numerator(x):
    n = 1
    while n * (n + 1) < x:
        n += 1
    return n


x = int(input())
if x == 1:
    print("1/1")
    exit()

numerator = find_numerator(x * 2)
sum_to_n = ((numerator) * (numerator - 1) // 2) + 1
dif = x - sum_to_n

if numerator % 2 == 0:
    print(1 + dif, "/", numerator - dif, sep="")
else:
    print(numerator - dif, "/", 1 + dif, sep="")
