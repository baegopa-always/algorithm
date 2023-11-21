import sys
input = sys.stdin.readline

def gcd(a,b):
    if a == 0:
        return b
    return gcd(b%a,a)

n, s = map(int,input().split())
nums = list(map(int,input().split()))
for i in range(n):
    nums[i] = abs(s-nums[i])

ans = min(nums)
for i in range(n):
    ans = gcd(ans,nums[i])
print(ans)