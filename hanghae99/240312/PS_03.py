# 프로그래머스 - 큰 수 만들기
def solution(number, k):
    stack = []
    for n in number:
        while stack and stack[-1] < n and k > 0:
            stack.pop()
            k -= 1
        stack.append(n)
    while k != 0:
        stack.pop()
        k -= 1
    # if k != 0
    # stack = stack[:-k]
    number = ''.join(stack)
    return number