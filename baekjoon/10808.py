import sys
input = sys.stdin.readline

s = input().rstrip()
alphabets = [0] * 26

for x in s:
    alphabets[ord(x)-97] +=1
print(*alphabets)