# 프로그래머스 - 점 찍기
import math
def solution(k, d):
    answer = 0
    dist = d ** 2
    # 1. k 단위로 증가하는 x 값에 따라 가질 수 있는 최대 y 값 계산
    # 2. 최대 y 값에 k 단위로 찍을 수 있는 점의 개수를 구하고 누적합
    for x in range(0, d + 1, k):
        y = math.sqrt(dist - (x ** 2))
        answer += y // k + 1
    return answer