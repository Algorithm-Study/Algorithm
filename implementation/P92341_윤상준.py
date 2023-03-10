import math
def solution(fees, records):
    IN = {}
    OUT = {}
    answer = []
    for record in records:
        time, num, status = record.split()
        hour, minute = time.split(':')
        if status == 'IN':
            IN[num] = int(hour) * 60 + int(minute)
        else:
            if num in OUT:
                OUT[num] += int(hour) * 60 + int(minute) - IN[num]
                del IN[num]
            else:
                OUT[num] = int(hour) * 60 + int(minute) - IN[num]
                del IN[num]
        #print(IN)
        #print(OUT)
    
    for i in IN.keys():
        if i in OUT:
            OUT[i] += 23*60 + 59 - IN[i]
        else:
            OUT[i] = 23*60 + 59 - IN[i]
    OUT = dict(sorted(OUT.items()))
    #print(OUT)
    for o in OUT.keys():
        if OUT[o] <= fees[0]:
            answer.append(fees[1])
        else:
            answer.append(math.ceil((OUT[o]-fees[0])/fees[2]) * fees[3] + fees[1])
    return answer