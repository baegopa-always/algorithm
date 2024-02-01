import sys
input = sys.stdin.readline

nums = [True] * 1000001

# 1,000,000 까지 소수 전부 구하기
for i in range(2,1001):
    if nums[i] == True:
        for j in range(i*2,1000001,i):
            nums[j] = False
nums[0],nums[1] = False, False

while True:
    n = int(input())
    if n == 0 :
        break
    possible = False
    for i in range(3,n,2):
        if nums[i] and nums[n-i]:
            possible = True
            break
    if possible:
        print('%d = %d + %d' %(n,i,n-i))
    else:
        print("Goldbach's conjecture is wrong.")
