from math import gcd
def solution(arrayA, arrayB):
    answer, max_A, max_B = 0, 0, 0
    gcd_A = arrayA[0]
    for arr in arrayA[1:]:
        gcd_A = gcd(gcd_A, arr)
    # print('A', gcd_A)
    if gcd_A != 1:
        gcd_A_list = [tp for tp in range(2, gcd_A+1) if gcd_A%tp == 0]
        # print(gcd_A_list)
        if gcd_A_list:
            for gcda in gcd_A_list:
                for B in arrayB:
                    if B % gcda == 0:
                        break
                else:
                    if max_A < gcda:
                        max_A = gcda
    gcd_B = arrayB[0]
    for arr in arrayB[1:]:
        gcd_B = gcd(gcd_B, arr)
    # print('B', gcd_B)
    if gcd_B != 1:
        gcd_B_list = [tp for tp in range(2, gcd_B+1) if gcd_B%tp == 0]
        # print(gcd_B_list)
        if gcd_B_list:
            for gcdb in gcd_B_list:
                for A in arrayA:
                    if A % gcdb == 0:
                        break
                else:
                    if max_B < gcdb:
                        max_B = gcdb
    # print(max_A, max_B)
    answer = max_B if max_A < max_B else max_A
    return answer