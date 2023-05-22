import math

def is_prime(num):
    if num == 0 or num == 1:
        return 0
    for i in range(2, int(float(math.sqrt(num))) + 1):
        if num % i == 0:
            return 0
    return 1

def ntok(n, k):
    ans = ''
    while n > 0:
        ans += str(n % k)
        n //= k
    return ans[::-1]

def solution(n, k):
    answer = 0
    new_n = ntok(n, k)
    keys = new_n.split('0')
    for key in keys:
        if key == '':
            continue
        elif is_prime(int(key)):
            answer += 1
            
    return answer