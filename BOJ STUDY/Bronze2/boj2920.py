music = list(map(int,input().split()))
music1 = [1,2,3,4,5,6,7,8]
if music == music1:
    print('ascending')
elif music == music1[::-1]:
    print('descending')
else :
    print('mixed')