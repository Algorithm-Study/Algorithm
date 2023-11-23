import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

preorder_arr = []
while True:
    try:
        preorder_arr.append(int(input()))
    except:
        break

def postorder(start, end):
    if start > end:
        return
    mid = end + 1
    for i in range(start+1, end+1):
        if preorder_arr[i] > preorder_arr[start]:
            mid = i
            break
    postorder(start+1, mid-1) #왼쪽 트리
    postorder(mid, end) #오른쪽 트리
    print(preorder_arr[start]) #루트 노드

postorder(0, len(preorder_arr)-1)