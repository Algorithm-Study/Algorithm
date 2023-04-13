# 1의 갯수 = 4**n 의 규칙을 따름
# n번째 비트열을 5개씩 자른 구간의 수는 5**(n-1)
def solution(n, l, r):
    def onecount(order, position):
        if order == 1:
            return sum([1,1,0,1,1][:position])
        interval = 5**(order-1)
        area, area_pos = position//interval, position%interval
        one = 0
        if area <= 1:
            one = 4**(order-1)*area + onecount(order-1, area_pos)
        elif area == 2:
            one = 4**(order-1)*2
        else:
            one = 4**(order-1)*(area-1) + onecount(order-1, area_pos)
        return one
    return onecount(n,r) - onecount(n,l-1)