print("------------")
print("Приветствую Вас в игре: \"Угадай животное!\"")
print("правило: можно отвечать только да/нет")
print("------------\n")
if input("это животное большое?") == "да":
    if input("это животное полосатое?") == "да":
        if input("это животное ораньжевое?") == "да":
            print("я думаю это тигр!")
        else:
            print("я думаю это зебра!")
else:
    if input("это животное маленькое?") == "да":
        if input("это животное любит морковку?") == "да":
            if input("у данного животного длинные уши?") == "да":
                print("я думаю это кролик!")
            else:
                 print("я думаю это мышка!")
        else:
            if input("оно любит сено?") == "да":
                print("я думаю это шиншила!")
            else:
                if input("оно любит мёд?") == "да":
                    print("я думаю это медведь!")


#if input("я угод
 #   print("поздравляю вы выйграли!!!!")
#else:
 #   print("к сожалению вы проиграли")ал?") == "да":
