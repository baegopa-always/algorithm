# 프로그래머스 - 디펜스 게임
from heapq import heappush, heappop
def solution(n, k, enemy):
    # 1. 힙 응용
    heap = []
    answer = 0
    for x in enemy:
        heappush(heap, x)
        if len(heap) > k:
            n -= heappop(heap)
        if n < 0:
            return answer
        answer += 1
    return answer