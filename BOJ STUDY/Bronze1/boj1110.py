input_num = temp = int(input()) 
cnt = 0 
while True: 
    num1 = temp // 10 
    num2 = temp % 10 
    sum_num = num1 + num2 
    temp = int(str(num2) + str(sum_num % 10)) 
    cnt += 1 
    if input_num == temp: 
        break 
    
    
print(cnt)

