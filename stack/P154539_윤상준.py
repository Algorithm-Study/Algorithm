# 문제에서 뒤에서 ~~~~ 이런 식으로 언급되면 stack으로 풀기
def solution(numbers):
    answer = [-1] * len(numbers)
    queue = []
    for idx, num in enumerate(numbers):
        while queue and numbers[queue[-1]] < num:
            answer[queue[-1]] = num
            queue.pop()
        queue.append(idx)
    return answer