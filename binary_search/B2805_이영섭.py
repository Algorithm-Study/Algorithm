N, M = map(int, input().split())
H = list(map(int, input().split()))
H.sort()


def tree_height(tree):
    high = tree[-1]
    height_diff = []
    for i in range(len(tree)-1, 0, -1):
        height_diff.append(tree[i] - tree[i-1])
    height_diff.append(tree[0])
    # print(height_diff)
    cut_tree, height, last = 0, 0, 0
    for idx, cut in enumerate(height_diff):
        last = idx+1
        height += cut
        cut_tree += last * cut
        # print(cut_tree)
        if cut_tree >= M:
            break
    while cut_tree > M:
        cut_tree -= last
        height -= 1
        # print(cut_tree)
    if cut_tree != M:
        height += 1
    return high - height


print(tree_height(H))

# 문제 접근 방법
# # 이분탐색 문제인데 이분탐색으로 못풀겠어서 나무를 정렬하고 나무끼리의 차이를 구함
# # M보다 지금까지 자른 나무가 작으면 다음 나무 크기까지 자름
# # 이때 M보다 커지게 되면 1m씩 다시 줄이면서 값을 찾음