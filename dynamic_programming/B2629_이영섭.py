n = int(input())
weight = list(map(int, input().split()))
board = ["N"]*40001
board[0] = "Y"

for w in weight:
    check = set()
    for i in range(40001):
        if board[i] == "Y":
            if i + w < 40001:
                check.add(i+w)
            if abs(i - w):
                check.add(abs(i-w))
    for c in check:
        board[c] = "Y"

m = int(input())
marble = list(map(int, input().split()))
for i in marble:
    print(board[i], end=" ")
