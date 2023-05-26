n, d, k, c = map(int, input().split())
sushi = [int(input()) for _ in range(n)]
circle = sushi + sushi
variation = 0
for i in range(n):
    choice = list(set(circle[i:i+k] + [c]))
    variation = max(variation, len(choice))
print(variation)
# Sliding Window
# 포인터를 움직이는 것보다 길이를 두대 늘려서 진행