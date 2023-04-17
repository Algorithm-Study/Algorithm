n = int(input())
data = list(map(int, input().split()))
data.sort()


def bin_search():
    ans_low, ans_mid, ans_high, min_val = 0, 1, n-1, 3000000001
    for low in range(0, n-2):
        mid = low + 1
        high = n - 1
        while mid < high:
            if data[low] + data[mid] + data[high] > 0:
                if min_val > abs(data[low] + data[mid] + data[high]):
                    min_val = abs(data[low] + data[mid] + data[high])
                    ans_low, ans_mid, ans_high = low, mid, high
                high -= 1
            elif data[low] + data[mid] + data[high] < 0:
                if min_val > abs(data[low] + data[mid] + data[high]):
                    min_val = abs(data[low] + data[mid] + data[high])
                    ans_low, ans_mid, ans_high = low, mid, high
                mid += 1
            else:
                return data[low], data[mid], data[high]
    return data[ans_low], data[ans_mid], data[ans_high]


low, mid, high = bin_search()
print(low, mid, high)

# 문제 접근 방법
# # low를 정점으로 두고 mid와 high 값을 이분탐색으로 찾음