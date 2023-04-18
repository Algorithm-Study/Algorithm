def solution(elements):
    answer = 0
    leng = len(elements)
    data = set()
    for i in range(1, len(elements)):
        # print("i", i)
        sum = 0
        for j in range(i):
            sum += elements[j]
        data.add(sum)
        for idx, element in enumerate(elements):
            sum -= element
            sum += elements[(idx + i)%leng]
            data.add(sum)
    sum = 0
    for element in elements:
        sum += element
    data.add(sum)
    return len(data)