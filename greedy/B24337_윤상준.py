n,a,b = map(int, input().split())
buildings = [max(a,b)]
buildings = [x for x in range(1,a)] + buildings + [x for x in range(b-1,0,-1)]
if len(buildings) > n:
    print(-1)
else:
    # 사전순으로 가장 앞으로 만들기 위해서는 길이가 부족한 경우 높이가 1인 빌딩을 앞쪽에 넣어야 함
    buildings = [buildings[0]] + [1]*(n-len(buildings)) + buildings[1:]
    print(*buildings)
# 사전 순으로 가장 앞으로 놓일 수 있는 조건에 대해서 생각해야 하는 문제