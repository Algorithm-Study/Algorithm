from collections import deque
def solution(elements):
    answer = set()
    total = sum(elements)
    answer.add(total)
    dq = deque(elements)
    for i in range(1,len(elements)//2+1):
        for _ in range(len(elements)):

            tmp = sum(dq[_] for _ in range(i))
            dq.appendleft(dq.pop())
            answer.add(tmp)
            answer.add(total-tmp)
            
    return len(answer)

# 30배 더 빠른 다른 풀이
# 원순열은 리스트를 한개 더 붙이고
# 인덱스를 나머지로 처리해줘서 돌아가게 구현할수도 있다
# def solution(elements):
#     ll = len(elements)
#     res = set()

#     for i in range(ll):
#         ssum = elements[i]
#         res.add(ssum)
#         for j in range(i+1, i+ll):
#             ssum += elements[j%ll]
#             res.add(ssum)
#     return len(res)
