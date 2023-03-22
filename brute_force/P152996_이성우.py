from collections import defaultdict

def solution(weights):
    answer = 0
    weights_dict = defaultdict(int)
    # ratios = [1/1, 2/4, 4/2, 3/2, 2/3, 4/3, 3/4]
    for weight in weights:
        answer += weights_dict[weight] + weights_dict[weight*2] + weights_dict[weight*1/2] + weights_dict[weight*3/2] + weights_dict[weight*2/3] + weights_dict[weight*3/4] + weights_dict[weight*4/3]
        weights_dict[weight] += 1
    # print(weights_dict)
    return answer