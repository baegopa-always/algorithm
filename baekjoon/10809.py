import sys
input = sys.stdin.readline

alphabets = [-1] * 26

string = input().rstrip()

for i, x in enumerate(string):
    k = ord(x) - 97
    if alphabets[k] == -1:
        alphabets[k] = i

print(*alphabets)