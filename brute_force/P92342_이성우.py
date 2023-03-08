from itertools import product
def solution(n, info):
    info.reverse()
    ans = [-1]
    max_point = 0
    for win_lose in product((True, False), repeat=11):
        current_arrow = sum(info[i]+1 for i in range(11) if win_lose[i])
        if current_arrow <= n:
            apeach = sum(i for i in range(11) if not win_lose[i] and info[i])
            ryan = sum(i for i in range(11) if win_lose[i])
            point = ryan-apeach
            if point > max_point:
                max_point = point
                ans = [info[i]+1 if win_lose[i] else 0 for i in range(11)]
                ans[0] += n - current_arrow
    ans.reverse()
    print(ans)
    return ans