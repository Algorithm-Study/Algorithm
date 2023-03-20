# 맨 마지막 층 노드에만 더미 노드가 가능하니 위 노드에 0이 있는 경우 모두 불가능한 케이스 
# 더미->더미 연속은 가능
from math import log2
def is_possible(root, tree):
    if root == '0':
        if sum(map(int, tree)) != 0:
            return False
    if len(tree) == 1:
        return True
    child_root = len(tree)//2
    return is_possible(tree[child_root], tree[:child_root]) and is_possible(tree[child_root], tree[child_root+1:])
def solution(numbers):
    answer = []
    bin_list = []
    possible_length = [1,3,7,15]
    #이진수로 변환
    for num in numbers:
        dec2bin = bin(num)[2:]
        fullnode = 2 ** (int(log2(len(dec2bin)))+1) - 1
        bin_list.append('0'*(fullnode - len(dec2bin))+ dec2bin)
    #print(bin_list)
    for b in bin_list:
        result = 1 if is_possible(b[len(b)//2], b) else 0
        answer.append(result)
    return answer