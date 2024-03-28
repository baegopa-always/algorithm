import sys

input = sys.stdin.readline

alphabetCount = [0 for _ in range(26)]
string = input().rstrip().upper()

for char in string:
    alphabetCount[ord(char) - 65] += 1

ans = max(alphabetCount)
print("?" if alphabetCount.count(ans) > 1 else chr(alphabetCount.index(ans) + 65))
