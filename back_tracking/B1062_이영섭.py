import string
from itertools import combinations

N, K = map(int, input().split())

data = []
char_set = set()
essential_set = {'a', 'c', 'i', 'n', 't'}
alp_dict = dict.fromkeys(string.ascii_lowercase, 0)
for i in essential_set:
    alp_dict[i] = 1

for _ in range(N):
    ip = input()[4:-4]
    data.append(ip)
    char_set.update(set(list(ip)))
char_set -= essential_set

if K < 5:
    print(0)
elif len(char_set) <= K - 5:
    print(N)
else:
    case = combinations(char_set, K - 5)
    ans = 0
    for cs in case:
        sum = 0
        for ch in cs:
            alp_dict[ch] = 1

        for dt in data:
            for val in list(dt):
                if alp_dict[val] == 0:
                    break
            else:
                sum += 1

        if sum >= ans:
            if sum == N:
                print(N)
                exit()
            ans = sum

        for ch in cs:
            alp_dict[ch] = 0
    print(ans)
