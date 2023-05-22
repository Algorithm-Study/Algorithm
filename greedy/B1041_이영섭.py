N = int(input())
dice = list(map(int, input().split()))
plane2 = [(0, 1), (0, 2), (0, 3), (0, 4), (5, 1), (5, 2), (5, 3), (5, 4), (1, 2), (1, 3), (4, 2), (4, 3)]
plane3 = [(0, 1, 2), (0, 2, 4), (0, 3, 4), (0, 3, 1), (5, 1, 2), (5, 2, 4), (5, 3, 4), (5, 3, 1)]
min_plane1 = min(dice)
min_plane2 = min([dice[i[0]] + dice[i[1]] for i in plane2])
min_plane3 = min([dice[i[0]] + dice[i[1]] + dice[i[2]] for i in plane3])
# print(min_plane1, min_plane2, min_plane3)
if N == 1:
    print(sum(dice) - max(dice))
elif N == 2:
    print(4 * min_plane2 + 4 * min_plane3)
else:
    print(min_plane3 * 4 + (2*N-3)*4*min_plane2 + ((N-1)*(N-2)*4 + (N-2)*(N-2)) * min_plane1)

# N^2*5
# ABC, ACE, ADE, ABD, FBC, FBD, FED, FEC
# AB, AC, AD, AE, FB, FC, FD, FE, BC, BD, EC, ED
# 1 - 5
# 2 - 20
# 3 - 45