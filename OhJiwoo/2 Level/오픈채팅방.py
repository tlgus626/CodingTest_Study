def solution(record):
    answer = []
    id=dict()
    records=[]
    for i in record :
        records.append(list(i.split()))
    #딕셔너리 할당 
    for j in records :
        if j[0]=="Enter" or j[0]=="Change" :
            id[j[1]]=j[2]
    for k in records:
        if k[0]=="Enter" :
            answer.append(id[k[1]]+"님이 들어왔습니다.")
        elif k[0]=="Leave":
            answer.append(id[k[1]]+"님이 나갔습니다.")
    return  answer
