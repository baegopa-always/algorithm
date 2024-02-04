# 잃어버린 괄호
## 실버 2
# 55-50+40, 00009-00009
# - 만나면 그냥 뺀다 (마지막 연산 상관없이), + 만나면 앞 연산에 -가 한번이라도 있었을 경우 뺸다.
import sys
input = sys.stdin.readline

exp = list(input())
exp += '-'
nums = []
lastOp = '+'
ans = 0
for x in exp:
    if (x == '+' or x == '-') and lastOp == '+':
        num = int("".join(nums))
        while nums:
            nums.pop()
        ans+=num
        lastOp = x
    elif x == '-' or x == '+':
        num = int("".join(nums))
        while nums:
            nums.pop()
        ans-=num
    else:
        nums.append(x)
print(ans)