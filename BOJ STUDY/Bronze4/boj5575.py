for _ in range(3):
    a,b,c,d,e,f = map(int,input().split())
    in1 = a*3600 + b*60 + c
    out = d*3600 + e*60 + f
    work = out -in1
    h = work//3600 % 24
    m = work//60%60
    s = work%60
    print(h,m,s)
