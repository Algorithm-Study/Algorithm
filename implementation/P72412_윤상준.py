# 4 X 3 X 3 X 3 = 108
from bisect import bisect_left
from itertools import product
def solution(info, query):
    answer = []
    info2code = [[]for _ in range(108)]
    categories = list(product((0, 1), repeat=4))
    query2code = []
    lang = ['cpp', 'java', 'python', '-']
    pos = ['backend', 'frontend', '-']
    career = ['junior', 'senior', '-']
    food = ['chicken', 'pizza', '-']
    for i in info:
        l,p,c,f, score = i.split()
        indexes = []
        for cat in categories:
            idx = 0
            if cat[0] == 0:
                idx += 27*lang.index('-')
            else:
                idx += 27* lang.index(l)
            if cat[1] == 0:
                idx += 9*pos.index('-')
            else:
                idx += 9* pos.index(p)
            if cat[2] == 0:
                idx += 3*career.index('-')
            else:
                idx += 3* career.index(c)
            if cat[3] == 0:
                idx += food.index('-')
            else:
                idx += food.index(f)
            indexes.append(idx)
        for idx in indexes:
            info2code[idx].append(int(score))
    sort_info2code = []
    for i in info2code:
        i.sort()
        sort_info2code.append(list(i))
    for q in query:
        q = q.replace('and ', '')
        l,p,c,f, score = q.split()
        idx = 27 * lang.index(l) + 9* pos.index(p) + 3* career.index(c) + food.index(f)
        after = bisect_left(sort_info2code[idx], int(score))
        answer.append(len(sort_info2code[idx]) - after)
    return answer