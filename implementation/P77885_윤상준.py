def solution(numbers):
    max_length = len(bin(1_000_000_000_000_000_000)[2:])
    answer = []
    for num in numbers:
        standard = list('0' * (max_length - len(bin(num)[2:])) + bin(num)[2:])[::-1]
        for idx, s in enumerate(standard):
            if s == '0':
                standard[idx] = '1'
                break
            elif s == '1' and standard[idx+1] == '0':
                standard[idx] = '0'
                standard[idx+1] = '1'
                break
        answer.append(int('0b' + ''.join(standard[::-1]),2))
    return answer

# 이진수로 변환해서 일일히 찾는 방법은 시간초과
# 2개 이하로 다른 비트에 대한 규칙을 찾아서 해야 시간내 문제 풀이 가능