# 반복문 연산을 함수로 전환하면 일반 코드 대비 더 빠르게 동작 4480ms ->  2108ms
# https://8iggy.tistory.com/155
n, m = map(int, input().split())
trees = list(map(int, input().split()))
start, end = 0, min(max(trees), 1_000_000_000)
def cut(mid):
    total = 0
    for tree in trees:
        if tree >= mid:
            total += tree - mid
    return total


while start <= end:
    mid = (start + end)//2
    get = cut(mid)
    if get >= m:
        start = mid + 1
    else:
        end = mid - 1
print(end)
