import sys
sys.setrecursionlimit(10**5)
num = []
while True:
    try:
        num.append(int(input()))
    except:
        break


def postorder(st, ed):
    if st > ed:
        return
    pre, post = -1, ed+1
    pre_flag = False
    for i in range(st+1, ed+1):
        if not pre_flag and num[i] < num[st]:
            pre = i
            pre_flag = True
        if num[i] > num[st]:
            post = i
            break

    if pre != -1:
        postorder(pre, post-1)
    if post != ed+1:
        postorder(post, ed)
    print(num[st])


postorder(0, len(num)-1)
