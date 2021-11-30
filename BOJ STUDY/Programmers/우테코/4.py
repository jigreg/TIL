def solution(s):
    cnt = 1
    arr = []
    answer = []
    print(s[0],s[-1])
    if s[0] == s[-1]:
        for i in range(len(s)-1):
                if s[i] == s[i+1]:
                    cnt+=1 
                else :
                    cnt = 0
                arr.append(cnt)
        last = arr[-1]
        arr.pop(-1)
        for j in range(len(arr)-1):
            if arr[j] == 0:
                answer.append(arr[j-1])
        print(answer)
    else :
        if s[i] == s[i+1]:
            cnt+=1 
        else :
            cnt = 0
        arr.append(cnt)

    return answer

solution("wowwow")