operation = list(map(int, input().split()))[:-1]
records = {(0,0): 0}
def move(goal, left_leg, right_leg, cost, side):
    if side == 0:
        if (goal,right_leg) in temp:
            if records[(left_leg, right_leg)] + cost < temp[(goal, right_leg)]:
                 temp[(goal,right_leg)] = records[(left_leg, right_leg)] + cost
        else:
            temp[(goal,right_leg)] = records[(left_leg, right_leg)] + cost
    else:
        if (left_leg, goal) in temp:
            if records[(left_leg, right_leg)] + cost < temp[(left_leg, goal)]:
                 temp[(left_leg, goal)] = records[(left_leg, right_leg)] + cost
        else:
            temp[(left_leg, goal)] = records[(left_leg, right_leg)] + cost
opposite = [(1,3), (3,1), (2,4), (4,2)]                 
for op in operation:
    temp = {}
    for record in records:
        if op == record[0]:
            move(op, record[0], record[1], 1, 0)
        elif op == record[1]:
            move(op, record[0], record[1], 1, 1)
        else:
            #왼발이동
            if (op, record[0]) in opposite:
                move(op, record[0], record[1], 4, 0)
            elif record[0]==0:
                move(op, record[0], record[1], 2, 0)
            else:
                move(op, record[0], record[1], 3, 0)
            #오른발이동
            if (op, record[1]) in opposite:
                move(op, record[0], record[1], 4, 1)
            elif record[1]==0:
                move(op, record[0], record[1], 2, 1)
            else:
                move(op, record[0], record[1], 3, 1)
    records = temp
print(min(records.values()))