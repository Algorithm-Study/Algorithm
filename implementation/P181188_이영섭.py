def solution(targets):
    answer = 1
    targets.sort()
    start, end = targets[0][0], targets[0][1]
    for i in range(1, len(targets)):
        if targets[i][0] >= end:
            answer += 1
            start, end = targets[i][0], targets[i][1]
        elif targets[i][1] < end:
            end = targets[i][1]
            
    return answer

# 문제 접근 방법
# # 정렬하여 start가 빠른 것부터 접근
# # 다음 index의 미사일의 시작점이 end 값보다 크면 다른 집합이므로 요격 미사일 + 1
# # 그렇지 않으면서 미사일의 끝점이 end 값보다 작으면 end 값을 바꿔줌