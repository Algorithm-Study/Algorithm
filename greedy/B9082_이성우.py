for _ in range(int(input())):
    n = int(input())
    mine_num = [1] + list(map(int, list(input()))) + [1]
    mine = list(input())
    answer = 0
    for i in range(1, n+1):
        if mine_num[i-1] != 0 and mine_num[i] != 0 and mine_num[i+1] != 0:
            mine_num[i-1] -= 1
            mine_num[i] -= 1
            mine_num[i+1] -= 1
            answer += 1
    print(answer)