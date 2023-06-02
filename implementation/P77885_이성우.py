def solution(numbers):
    answer = []

    for num in numbers:
        bin_num = '0' + bin(num)[2:]
        idx = bin_num.rfind('0')
        bin_num = list(bin_num)
        
        if num % 2 == 0:
            bin_num[-1] = '1'
        
        else:
            bin_num[idx], bin_num[idx+1] = bin_num[idx+1], bin_num[idx]
        
        answer.append(int(''.join(bin_num), 2))
    return answer