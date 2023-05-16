from collections import defaultdict

def solution(genres, plays):
    answer = []
    genre = defaultdict(int)
    music = defaultdict(list)
    for idx, (g, n) in enumerate(zip(genres, plays)):
        genre[g] += n
        music[g].append((n, idx))
    sorted_genre = sorted(genre.items(), key = lambda x:x[1], reverse=True)
    for sg in sorted_genre:
        sorted_music = sorted(music[sg[0]], key = lambda x: (-x[0], x[1]))
        for sm in sorted_music[0:2]:
            answer.append(sm[1])
    return answer