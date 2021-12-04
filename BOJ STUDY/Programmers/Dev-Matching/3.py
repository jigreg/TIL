import itertools
def solution(s):
    answer = 0
    keyboard = [['q','w','e','r','t','y','u','i','o'],
                ['p','a','s','d','f','g','h','j','k'],
                ['l','z','x','c','v','b','n','m','0']]
    
    
    return answer

def indexing(st):
    cnt = 1
    bubun = []
    while cnt > len(st):
        if cnt == 2:
            for i in range(len(st)-1):
                bubun.append(st[i:i+1])
        