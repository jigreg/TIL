n = int(input())
for _ in range(n): 
    p = int(input()) 
    max = 0 
    mName = "" 
    for _ in range(p): 
        num, name = input().split() 
        num = int(num) 
        if(num > max): 
            max = num 
            mName = name 
    print(mName)

