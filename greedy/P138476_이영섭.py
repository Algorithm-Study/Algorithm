def solution(k, tangerine):
    answer = 0
    num = 0
    data = {}
    for tan in tangerine:
        if tan not in data:
            data[tan] = 1
        else:
            data[tan] += 1
    tan_list = list(sorted(data.items(), reverse = True, key = lambda x:x[1]))
    for i in tan_list:
        num += int(i[1])
        answer += 1
        if num >= k:
            return answer
    return answer

# 문제 접근 방법
# # 들어온 입력 값의 개수를 dict에 담아 파악하고
# # value가 큰 값부터 더하면서 k보다 크면 return