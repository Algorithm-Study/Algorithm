def solution(n, m, section):
    idx = 0
    answer = 0
    for pt in section:
        if idx == 0:
            idx = pt
            answer += 1
            continue
        else:
            if pt > idx + m - 1:
                idx = pt
                answer += 1
    return answer

# 문제 접근 방식
# # 순회하면서 첫번째 번호부터 페인트 칠하고 범위 벗어나면 횟수 +1