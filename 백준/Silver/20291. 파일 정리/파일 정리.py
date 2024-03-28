import sys
from collections import defaultdict
input = sys.stdin.readline
n = int(input())
types = defaultdict(int)
for _ in range(n):
    title, fileType = input().rstrip().split(".")
    types[fileType] += 1
for fileType, count in sorted(types.items(), key=lambda x: x[0]):
    print(fileType, count)