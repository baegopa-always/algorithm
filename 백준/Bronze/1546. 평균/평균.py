import sys
input = sys.stdin.readline
n = int(input())
subjects = list(map(int, input().split()))
s = 0
for sub in subjects:
    s += sub / max(subjects) * 100
print(s / n)