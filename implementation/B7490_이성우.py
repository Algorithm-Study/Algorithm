from itertools import product
TC = int(input())
for tc in range(TC):
    n = int(input())
    operator = [' ', '+', '-']
    
    for opers in product(operator, repeat=n-1):
        exp = '1'
        for op, num in zip(opers, range(2,n+1)):
            exp += op + str(num)
        n_exp = exp.replace(' ','')
        if eval(n_exp) == 0:
            print(exp)
    if tc < TC-1:
        print()
