n = int(input())
dice = list(map(int, input().split()))

answer = 0
face = []
if n == 1:
    dice = sorted(dice)
    answer = sum(dice[:5])

else:
    for i in range(3):
        face.append(min(dice[i], dice[5-i]))
    face.sort()
        
    face1 = sum(face[:1])
    face2 = sum(face[:2])
    face3 = sum(face[:3])

    look1 = (n-2)*(n-2) + 4*(n-1)*(n-2)
    look2 = 4*(n-2) + 4*(n-1)
    look3 = 4

    answer += face1 * look1 + face2 * look2 + face3 * look3

print(answer)