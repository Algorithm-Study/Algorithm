def solution(genres, plays):
    song_genre = list(set(genres))
    total_play = []
    answer = []
    # 각 장르별 총 플레이 횟수 구하기
    for i in range(len(song_genre)):
        temp = 0
        for j in range(len(genres)):
            if song_genre[i] == genres[j]:
                temp += plays[j]
        total_play.append((song_genre[i], temp))
    total_play.sort(key = lambda x: -x[1])
    # 각 곡별 정보 리스트 만들기
    song_features = []
    for i in range(len(genres)):
        song_features.append((genres[i], i, plays[i]))
    song_features.sort(key = lambda x: (x[0],-x[2]))
    #print(song_features)
    #print(total_play)
    #베스트 추출
    for i in range(len(total_play)):
        best_genre = total_play[i][0]
        count = 0
        for j in range(len(song_features)):
            if count >=2:
                break
            if best_genre == song_features[j][0]:
                answer.append(song_features[j][1])
                count+=1
    return answer
