import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))
ans = []
for i in range(n):
    notFound = True
    for j in range(i+1,n):
        if nums[i] < nums[j]:
            notFound = False
            ans.append(nums[j])
            break
    if notFound:
        ans.append(-1)
print(*ans)