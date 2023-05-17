from collections import defaultdict
def solution(genres, plays):
    total_dict = defaultdict(list)
    answer = []
    for gen, play, idx in zip(genres, plays, range(len(genres))):
        total_dict[gen].append([play, idx])

    sorted_genres = sorted(total_dict, key = lambda x : -sum(t[0] for t in total_dict[x]))
    for t in sorted_genres:
        tmp = sorted(total_dict[t], key = lambda x : -x[0])
        answer += [x[1] for x in tmp][:2]

    return answer