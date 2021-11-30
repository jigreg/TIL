n = int(input())
coin = [500,100,50,10,5,1]
pay = 1000-n
answer = 0
for i in coin:
    answer += pay//i
    pay %= i
print(answer)