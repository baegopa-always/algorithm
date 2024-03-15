# 프로그래머스 - 요격 시스템
def solution(targets):
    answer = 0
    # 1. 공격 종료 시점을 기준으로 정렬 => 공격이 빨리 끝나는 것부터 확인하도록
    # 2. 요격 시작점 +0.5가 이전 요격 종료점 보다 높다 == 겹치지 않는다
    # 3. (2)에 해당하면 카운트 추가하고, 확인해야할 요격 종료점을 현재 요격 종료로 업데이트
    targets = sorted(targets, key = lambda x:x[1])
    end = 0
    for s, e in targets:
        if s + 0.5 > end:
            answer += 1
            end = e
    return answer