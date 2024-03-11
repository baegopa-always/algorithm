def solution(numbers):
    answer = []
    stack = []
    # number 리버스
    # 1. 스택 맨위의 수보다 큰 수 나오면 스택에서 뺀다
    # 2. 사이즈 0일 경우 ans에 -1 넣고 stack에 그 숫자 넣기
    # 3. 작으면 맨위숫자 ans 넣고 작은 숫자는 stack에 넣기
    numbers = numbers[::-1]
    for i in numbers:
        while stack and stack[-1] <= i:
            stack.pop()
        if stack:
            answer.append(stack[-1])
            stack.append(i)
        else:
            answer.append(-1)
            stack.append(i)
    answer = answer[::-1]
    return answer