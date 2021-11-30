def solution(numbers,target):
    super=[0]
    for i in numbers:
        sub=[]
        for j in super:
            sub.append(j+i)
            sub.append(j-i)
        super = sub
    return super.count(target)