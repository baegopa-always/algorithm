# 백준 - 문자열 반복
# 브론즈 2
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    r, s = input().split()
    for t in s:
        print(t * int(r), end="")
    print()