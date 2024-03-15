# 프로그래머스 - 혼자 놀기의 달인
def solution(cards):
    answer = 0
    # 1. s = 그룹의 상자 개수
    # 2. check[n] = 0일 경우 한번도 열지 않은 상자, 1일 경우 열어본 상자
    # 3. 열어본 상자를 다시 확인할 경우 현재까지 돌았던 상자 개수를 box에 넣음
    # 4. 정렬 후 가장 큰 값 둘 곱하고 리턴 (길이가 1 이하 일 경우 곱이 불가하므로 0 반환)
    check = [0 for _ in range(len(cards))]
    box = []
    for i in range(len(cards)):
        s = 0
        for _ in range(len(cards)):
            if check[i] == 0:
                check[i] = 1
                s += 1
                i = cards[i] - 1
            else:
                box.append(s)
                break
    box.sort()
    if len(box) < 2:
        return 0
    answer = box[-1] * box[-2]
    return answer