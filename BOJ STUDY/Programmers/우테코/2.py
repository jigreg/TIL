#우테코 2번 공부시간 구하기
def solution(log):
    answer = ''
    ansh = 0
    ansm = 0
    log1 = [log[i:i+2] for i in range(0, len(log), 2)]
    for i in log1:
        hh,mm= i[0].split(":")
        hh1,mm1=i[1].split(":")
        if int(mm1)-int(mm) < 0:
            m = 60-(int(mm)-int(mm1))
            h = int(hh1)-int(hh)-1
        else :
            h = int(hh1)-int(hh)
            m = int(mm1)-int(mm)
        if h>=2 or h==1 and m>=45:
            h,m=1,45
        elif m <5 :
            m=0
        ansh += h
        ansm += m
        if ansm >=60:
            ansm = ansm-60
            ansh +=1 
    if ansh < 10:
        ans = ("0"+str(ansh)+":"+str(ansm))
    else :
        ans = (str(ansh)+":"+str(ansm))
    return ans

solution(["01:00", "08:00", "15:00", "15:04", "23:00", "23:59"])
