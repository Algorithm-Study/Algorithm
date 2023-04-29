N = int(input())
word = list(input())
ans = 0
for _ in range(N-1):
    new_word = word[:]
    temp = input()
    cor = 0
    for tp in temp:
        if tp in new_word:
            new_word.remove(tp)
        else:
            cor += 1
    if cor < 2 and len(new_word) < 2:
        ans += 1
print(ans)

# 문제 접근 방법
# # 처음에는 dict로 차이점을 구하려 했으나
# # 실패하여 list를 복사하여 새로운 문자열과 비교하여 같으면 복사된 문자열에서 제거하고
# # 그렇지 않으면 cor 값을 늘려줘서 기존 문자열과 다른 개수를 구했다.