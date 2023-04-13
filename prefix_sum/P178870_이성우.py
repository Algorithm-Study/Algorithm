def solution(sequence, k):
    left = 0
    right = 0
    s = sequence[left]
    tmp = []
    tmp2 = float('inf')
    
    while left <= right < len(sequence):
        if s <= k:
            # print(sequence[left:right])
            if s == k and right - left < tmp2:
                tmp.append([left,right])
                tmp2 = right - left
            right += 1
            if right < len(sequence):
                s += sequence[right]

        else:
            s -= sequence[left]
            left += 1

    # print(tmp)
    return tmp[-1]