import sys
input = sys.stdin.readline

N = int(input())
data = list(map(int, input().split()))
data.sort()


def bin_search(data):
    low, ret_low = 0, 0
    high, ret_high = len(data) - 1, len(data) - 1
    like_zero = 2000000001
    while low < high:
        # print(low, high, data[low], data[high])
        if like_zero > abs(data[low] + data[high]):
            like_zero = abs(data[low] + data[high])
            ret_low = low
            ret_high = high
        if data[low] + data[high] < 0:
            low += 1
        elif data[low] + data[high] > 0:
            high -= 1
        else:
            return low, high
    return ret_low, ret_high


low, high = bin_search(data)
print(data[low], data[high])

# 문제 접근 방법
# # 정렬 후 이분탐색의 원리를 사용하여 외부에서 내부로 좁혀 들어오며 비교
# # ++ or --도 가능하고 합이 0에 가까워야 하므로 초기값을 최댓값*2 + 1로 설정