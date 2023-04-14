def num_of_one(num):
    gob = [0, 1, 2, 2, 3]
    flag = False
    temp = ''
    for i in range(len(num)):
        if flag == True:
            temp += '0'
        else:
            temp += num[i]
        if num[i] == '2':
            flag = True
    sum = 0
    for i in range(len(num)-1, -1, -1):
        sum += 4**(len(num)-1-i)*gob[int(temp[i])]
    return sum

def to_penta(num):
    temp = ''
    while num > 0:
        temp += str(num % 5)
        num //= 5
    return temp[::-1]

def solution(n, l, r):
    answer = 0
    cantor = '1'
    penta_l = to_penta(l-1)
    penta_r = to_penta(r)
    ll = num_of_one(penta_l)
    rr = num_of_one(penta_r)
    return rr - ll

# 문제 접근 방법
# # 5**(n-1)부분이 5**(n)