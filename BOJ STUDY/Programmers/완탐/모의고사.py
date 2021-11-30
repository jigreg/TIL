def solution(answers):
    answer=[]
    answer_temp=[]
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]
    acnt=bcnt=ccnt = 0
    for i in range(len(answers)):
        print(i)
        if answers[i] == a[i%len(a)]:
            acnt += 1
        if answers[i] == b[i%len(b)]:
            bcnt +=1
        if answers[i] == c[i%len(c)]:
            ccnt +=1
        
    answer_temp = [acnt,bcnt,ccnt]
    for person,score in enumerate(answer_temp):
        if score == max(answer_temp):
            answer.append(person+1)
    return answer

solution([1,3,2,4,2])