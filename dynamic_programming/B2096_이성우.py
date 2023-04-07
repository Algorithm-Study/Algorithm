import sys
input = sys.stdin.readline

n = int(input())
max_maps = [0,0,0]
min_maps = [0,0,0]
tmp_map1 = [0,0,0]
tmp_map2 = [0,0,0]
for i in range(1,n+1):

    maps = list(map(int,input().split()))
    max_maps[0] = maps[0] + max(tmp_map1[0], tmp_map1[1])
    max_maps[1] = maps[1] + max(tmp_map1[0], tmp_map1[1], tmp_map1[2])
    max_maps[2] = maps[2] + max(tmp_map1[1], tmp_map1[2])
    tmp_map1 = max_maps[:]
    min_maps[0] = maps[0] + min(tmp_map2[0], tmp_map2[1])
    min_maps[1] = maps[1] + min(tmp_map2[0], tmp_map2[1], tmp_map2[2])
    min_maps[2] = maps[2] + min(tmp_map2[1], tmp_map2[2])
    tmp_map2 = min_maps[:]
    
print(max(max_maps), min(min_maps))