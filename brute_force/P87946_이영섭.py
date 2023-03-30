def permutations(array, r, prefix=[]):
    for i in range(len(array)):
        if i in prefix: continue
        if r == 1:
            yield [array[i]]
        else:
            prefix.append(i)
            for next in permutations(array, r-1, prefix):
                yield [array[i]] + next
            prefix.pop()

def solution(k, dungeons):
    answer = -1
    bf = list(permutations(list(range(len(dungeons))), len(dungeons), []))
    result = []
    for case in bf:
        temp = k
        cnt = 0
        for val in case:
            if temp >= dungeons[val][0]:
                temp -= dungeons[val][1]
                cnt += 1
            else:
                break
        result.append(cnt)
    answer = max(result)
    return answer

# 문제 접근 방법
# # 중복 순열과 순열 사이에서 굉장히 헷갈렸다.
# # 뽑기 or 안뽑기를 [0, 1] 리스트로 n번 뽑으려 했는데 이렇게 하면 순서가 고정된다는 것을 깨달음
# # 그냥 순열로 순서를 정해서 뽑고 k가 0보다 작아지면 그 케이스를 탈출하는 것으로 해결
# 새로 배운 python
# permutations
# # def permutations(arr, r, prefix):
# #     for i in range(len(arr)):
# #         if i in prefix: continue
# #         if r == 1:
# #             yield [arr[i]]
# #         else:
# #             prefix.append(i)
# #             for next in permutations(arr, r-1, prefix):
# #                 yield [arr[i]] + next
# #             prefix.pop()