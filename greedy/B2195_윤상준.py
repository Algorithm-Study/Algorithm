s = input()
p = input()
p_idx, answer = 0,0
while p_idx < len(p):
    max_length, streak, s_idx = 0,0,0
    while s_idx < len(s) and streak + p_idx < len(p):
        if p[p_idx + streak] == s[s_idx]:
            streak += 1
            max_length = max(max_length, streak)
        else:
            streak = 0
        s_idx += 1
    p_idx += max_length
    answer += 1
print(answer)