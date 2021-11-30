roomnum = list(input())

for _ in range(len(roomnum)):
    if "6" in roomnum:
        roomnum.remove("6")
        roomnum.append("9")
        roomnum.sort()
cnt = 0
for i in roomnum:
    if i in roomnum:
        cnt +=1

print(cnt)
