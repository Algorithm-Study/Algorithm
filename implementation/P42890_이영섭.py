from itertools import combinations

def solution(relation):
    answer = 0
    leng = list(range(len(relation[0])))
    candidate_key = []
    for i in range(1, len(relation[0])+1):
        if len(leng) < i:
            break
        bf = list(combinations(leng, i))
        for case in bf:
            ns = []
            for r in relation:
                key = [r[c] for c in case]
                if key in ns:
                    break
                else:
                    ns.append(key)
            else:
                for ck in candidate_key:
                    if set(ck).issubset(set(case)):
                        break
                else:
                    candidate_key.append(case)
    return len(candidate_key)

# 문제 접근 방법
# # 모든 케이스를 봐야한다는 것까지는 생각했으나 이후 구현을 헤맴
# # 각 열에서 key 값을 먼저 찾고 겹치는 것이 있으면 중복이므로 넘어감
# # 만약 모두 구분이 된다면 이미 생성된 후보키 집합에서 값을 찾아 부분집합인지 검사
# 새로 배운 python
# # 부분집합인지 확인할 수 있는 method(set과 set으로 사용 가능)
# # set 내부에 list를 넣기 위해서는 tuple로 변경하여 넣을 수 있다.