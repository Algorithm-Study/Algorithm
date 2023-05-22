def solution(n, k):
    answer = 0
    val_list = change_notation(n,k)
    for i in val_list:
        if i == '':
            continue
        i = int(i)
        if int(i) > 1 and is_prime(i):
            answer = answer + 1
    return answer
def change_notation(n,k):
    ch = ""
    while n>0:
        ch = str(n%k) + ch
        n = n//k
    val_list = ch.split('0')
    while '' in val_list:
        val_list.remove('')
    return val_list
def is_prime(i):
    for j in range(2,int((i+ 1)**0.5+1)):
        if i%j==0:
            return False
    return True