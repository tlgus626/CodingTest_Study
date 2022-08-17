def solution(progresses, speeds):


    #변수설정

    answer = []
    time = 0
    count = 0


    ### 설명을 위한 입력값 설정 ###
    # progresses = [93,30,55]
    # speeds = [1,30,5]


    ### 첫 번째가 100이 될때까지 loop를 돌며  time을 늘린다. ###

    ### (time =7) 이 되면  첫번째 값이(93) 100이 되어 if에 따라 pop 되고 count +=1 ###
    ### 현재 time 이 7이기 때문에 두번째 값(30)도 if에 따라 pop 되고 count +=1  ###
    ### 세번째 값은 100이 안되기 때문에 loop를 돌며 time을 늘림 ###
    ### ->  미리 완성된 제품들의 count를 answer에 넣어준다. ###
    ### -> 그 후, count = 0 으로 초기화시키고 다시 loop 돌린다.
    ### 끝!

    while len(progresses) > 0:

        if (progresses[0] + time * speeds[0]) >= 100:

            progresses.pop(0) #progress에서 첫 번째 값이 없어짐. : pop
            speeds.pop(0)
            count += 1

        else:
            if count > 0:

                answer.append(count)
                count = 0

            time += 1

    answer.append(count)

    return answer
