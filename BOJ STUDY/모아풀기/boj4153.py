while True :
    a= list(map(int,input().split()))
    max_a = max(a)
    if sum(a) == 0 :
        break
    a.remove(max_a)
    if a[0]**2 + a[1]**2 == max_a**2:
        print('right')
    else :
        print('wrong')