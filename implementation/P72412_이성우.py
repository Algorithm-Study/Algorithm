import bisect, itertools, collections

def solution(info, query):
    infomap = collections.defaultdict(list)
    binarys = list(itertools.product((True, False), repeat=4))
    for inf in info:
        inf = inf.split()
        for binary in binarys:
            key = ''.join([inf[i] if binary[i] else '-' for i in range(4)]) 
            infomap[key].append(int(inf[4]))

    for k in infomap.keys():
        infomap[k].sort()

    answers = []
    for q in query:
        l,_,p,_,c,_,f, point = q.split()
        key = ''.join([l,p,c,f])
        i = bisect.bisect_left(infomap[key], int(point))
        answers.append(len(infomap[key]) - i)

    return answers
# def solution(info, query):
#     answer = 0
#     answers = []
#     for query_line in query:
#         q = query_line.split()
#         q_lang, q_job, q_career, q_food, q_point = q[0], q[2], q[4], q[6], int(q[7])
        
#         for info_line in info:
#             i_lang, i_job, i_career, i_food, i_point = info_line.split()
#             if q_lang == i_lang or q_lang == '-':
#                 if q_job == i_job or q_job == '-':
#                     if q_career == i_career or q_career == '-':
#                         if q_food == i_food or q_food == '-':
#                             if q_point <= int(i_point):
#                                 answer += 1
#         else:
#             answers.append(answer)
#             answer = 0
#     return answers