import heapq
def solution(n, k, enemy):
    answer = 0
    l = []

    for i, e in enumerate(enemy):
        heapq.heappush(l, (-e, i))

        if n < e:
            if k:
                k -= 1
                max_num, m = heapq.heappop(l)
                # print(max_num, m)
                n -= max_num
                n -= e
                answer += 1
            else:
                break
        else:
            n -= e
            answer += 1
        # print(l, n)
    return answer