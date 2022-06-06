score = int(input("Бахои худро ворид кунед: "))
if score <= 100:  
    if score > 90 and score <= 100:
        if score >= 95:
            print("Аъло.Бахои шумо А")
        else:
            print("Аъло.Бахои шумо -А")
    elif score > 75 and score <= 85:
        if score > 75 and score < 80:
            print("Хуб.Бахои шумо -B")
        elif score >= 80 and score < 85:
            print("Хуб.Бахои шумо B")
        else :
            print("Хуб.Бахои шумо +B")
    elif score > 60 and score < 75:
        if score > 60 and score < 65:
            print("Миёна.Бахои шумо -C")
        elif score >= 65 and score < 70:
            print("Миёна.Бахои шумо C")
        else :
            print("Миёна.Бахои шумо +C")
    elif score > 50 and score < 60:
        if score > 50 and score < 55:
            print("Бад.Бахои шумо D")
        else:
            print("Бад.Бахои шумо +D")
    else :
        print("Каноатбахш.Бахои шумо F")
    
else :
    print("Бахо набояд аз 100 зиёд бошад!!")
