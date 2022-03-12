def solution(money,cost):
    answer = 0
    moneys=[]
    moenyi = 0
    coin = [500,100,50,10,5,1]
    cost.reverse()
    while len(coin) > 0:
        moneyi = money
        if len(coin) == 0:
            break
        for i in range(len(coin)):
                count = moneyi //coin[i]
                moneyi -= (count)*coin[i]
                answer += count * cost[i]
                if moneyi == 0 :
                    moneys.append(answer)
                    answer = 0
                    coin.pop(0)
                    cost.pop(0)
    print(min(moneys))
    return min(moneys)


solution(4578,[1,4,99,35,50,1000])