alpa = list(input())
num = {'A':2,'B':2,'C':2,'D':3,'E':3,'F':3,'G':4,'H':4,
        'I':4,'J':5,'K':5,'L':5,'M':6,'N':6,'O':6,'P':7,
        'Q':7,'R':7,'S':7,'T':8,'U':8,'V':8,'W':9,'X':9
        ,'Y':9,'Z':9}

s = []
for i in alpa:
    if i in num:
        s.append(num.get(i))

print(sum(s)+len(alpa))

'''
alpabet_list = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
word = input()

time = 0
for unit in alpabet_list :  
    for i in unit:  # alpabet 리스트에서 각 요소를 꺼내서 한글자씩 분리
        for x in word :  # 입력받은 문자를 하나씩 분리
            if i == x :  # 두 알파벳이 같으면
                time += alpabet_list.index(unit) +3  # time = time + index +3
print(time)
'''