import math

# from string('05:30') to minutes(5*60 mins + 30 mins)
def string_to_time(x):
    x = x.split(':')
    x = int(x[0]) * 60 + int(x[1])
    return x

# total fees using cumulate minutes
def get_charge(fees, x):
    if x <= fees[0]:
        return fees[1]
    else:
        return fees[1] + math.ceil((x - fees[0]) / fees[2]) * fees[3]


def solution(fees, records):
    # key=car number , value=[IN, OUT, IN, OUT ...]
    rec = dict()
    for r in records:
        time, car, _ = r.split()
        if car not in rec.keys():
            rec[car] = [time]
        else:
            rec[car].append(time)
    # if len(value) is odd
    for r in rec.keys():
        if len(rec[r]) % 2 != 0:
            rec[r].append('23:59')
    # total fees
    answer = []
    for r in sorted(rec.keys()):
        times = rec[r]
        cum_time = 0
        for i in range(1, len(times), 2):
            cum_time += (string_to_time(times[i]) - string_to_time(times[i - 1]))
        answer.append(get_charge(fees, cum_time))
    return answer
