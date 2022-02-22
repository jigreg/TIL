budget = int(input()) # 초기자산
cnbc = list(map(int,input().split())) # 주가 표

juncash , sungcash = budget,budget
jun = 0 #주식 수
#준현 주식 거래 현황
for i in cnbc:
    if juncash >= i:
        jun += juncash //i
        juncash %= i

bnp = juncash + jun*cnbc[-1]

sung = 0 # 주식 수
#성민 주식 거래 현황
for i in range(len(cnbc)-3):
    #매수현황
    if cnbc[i] > cnbc[i+1] > cnbc[i+2]:
        sung += sungcash // cnbc[i+3]
        sungcash %= cnbc[i+3]
    #매도현황
    elif cnbc[i]< cnbc[i+1] < cnbc[i+2]:
        sungcash += sung*cnbc[i+3]
        sung = 0


timing = sungcash + sung*cnbc[-1]


if timing < bnp:
    print('BNP')
elif timing > bnp :
    print('TIMING')
else :
    print('SAMESAME')