expression = input()
minus_split = expression.split('-')
answer = ''

for ex in minus_split:
    
    tmp = ''
    for num in ex.split('+'):
        tmp += f'+{int(num)}'
        
    answer += f'-({tmp[1:]})'
    
print(eval(answer[1:]))