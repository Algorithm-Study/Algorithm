N = int(input())
data = list(map(int, input().split()))
left, right, sim_zero = 0, N-1, float('INF')
al, ar = 0, N-1
while left < right:
    val = data[left] + data[right]
    if abs(val) < abs(sim_zero):
        sim_zero = val
        al, ar = left, right
    if val > 0:
        right -= 1
    else:
        left += 1
print(data[al], data[ar])
