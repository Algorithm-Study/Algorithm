from collections import Counter

S = input()
dict_S = Counter(S)
num_0, num_1 = 0, dict_S['1']//2
ans = ''
for i in S:
    if i == '0' and num_0 < dict_S['0']//2:
        num_0 += 1
        ans += i
    elif i == '1':
        if num_1 > 0:
            num_1 -= 1
        else:
            ans += i
print(ans)
