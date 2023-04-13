def solution(sequence, k):
    answer = []
    arr = [0]
    for i in range(len(sequence)):
        arr.append(arr[i]+sequence[i])
    min_len = 1000000001
    point = [1000001, 1000001]
    end = len(arr)-1
    start = len(arr)-2
    while True:
        if arr[end] - arr[start] > k:
            end -= 1
        # print(start, end, arr[start], arr[end])
        elif arr[end] - arr[start] == k:
            if min_len > end - start:
                point = [start, end]
                min_len = end - start
            elif min_len == end - start:
                if point[1] > start:
                    point = [start, end]
                    min_len = end - start
            if start > 0:
                start -= 1
            if end > 0:
                end -= 1
        else:
            if start > 0:
                start -= 1
            elif start == 0:
                break
    answer = [point[0], point[1]-1]
    return answer

# 문제 접근 방법
# # 자신 앞까지의 배열을 모두 더한 값을 저장한 arr라는 배열을 만들어서
# # start, end 투포인터를 활용하여 조건에 맞는 수열을 찾음