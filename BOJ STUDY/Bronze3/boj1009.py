t = int(input())

for _ in range(t):
    a,b = map(int,input().split())
   
    if a==1:
        print(1)
        continue
    elif a==5 :
        print(5)
        continue
    elif a == 6:
        print(6)
        continue

    result_list = []
    temp = 1
    for _ in range(b):
        temp *= a
        temp %= 10
        if temp in result_list:
            break
        result_list.append(temp)

    result = result_list[b%len(result_list)-1]
    if result == 0:
        print(10)
    else :
        print(result)