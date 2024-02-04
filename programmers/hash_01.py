# 폰켓몬
## level 1
def solution(nums):
    maximum = len(nums) // 2
    m = len(list(set(nums)))
    if maximum > m:
        return m
    return maximum