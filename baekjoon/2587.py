nums = [int(input()) for _ in range(5)]
for i in range(5):
    for j in range(i+1,5):
        if nums[i] >= nums[j]:
            tmp = nums[j]
            nums[j] = nums[i]
            nums[i] = tmp
print(sum(nums)//5,nums[2],sep="\n")