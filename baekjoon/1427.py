import sys
input = sys.stdin.readline
num = list(map(int,list(input())[:-1]))
print(*sorted(num,reverse=True),sep="")