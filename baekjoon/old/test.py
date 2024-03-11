import math
def solution(n, k):
    # n을 k 진수로 바꾼다.
    # 하나씩 stack에 넣는다. 0일 때 stack에 숫자 있는 경우 prime인지 확인 후 초기화, 숫자 없을 경우 continue
    # 해당할 경우 count 증가
    # 마지막 stack 비어 있는 지 확인
    answer = 0
    stack = []
    num = ''
    while n:
        num += str(n % k)
        n = n // k
    
    for i in num:
        if i == '0' and stack:
            x = int(''.join(map(str,stack)))
            if isPrime(x):
                answer += 1
        else:
            stack.append(i)
    return answer

def isPrime(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

t = solution(437674,3)
print(t)