def solution(book_time):
    new_book = []
    answer = 0
    for bt in book_time:
        sth, stm = bt[0].split(":")
        st = int(sth)*60 + int(stm)
        new_book.append([st, 1])
        eth, etm = bt[1].split(":")
        et = int(eth)*60 + int(etm) + 10
        new_book.append([et, 0])
    new_book.sort()
    cnt = 0
    for nb in new_book:
        if nb[1] == 1:
            cnt += 1
            answer = max(answer, cnt)
        else:
            cnt -= 1
    return answer

# 문제 접근 방법
# # 입실 시간과 퇴실 시간을 구분하는 것이 포인트
# # 만약 시간이 같다면 퇴실을 먼저 입실을 나중에
# # 정렬 후 확인한다면 현재 객실에 들어가 있는 인원 수를 구할 수 있음