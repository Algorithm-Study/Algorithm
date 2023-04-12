def solution(scores):
    answer = 1
    wanho = scores[0]
    wanho_sum = sum(wanho)
    scores.sort(key= lambda x: [-x[0], x[1]])
    max_df = 0
    for s in scores:
        if wanho[0] < s[0] and wanho[1] < s[1]:
            return -1
        if max_df <= s[1]:
            if wanho_sum < s[0] + s[1]:
                answer += 1
            max_df = s[1]
    return answer

# 문제 접근 방법
# # n이 10만 이므로 nlogn 이하의 알고리즘이 필요
# # 정렬을 해주되, 앞은 내림차순으로 하여 뒷 번호가 작게 만들고
# # 뒤는 오름차순으로 하여 max값만 취해줌(max보다 작으면 두 점수 작은 사원이 무조건 하나는 있으므로)