# 프로그래머스 - 숫자 카드 나누기
def solution(arrayA, arrayB):
    # 1. A의 최대 공약수 구하기
    # 2. B의 원소를 나눌 수 있는지
    # 3. (2)에 답이 없다면 반대의 경우 확인
    answer = get(arrayA, arrayB)
    answer = max(answer, get(arrayB, arrayA))
    return answer

def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

def get(arrayA, arrayB):
    result = arrayA[0]
    for x in arrayA:
        result = gcd(result, x)
    if result == 0:
        return result
    for x in arrayB:
        if x % result == 0:
            return 0
    return result