import sys
input = sys.stdin.readline
n = int(input())
nums = list(map(int,input().split()))
numset = sorted(list(set(nums)))
ans = {}
for i in range(len(numset)):
    ans[numset[i]] = i
for i in nums:
    print(ans[i],end=' ')