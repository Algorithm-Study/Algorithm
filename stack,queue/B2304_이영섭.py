N = int(input())
ware_house = {}
max_val, max_idx, last_idx = 0, 0, 0
for _ in range(N):
    L, H = map(int, input().split())
    ware_house[L] = H
    if H > max_val:
        max_val, max_idx = H, L
    if L > last_idx:
        last_idx = L
square_meter, height = 0, 0
for i in range(max_idx+1):
    if i in ware_house and ware_house[i] > height:
        height = ware_house[i]
    square_meter += height
height = 0
for i in range(last_idx, max_idx, -1):
    if i in ware_house and ware_house[i] > height:
        height = ware_house[i]
    square_meter += height
print(square_meter)