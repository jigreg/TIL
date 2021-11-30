
n = int(input())

for _ in range(n):
    a = input().split()
    b = input().split() # A,B 의 딱지 입력 받기
    #print(a,b)
    a.pop(0)
    b.pop(0)
    byul = a.count('4')
    byul1 = b.count('4')
    round = a.count('3')
    round1 = b.count('3')
    square = a.count('2')
    square1 = b.count('2')
    tri = a.count('1')
    tri1 = b.count('1') # 개수 파악

    if byul > byul1:
        print('A')
    elif byul < byul1 :
        print('B')
    else :
        if round > round1:
            print('A')
        elif round < round1:
            print('B')
        else :
            if square > square1:
                print('A')
            elif square < square1:
                print('B')
            else :
                if tri > tri1:
                    print('A')
                elif tri < tri1:
                    print('B')
                else :
                    print('D')

'''
from collections import defaultdict

number_of_round = int(input())
for round_num in range(number_of_round):
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    #딱지의 개수 부분 제거
    A.pop(0)
    B.pop(0)
    #각 모양의 갯수를 판단하기 위한 딕셔너리 생성
    A_dic, B_dic = defaultdict(int), defaultdict(int)
    for num in A:
        A_dic[num] += 1
    for num in B:
        B_dic[num] += 1
    
    #같은 모양 기준, 개수가 더 많은 쪽을 프린트
    #전부 다 같으면 D
    for shape in range(4,0,-1):
        if A_dic[shape] > B_dic[shape] :
            print('A')
            break
        elif A_dic[shape] < B_dic[shape] :
            print('B')
            break
    else :
        print('D')
'''
