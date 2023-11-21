import sys
import math
input = sys.stdin.readline

n,m = map(int,input().split())
ans = [True] * (m+1)
for i in range(2,int(math.sqrt(m))+1):
    if ans[i] == True: # 그 수의 배수 전부 false
        for j in range(i*2,m+1,i):
            ans[j] = False

ans[0],ans[1] = False,False
for i in range(n,m+1):
    if ans[i] == True:
        print(i)