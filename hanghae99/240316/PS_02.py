# 프로그래머스 - 베스트 앨범
def solution(genres, plays):
    answer = []
    all_songs = {}
    # 1. 각 장르의 이름으로 딕셔너리를 만든다. ==> key = 장르 이름, value = 해당 장르의 곡 정보 모음
    for data in set(genres):
        all_songs[data] = {}
    # 2. 각 장르 딕셔너리(1에서의 value)에 곡 정보를 추가 한다. ==> key = 곡 번호, value = 곡 플레이 수
    for i, genre in enumerate(genres):
        all_songs[genre][i] = plays[i]
    # 3. 곡 플레이 수의 합을 기준으로 내림차순하여 장르 정렬
    all_songs = sorted(all_songs.items(), key = lambda x:sum(x[1].values()), reverse=True)
    # 4. 장르 딕셔너리에서 곡 플레이 수를 기준으로 내림차순 정렬 후, 플레이 수가 높은 두 곡의 번호를 answer에 담음
    for genre, songs in all_songs:
        songs = sorted(songs.items(), key = lambda x:-x[1])
        for song in songs[:2]:
            answer.append(song[0])
    return answer