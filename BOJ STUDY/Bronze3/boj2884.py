h, m = map(int,input().split())

if h == 0 :
    if m >= 45:
        m = m-45
        print(0,m)
    else :
        m = 60-(45 -m)
        print(23,m)
else : 
    if m >= 45:
        m = m-45
        print(h,m)
    else :
        h = h-1
        m = 60-(45-m)
        print(h,m) 

