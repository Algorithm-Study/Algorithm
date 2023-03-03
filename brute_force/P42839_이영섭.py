from itertools import permutations
import math

def is_prime_number(number):
    # 2부터 제곱근까지 나눠지는 것이 없으면 소수
    for i in range(2, int(math.sqrt(number))+1):
        if number % i == 0:
            return False
    return True

def solution(numbers):
    data = []
    permute = []
    value = []
    answer = 0
    # 입력값을 list로 변경
    for i in range(len(numbers)):
        data.append(numbers[i])
    # list로 순열 생성
    for i in range(1, len(data)+1):
        permute.extend(list(permutations(data, i)))
    # 정수로 변경
    for per in permute:
        value.append(int(''.join(per)))
    # 중복 제거
    value = list(set(value))
    # val 값이 1보다 크면서 소수이면 answer 값 증가
    for val in value:
        if val > 1 and is_prime_number(val) == True:
            answer += 1
    
    return answer

# 문제 접근 방법
# # number의 길이가 7 이하이고 0~9까지의 숫자들로 이루어져 있으므로 완전탐색으로 해결 가능
# # 수를 나열하는 순서가 중요하므로 순열로 접근
# 새로 배운 python
# # itertools의 permutations, combinations, product, combinations_with_replacement를 활용하면
# # 쉽게 결과를 list로 얻을 수 있음
# # result = list(function(data, x))