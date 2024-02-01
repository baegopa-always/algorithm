n = int(input())
nums = [int(input()) for _ in range(n)]
for i in range(n):
    for j in range(i+1,n):
        if nums[i] >= nums[j]:
            tmp = nums[j]
            nums[j] = nums[i]
            nums[i] = tmp
for x in nums:
    print(x)