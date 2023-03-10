def cal_fee(fees, time):
    if time <= fees[0]:
        return fees[1]
    else:
        mok = (time - fees[0]) // fees[2]
        if (time - fees[0]) % fees[2] != 0:
            mok += 1
        return fees[1] + mok * fees[3]

def cal_time(re_str):
    temp = re_str.split(":")
    return int(temp[0]) * 60 + int(temp[1])

def solution(fees, records):
    record = [rec.split() for rec in records]
    # record = sorted(record, key=lambda record: record[1])
    car_number = dict()
    fee = dict()
    for re in record:
        if re[1] not in car_number:
            car_number[re[1]] = cal_time(re[0])
        else:
            past = car_number.pop(re[1])
            now = cal_time(re[0])
            if re[1] not in fee:
                fee[re[1]] = now - past
            else:
                fee[re[1]] += now - past
    for cn in car_number:
        now = 1439
        if cn not in fee:
            fee[cn] = now - car_number[cn]
        else:
            fee[cn] += now - car_number[cn]
    for fe in fee:
        fee[fe] = cal_fee(fees, fee[fe])
    answer = list(map(lambda x:x[1], sorted(fee.items())))
    # answer = [cal_fee(fees, fee[fe]) for fe in fee]
    return answer

# 문제 접근 방식
# # IN, OUT이 잘못 들어오는 경우는 없으므로 순서대로 시간 계산
# # 계산된 시간으로 요금을 구하기
# # 주석처리된 부분으로 정렬을 했었는데 계속 틀림
# 새로 배운 python
# # map 함수에 lambda를 사용하면 dictionary를 원하는 값으로 정렬이 가능, 37번째 줄!!!!