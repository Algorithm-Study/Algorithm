def gcd(big, small):
    left = big % small
    if left == 0:
        return small
    return gcd(small, left)

def solution(arrayA, arrayB):
    gcd_A = arrayA[0]
    for a in arrayA:
        gcd_A = gcd(gcd_A, a)
    gcd_B = arrayB[0]
    for b in arrayB:
        gcd_B = gcd(gcd_B, b)
    answer2 = gcd_A
    answer1 = gcd_B
    for a,b in zip(arrayA, arrayB):
        if a % gcd_B == 0:
            answer1 = gcd_B // gcd(a,gcd_B)
        if b % gcd_A == 0:
            answer2 = gcd_A // gcd(b,gcd_A)
    return max(answer1, answer2) if answer1 != answer2 else 0