n = int(input())
buildings = list(map(int,input().split()))
result = 0
for idx, building in enumerate(buildings):
    count = 0
    left, right = float('inf'), -float("inf")
    for i in range(idx-1,-1,-1):
        slope = (building - buildings[i])/(idx-i)
        if slope < left: 
            left = slope
            count += 1
    for i in range(idx+1,n):
        slope = (building - buildings[i])/(idx-i)
        if slope > right: 
            right = slope
            count += 1
    result = max(result,count)
print(result)

# 왼쪽은 양의 기울기, 오른쪽은 음의 기울기 이므로 이에 맞춰서 기울기 체크