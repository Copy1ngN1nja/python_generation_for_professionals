c1, c2, c3 = input(), input(), input()
eng = "AaBCcEeHKMOoPpTXxy"
rus = "АаВСсЕеНКМОоРрТХху" 

if all([c1 in eng, c2 in eng, c3 in eng]):
    print("en")
elif all([c1 in rus, c2 in rus, c3 in rus]):
    print("ru")
else:
    print("mix")