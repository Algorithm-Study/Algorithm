def solution(picks, minerals):
    pick = ['diamond','iron', 'stone']
    answer = 0
    trials = []
    max_picks = sum(picks)
    pick_list = []
    for idx,p in enumerate(picks):
        for i in range(p):
            pick_list.append(pick[idx])
    count = 0
    # 채굴할 수 있는 만큼 구간 잘라서 가져오기
    for i in range(0, len(minerals), 5):
        if count == max_picks:
            break
        temp = minerals[i:i+5]
        d_val = temp.count('diamond')
        i_val = temp.count('iron')
        s_val = temp.count('stone')
        trials.append([d_val, i_val, s_val])
        count +=1
    s_trials = sorted(trials, key = lambda x : (-x[0], -x[1], -x[2]))
    for p, s in zip(pick_list, s_trials):
        #print(s)
        #print(answer)
        if p == 'diamond':
            answer += s[0] + s[1] + s[2]
        elif p == 'iron':
            answer += 5*s[0] + s[1] + s[2]
        else:
             answer += 25*s[0] + 5*s[1] + 1*s[2]
    return answer