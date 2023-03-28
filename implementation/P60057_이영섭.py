def solution(s):
    answer = 1001
    ans = [[] for _ in range(len(s)//2+1)]
    again_num = 1
    if len(s) == 1:
        return 1
    for i in range(1, len(s)):
        if s[i-1] == s[i]:
            again_num += 1
        else:
            if again_num != 1: ans[1].append(str(again_num))
            ans[1].append(s[i-1])
            again_num = 1
    if again_num != 1: ans[1].append(str(again_num))
    ans[1].append(s[-1])
    for i in range(2, len(s)//2+1):
        again_num = 1
        before_val = 'start'
        temp = s[0]
        change = False
        for j in range(1, len(s)):
            # print(f"temp: {temp}")
            if j%i == 0 and temp == before_val:
                again_num += 1
                temp = s[j]
                # print(1, end=" ")
            elif j%i == 0 and temp != before_val:
                if again_num != 1: ans[i].append(str(again_num))
                ans[i].append(temp)
                before_val = temp
                temp = s[j]
                again_num = 1
                # print(2, end=" ")
            else:
                temp += s[j]
                # print(3, end=" ")
        # print()
        if temp != '':
            if temp == before_val:
                again_num += 1
                ans[i].append(str(again_num))
            else:
                if again_num != 1: ans[i].append(str(again_num))
                ans[i].append(temp)
    for i in ans[1:]:
        # print(i, ''.join(i), len(''.join(i)), answer)
        if answer > len(''.join(i)):
            answer = len(''.join(i))
    return answer

# 문제 접근 방식
# # 문자열을 2로 나눈 값까지가 문자열 개수의 단위를 나타냄
# # 한 개 씩 나눴을 때와 나머지를 나눠서 접근