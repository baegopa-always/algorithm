# 백준 - 별 찍기 - 8
# 브론즈 3
import sys
input = sys.stdin.readline

n = int(input())

for i in range(1, n):
    print("*" * i, " " * (n-i) * 2, "*" * i, sep = "")

print("*" * n * 2)

for i in range(n-1, 0, -1):
    print("*" * i, " " * (n-i) * 2, "*" * i, sep = "")