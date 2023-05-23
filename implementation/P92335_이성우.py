def num2k(n,k):
    ans = ''
    while n:
        ans += str(n%k)
        n //= k
    return ans[::-1]

def isprime(n):
    if n < 2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    num = num2k(n,k)
    tmp = ''
    num_list = []
    
    for letter in num:
        if letter == '0' and tmp != '':
            num_list.append(int(tmp))
            tmp = ''
        else:
            tmp += letter
    num_list.append(int(tmp))

    for n in num_list:
        if isprime(n):
            answer += 1
            
    return answer