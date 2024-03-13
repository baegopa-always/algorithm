def solution(order):
    answer = 0
    stack = []
    cur = 0
    # 1. i는 기존 택배 번호
    # 2. order[cur] = 현재 찾아야 할 택배 상자 번호
    # 3. 스택의 최상단 요소가 (2) 에 해당한다면 스택에서 뺀다.
    for i in range(1, len(order) + 1):
        stack.append(i)
        while stack and stack[-1] == order[cur]:
            answer += 1
            cur +=1
            stack.pop()
    return answer