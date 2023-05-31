from collections import defaultdict

N = int(input())
num = list(map(int, input().split()))
num.sort()
num_dict = defaultdict(int)
ans_dict = defaultdict(int)
for n in num:
    num_dict[n] += 1

for i in range(len(num)):
    for j in range(i+1, len(num)):
        if num[i] + num[j] in num_dict.keys():
            if num[i] == 0 and num_dict[num[i] + num[j]] < 2:
                continue
            elif num[j] == 0 and num_dict[num[i] + num[j]] < 2:
                continue
            elif num[i] == 0 and num[j] == 0 and num_dict[0] < 3:
                continue
            ans_dict[num[i] + num[j]] += 1

ans = 0
for n in num:
    if n in ans_dict:
        ans += 1
print(ans)