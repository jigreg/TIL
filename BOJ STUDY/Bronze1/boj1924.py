x,y = map(int,input().split())
'''
1,3,5,7,8,10,12 = 31일까지
4,6,9,11 = 30 일까지
2 = 28일까지
1.1은 월
x,y 가 총 일수를 구하면 됨 그러면 총일수 /7 나머지 대로 월화수목금토일 출력

'''
day = 0
if x == 1:
    day = y
elif x == 2:
    day = 31 + y
elif x == 3:
    day = 31+28+y
elif x == 4:
    day = 31 + 28 + 31 + y
elif x == 5 :
    day = 31 + 28 + 31 + 30 + y
elif x == 6 :
    day = 31 + 28 + 31 + 30 + 31 + y
elif x == 7 :
    day = 31 + 28 + 31 + 30 + 31 + 30 + y
elif x == 8 :
    day = 31 + 28 + 31 + 30 + 31 + 30 + 31 + y
elif x == 9:
    day = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + y
elif x == 10 :
    day = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + y
elif x == 11 :
    day = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + y
else :
    day = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + y

yo = {1:'MON', 2:'TUE', 3:'WED',4:'THU',5:'FRI',6:'SAT',0:'SUN'}
print(yo.get(day%7))

'''
Day = 0
arrList = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
weekList = ["SUN", "MON","TUE", "WED", "THU", "FRI", "SAT"]
 
x, y = map(int,input().split())
 
for i in range(x-1):
    Day = Day + arrList[i]
Day = (Day + y) % 7
 
print(weekList[Day])
'''