def solution(numbers):
    answer = [-1]*len(numbers)
    stack = []
    for i, number in enumerate(numbers):
        while stack and numbers[stack[-1]] < number:
            answer[stack.pop()] = number
        stack.append(i)

    return answer