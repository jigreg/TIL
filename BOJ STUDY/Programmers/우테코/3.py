import collections
def solution(ings, menu, sell):
    answer = 0
    ings = [ings[i * 1:(i + 1) * 1] for i in range((len(ings) + 1 - 1) // 1 )]
    menu = [menu[i * 1:(i + 1) * 1] for i in range((len(menu) + 1 - 1) // 1 )]
    sell = [sell[i * 1:(i + 1) * 1] for i in range((len(sell) + 1 - 1) // 1 )]
    for i in menu:
        profit=0
        price=0
        realprice=0
        price1 = 0 # 총 드는 재료비
        ingre = i[0].split(" ") #재료
        ingre1 = ingre[1] #재료 문자열
        realprice = ingre[2]
        cingre = collections.Counter(ingre1)
        for j in cingre:
            for k in ings:
                if k[0][:1] == j:
                    price = int(k[0][1:]) # 재료 가격
                    price1 += price * cingre.get(j)       
        profit = int(realprice)-price1 # 메뉴별 수익
        for l in sell:
            sellmenu = l[0].split(" ")
            if sellmenu[0] == ingre[0]:
                answer += int(sellmenu[1]) * profit
    print(answer)

    return answer

solution(["r 10", "a 23", "t 124", "k 9"],["PIZZA arraak 145", "HAMBURGER tkar 180", "BREAD kkk 30", "ICECREAM rar 50", "SHAVEDICE rar 45", "JUICE rra 55", "WATER a 20"],["BREAD 5", "ICECREAM 100", "PIZZA 7", "JUICE 10", "WATER 1"])
