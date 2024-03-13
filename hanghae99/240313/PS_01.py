# 프로그래머스 - 호텔 대실
def solution(book_time):
    answer = 0
    timeTable = []
    # 1. 각 예약을 분으로 변환
    # 2. 방 사용 시작 시점을 1, 사용 종료 시점을 0으로 하여 각 예약의 시작, 종료와 함께 타임테이블에 넣는다.
    # 3. 오름차순으로 정렬 -> 시간 순 나열
    # 4. 방을 사용했을 경우 rooms (현재 사용 중인 방의 개수) 를 더한다
    # 5. 방 사용 종료 시 rooms 에서 뺀다.
    # 6. (4), (5) 반복하며 최대로 방을 사용했을 때 값이 필요한 방의 개수
    for start, end in book_time:
        timeTable.append([timeToInt(start), 1])
        timeTable.append([timeToInt(end)+10, 0])
    timeTable.sort()
    rooms = 0
    for time, status in timeTable:
        if status == 1:
            rooms += 1
        else:
            rooms -= 1
        answer = max(answer, rooms)
    return answer

def timeToInt(time):
    return int(time[:2]) * 60 + int(time[3:])

x = [["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]
out = solution(x)
print(out)