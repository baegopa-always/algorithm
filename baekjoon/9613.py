import sys
input = sys.stdin.readline

def gcd(a,b):
    if a == 0:
        return b
    return gcd(b%a,a)

for _ in range(int(input())):
    nums = list(map(int,input().split()))
    ans = 0
    for i in range(1,nums[0]+1):
        for j in range(i+1,nums[0]+1):
            ans += gcd(nums[i],nums[j])
    print(ans)