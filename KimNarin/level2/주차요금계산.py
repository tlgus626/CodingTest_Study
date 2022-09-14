from math import ceil

def hour_to_minute(time):   # 시간 단위를 분단위로 변환하는 함수
    
    time_lst = time.split(':')
    
    minute = int(time_lst[0])*60 + int(time_lst[1])
    return minute

def make_fee_dict(records):   # 요금 내역을 차 번호를 키로 딕셔너리 제작
    fee_dict = {}
    for r in records:
        time, car_num, status = r.split(' ')


        if car_num not in fee_dict.keys():
            fee_dict[car_num]={'time_history': [time]}
        else:
            fee_dict[car_num]['time_history'].append(time)
            
    return fee_dict

def make_car_fee(car_num_lst,fee_dict,default_time, default_fee, unit_time, unit_fee ):
    tot_time = 0
    car_fee = {}
    for car in car_num_lst:
        tot_time = 0
        time_his = fee_dict[car]['time_history']    # 최종 요금 계산 함수


        if len(time_his) % 2 !=0:
            time_his.append('23:59')  # 리스트에 짝수가 아니면 11:59 추가
            
        for i in range(1,len(time_his)+1,2):
            out_time = time_his[i]
            in_time = time_his[i-1]

            out_min = hour_to_minute(out_time)
            in_min = hour_to_minute(in_time)

            tot_time += out_min - in_min

        if tot_time <= default_time:
            tot_fee = default_fee
        else:
            tot_fee = default_fee + ceil((tot_time - default_time)/unit_time) * unit_fee

        car_fee[car]= tot_fee

    
    return car_fee

def solution(fees, records):
    default_time, default_fee, unit_time, unit_fee = fees
    
    fee_dict = make_fee_dict(records)
            
    car_num_lst = sorted(list(fee_dict.keys()))
    
    car_fee = make_car_fee(car_num_lst,fee_dict,default_time, default_fee, unit_time, unit_fee)

    
    return list(map(lambda x : car_fee[x], car_num_lst))
