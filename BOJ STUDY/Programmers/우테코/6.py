def solution(time, plans):
    chul = 13 # 출근시간
    toei = 18 # 퇴근시간
    vac = 0 # 휴가
    answer =''
    for i in plans:
        if i[1][-2:] == 'PM':
            start = int(i[1][:-2]) + 12 #출발시간 구하기
        else : 
            start = int(i[1][:-2])
        if start < toei :
            vac += toei-start
        if i[2][-2:] == 'PM':
            arrive = int(i[2][:-2]) + 12
        else :
            arrive = int(i[2][:-2])
        if arrive > chul :
            vac += arrive - chul
        if vac <= time:
            answer = i[0]
        else :
            answer = "호치민"
    print(answer)
    return answer

solution(2,[ ["홍콩", "11PM", "9AM"], ["엘에이", "3PM", "2PM"] ])