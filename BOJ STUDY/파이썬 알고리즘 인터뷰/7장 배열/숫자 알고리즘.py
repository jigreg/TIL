num_list=[]

for i in range(100):
    num_list.append(i)

index = 0
for i in num_list:
    temp = '{:0<3d}'.format(i)
    num_list[index] = temp
    index +=1

num_list.sort()

temp = list(map(int,i))