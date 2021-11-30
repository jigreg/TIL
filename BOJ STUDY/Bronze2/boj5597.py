# 1 줄에 1명씩 입력됨 번호는 30번까지 총 28명 입력 2명 출력 가장 작은 출석번호 순으로 출력
students = [x for x in range(1,31)]
for _ in range(28):
    students.remove(int(input())) #제출학생 출석부에 제외
    

print(students[0])
print(students[1])



# 좀더 간결하게 만들어 볼까
# 리스트 선언부를 students = [x for x in range(1,31)]
    
