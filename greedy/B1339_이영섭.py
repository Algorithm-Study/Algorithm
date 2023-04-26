from collections import defaultdict

N = int(input())
word = [input() for _ in range(N)]
word.sort(key=lambda x: [-len(x), x])
word_dict = defaultdict(int)
max_len = max(map(len, word))
for idx in range(N):
    leng = len(word[idx])
    for i in range(leng):
        word_dict[word[idx][leng - 1 - i]] += 10 ** i

word_list = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)
num, ans = 9, 0
for wl in word_list:
    ans += wl[1] * num
    num -= 1
print(ans)

# 문제 접근 방법
# # 각 알파벳이 몇 번째 자리에 얼마나 들어가 있는지 dict로 표현하고
# # 값이 큰 알파벳으로 정렬하여 9부터 차례로 숫자를 부여