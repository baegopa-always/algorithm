#######################################################################################################
# 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
# 아래 표준 입출력 예제 필요시 참고하세요.
# 표준 입력 예제
# a = int(input())                                                  # 정수 1개 입력받는 예제
# b, c = map(float, input().split())                                # 실수 2개 입력받는 예제
# var = input()                                                     # 문자열 1개 입력받는 예제
# A = [int(num) for num in input().split()]                         # 1차원 배열에 정수 입력받는 예제
# B = [[int(num) for num in input().split()] for _ in range(row)]   # 2차원 배열에 정수 입력받는 예제
#######################################################################################################
# 표준 출력 예제
# a = 0
# b = 1.0
# c = 2.0
# var = "ABCDEFG"
# N = 10
# A = [0] * N
# B = [[1] * N for _ in range(N)]
# print(a)                                                          # 정수 1개 출력하는 예제
# print(b, c)                                                       # 실수 2개 출력하는 예제
# print(var)                                                        # 문자열 1개 출력하는 예제
# print(' '.join(str(num) for num in A))                            # 1차원 배열 출력하는 예제
# print('\n'.join(' '.join(str(num) for num in N) for N in B))      # 2차원 배열 출력하는 예제
#######################################################################################################

# import sys

'''
   아래의 stdin 함수는 sample_input.txt 를 read only 형식으로 연 후,
   앞으로 표준 입력(키보드) 대신 sample_input.txt 파일로부터 읽어오겠다는 의미의 코드입니다.
   여러분이 작성한 코드를 테스트 할 때, 편의를 위해서 sample_input.txt에 입력을 저장한 후,
   stdin 함수를 이용하면 이후 input 을 수행할 때 표준 입력 대신 파일로부터 입력을 받아올 수 있습니다.
   따라서 테스트를 수행할 때에는 아래 주석을 지우고 이 함수를 사용하셔도 좋습니다.
   단, 채점을 위해 코드를 제출하실 때에는 반드시 stdin 함수를 지우거나 주석 처리 하셔야 합니다.
'''
# sys.stdin = open('sample_input.txt', 'r')


'''
  여러 개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
'''

T = int(input())
for test_case in range(1, T + 1):
    #######################################################################################################
    n, a, b = map(int, input().split())
    score = list(map(int, input().split()))
    score.sort()
    ans = 0
    all_scores = [0 for _ in range(1001)]

    # 중그룹에 x 점수만 넣었을때 x+a 점수도 넣엇을때 인원이 최소면서 최대가 되도록
    # 무조건 3그룹이 나오는 숫자들
    for num in score:
        all_scores[num] += 1
    all_scores[min(score)] = 0
    all_scores[max(score)] = 0
    for i in range(a, b+1):
        for j in range(1, 1001, i):
            if len(all_scores[j:j+i]) >= a and len(all_scores[j:j+i]) <= b:
                ans = max(ans,len(all_scores[j:j+i]))
    # 1 1 2 2 3 3 4
    # 2 2 3 3 4
    # 2 2 3 3 3
    #######################################################################################################

    # 표준출력(화면)으로 답안을 출력합니다.
    print(f'#{test_case} {ans}')
