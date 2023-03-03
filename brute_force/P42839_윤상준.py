from itertools import permutations
def solution(numbers):
    answer = []
    for i in range(1,len(numbers)+1):
        temp = list(set(permutations(numbers, i)))
        for j in range(len(temp)):
            answer.append(int(''.join(temp[j])))
    answer = list(set(answer))
    if 1 in answer:
        answer.remove(1)
    if 0 in answer:
        answer.remove(0)
    final = answer.copy()
    #print(final)
    
    for i in range(len(answer)):
        for j in range(2,int(answer[i]**0.5) +1):
            if answer[i] % j == 0:
                print(answer[i])
                final.remove(answer[i])
                break
    return len(final)