
while True:
    try:
        print(input())
    except EOFError:
        break

#EOError : 읽어들일 데이터가 더이상 없을 때 발생하는 에러