import sys
input = sys.stdin.readline
string = input().rstrip()
wordCount = {}
for i in range(1, len(string) + 1):
    for j in range(len(string) - i + 1):
        wordCount[string[j : j + i]] = 0
print(len(wordCount.keys()))