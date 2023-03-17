def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []
    for idx, num in enumerate(numbers):
        while len(stack) != 0:
            if stack[-1][1] < num:
                answer[stack[-1][0]] = num
                stack.pop()
            else:
                break
        stack.append([idx, num])
    return answer

# 문제 접근 방식
# # dict로 접근해서 기존 idx와 val을 모두 sort해서 접근하려 했지만
# # n이 100만이라 어떻게 정렬하고 읽어도 O(n^2)이 나와서 포기
# # 일반적인 경우의 수로 시간초과가 나면 stack으로 노선 변경