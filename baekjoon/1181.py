import sys
input = sys.stdin.readline
n = int(input())
words = list(set([input()[:-1] for _ in range(n)]))
words.sort(key=lambda x:(len(x),x))
for i in words:
    print(i)