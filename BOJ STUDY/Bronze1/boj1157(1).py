from collections import Counter
s = input().upper()
c = Counter(s)
maximum = c.most_common(1)[0][1]
if maximum == c.most_common(2)[1][1] :
    print("?")
else :
    print(c.most_common(1)[0][0])