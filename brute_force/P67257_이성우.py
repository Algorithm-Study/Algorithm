from itertools import permutations as pmt
def solution(expression):
    answer = 0
    for operators in pmt(['+','-','*']):
        last = operators[2]
        second = operators[1]
        tmp_last = [f'({last_split})' for last_split in expression.split(last)]
        # print(tmp)
        tmp_answer = []
        for tmp_exp in tmp_last:
            tmp_second = [f'({second_split})' for second_split in tmp_exp.split(second)]
            tmp_answer.append(second.join(tmp_second))
        tmp_answer = abs(eval(last.join(tmp_answer)))
        answer = max(answer, tmp_answer)
    return answer