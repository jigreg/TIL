def solution(rows, columns):
    answer = [[]]
    arr = [[0] * columns] * rows
    while 0 in arr[0] :
        cnt = 0
        arr[0][0] = 1
        arr[0][1] = 2
        arr[1][1] = 3
        for i in range(len(arr)-1):
            for j in range(len(arr)-1):
                if arr[i][j] % 2 == 0:
                    cnt +=1
                    arr[i][j+1] = cnt
                else :
                    cnt +=1
                    arr[i+1][j] = cnt
        break
    print(arr)
    print(0 not in arr)
    return answer

solution(3,4)