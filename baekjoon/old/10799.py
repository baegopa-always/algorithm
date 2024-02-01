# 멀리 떨어진 괄호 쌍 안에서 붙은 쌍 개수+1 만큼 나옴
# 1 (((11)(1)1))(1) 3, 쌍 붙으면 1로. 옆에 숫자인가 닫괄호인가 확인
import sys
input = sys.stdin.readline
segments = input()
stack = []
ans = 0
for i in segments:
    stack.append(i)
    
    print(stack)
print(ans)