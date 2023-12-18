n = int(input())
boys = sorted(list(map(int, input().split())))
girls = sorted(list(map(int, input().split())), reverse= True)
b_idx, g_idx = 0, 0
couples = 0
while b_idx < n and g_idx < n:
    boy, girl = boys[b_idx], girls[g_idx]
    # 조건을 충족한 경우
    if boy < 0 and girl > 0 and abs(boy) > girl:
        couples += 1
        b_idx += 1
        g_idx += 1
    elif boy < 0 and girl > 0 and abs(boy) <= girl:
        g_idx += 1
    # 조건을 충족한 경우
    elif boy > 0 and girl < 0 and boy < abs(girl):
        couples += 1
        b_idx += 1
        g_idx += 1
    elif boy > 0 and girl < 0 and boy >= abs(girl):
        g_idx += 1
    elif boy < 0 and girl < 0:
        b_idx += 1
    elif 0 < boy and girl > 0:
        g_idx += 1
print(couples)