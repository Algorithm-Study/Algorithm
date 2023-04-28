def solution(n, wires):
    answer = 100
    for i in range(n-1):
        heap = list(wires)
        heap.pop(i)
        L, R = set(), set()
        L.add(wires[i][0])
        R.add(wires[i][1])
        while heap:
            a, b = heap.pop(0)
            if a in L or b in L:
                L.add(a)
                L.add(b)
            elif a in R or b in R:
                R.add(a)
                R.add(b)
            else:
                heap.append([a, b])
        answer = min(abs(len(L)-len(R)), answer)
    return answer