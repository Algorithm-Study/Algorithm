tc = int(input())
for _ in range(tc):
    # 초기값 설정
    n, m, k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr = arr + arr[:m-1]
    tmp = sum(arr[:m])
    answer = int(tmp < k)
    # 슬라이딩 윈도우
    for idx in range(m, len(arr)):
        # 엣지 케이스 처리
        if m == n:
            break
        tmp += arr[idx] - arr[idx-m]
        if tmp < k:
            answer += 1
    print(answer)