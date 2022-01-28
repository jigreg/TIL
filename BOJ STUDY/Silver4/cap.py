import pandas as pd
file_path = '/content/drive/MyDrive/data/1.xlsx'
cap = pd.read_excel(file_path)
cap = cap[['생년월일','이름','학력','학력상태','성별']]
cap.sort_values('생년월일')
# 남 여 수 구하기
cap['성별'].value_counts()
# 생년월일 구하
date1 = cap['생년월일']
A20 = 0
A30 = 0
A10 = 0
sum = len(date1)
for i in date1:
  age = 2022-int(i[0:4])
  if age < 20 :
    A10 +=1
  elif 20<=age<30:
    A20 +=1
  else :
    A30 +=1

print("10대",A10,"20대", A20,"30대",A30)
print('10대 = {:.2f} 20대 = {:.2f} 30대 ={:.2f}'.format(A10/sum*100,A20/sum*100,A30/sum*100))