from collections import defaultdict
def solution(fees, records):
    default_time, default_fee, unit_time, unit_fee = fees
    car_dict = defaultdict(int)
    car_io_dict = {}
    answer = {}
    
    for record in records:
        car_time, car_number, car_io = record.split()
        car_time = car_time.split(':')
        car_time = int(car_time[0])*60 + int(car_time[1])
        
        if car_io == "IN":
            car_dict[car_number] -= car_time
            car_io_dict[car_number] = "IN"
        else:
            car_dict[car_number] += car_time
            car_io_dict[car_number] = "OUT"

    for left_car in car_dict:
        if car_io_dict[left_car] == "IN":         
            car_dict[left_car] += 23*60 + 59
            car_io_dict[left_car] = "OUT"

    for car in car_dict:

        if car_dict[car] > default_time:
            car_fee = default_fee + (car_dict[car] - default_time)//unit_time*unit_fee
            if (car_dict[car] - default_time)%unit_time:
                car_fee += unit_fee
        else:
            car_fee = default_fee

        answer[car] = car_fee

    answer = sorted(answer.items())
    answer = [i[1] for i in answer]
    return answer