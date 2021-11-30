emotions = input()
happy = emotions.count(":-)")
sad = emotions.count(":-(")

 
if happy > sad:
    print("happy")
elif happy < sad :
    print("sad")
elif happy == sad > 0 :
    print("unsure")
else :
    print("none")