import sys
input = sys.stdin.readline

word1 = input().rstrip()
word2 = input().rstrip()
word3 = input().rstrip()

x = len(word1)
y = len(word2)
z = len(word3)

arr = [[[0] * (z+1) for _ in range(y+1)] for _ in range(x+1)]


for i in range(1, x+1):
    for j in range(1, y+1):
        for k in range(1, z+1):
            if word1[i-1] == word2[j-1] == word3[k-1]:
                arr[i][j][k] = arr[i-1][j-1][k-1] + 1
            
            else:
                arr[i][j][k] = max(arr[i][j][k-1], arr[i][j-1][k], arr[i-1][j][k])

ans = 0

for i in range(x+1):
    for j in range(y+1):
        ans = max(max(arr[i][j]), ans)

print(ans)