n = int(input())
words = []
words_idx = []
for i in range(n):
    words.append(input())
    words_idx.append((words[i], i))
words_idx.sort()

max_l = -1
pre_l = -1

for i in range(1, n):
    now_l = 0
    while now_l < len(words_idx[i - 1][0]) and now_l < len(words_idx[i][0]) and words_idx[i - 1][0][now_l] == words_idx[i][0][now_l]:
        now_l += 1
    if now_l != pre_l:
        pre_l = now_l
        tmp = (words_idx[i - 1][1], words_idx[i][1])
    elif tmp[1] > words_idx[i][1]:
        tmp = (tmp[0], words_idx[i][1])
    if tmp[0] > tmp[1]:
        tmp = (tmp[1], tmp[0])
    if max_l < now_l or (max_l == now_l and ans > tmp):
        max_l = now_l
        ans = tmp

print(words[ans[0]])
print(words[ans[1]])