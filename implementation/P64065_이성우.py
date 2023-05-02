from collections import defaultdict
def solution(s):
    # 초기값 설정
    answer = defaultdict(int)
    new_s = s.replace('{','')
    new_s = new_s.replace('}','')
    new_s = list(map(int, new_s.split(',')))

    # 숫자 개수 세기
    for num in new_s:
        answer[num] += 1

    # 숫자 개수의 내림차순으로 정렬하여 반환
    ans = sorted(answer.keys(), key = lambda x : -answer[x])
    return ans