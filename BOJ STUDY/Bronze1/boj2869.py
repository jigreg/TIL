a,b,v = map(int,input().split())
d = 0

# a를 더한거 저장, b 뺸거 저장 a 더햇을때 v 넘으면 끝 a,b 나 a 실행되면 1일카운트 
# 싸이클 돌아야댐 a,b cnt +=1 if a += d > v 면 break 시간초가남
# a-b -> 달팽이 1일 이동 안미끄러짐 v-b
if (v-b) % (a-b) !=0:
    d = ((v-b)//(a-b)) + 1
else :
    d = ((v-b)//(a-b))

print(d)

'''
import math

a, b, v = map(int, input().split())
# a= 올라가는 길이, b= 떨어지는길이, v= 나무높이 

day = math.ceil((v-a)/(a-b)) + 1
print(day)

math.celi 올림
'''