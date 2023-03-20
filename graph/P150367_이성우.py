def is_tree(s, parent):
    if parent == '0':
        if not all(child == '0' for child in s):
            return False
    if len(s) == 1:
        return True
    center = len(s) // 2
    return is_tree(s[:center], s[center]) and is_tree(s[center + 1:], s[center])


def solution(numbers):
    answer = []
    for number in numbers:
        bs = bin(number)[2:]
        digit = 0  # 포화 이진트리가 되기 위한 문자열의 길이
        for i in range(51):
            digit = 2 ** i - 1
            if digit >= len(bs):
                break
        bs = '0' * (digit - len(bs)) + bs
        answer.append(1 if is_tree(bs, bs[len(bs) // 2]) else 0)
    return answer