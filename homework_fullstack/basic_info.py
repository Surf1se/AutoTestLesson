name = input("Your name? ")
print(f"Привет, {name}! Рад с тобой познакомиться, меня зовут Ben!")

profesional = input("Твоя проффесия QA (ответь 'да')? Или напшиши, чем ты занимаешься.")
profesional = profesional.lower()

if profesional == "да":
    print(f"Круто! Наверное проффесия тестера тебе очень нравится?) А я - просто робот этой программы, я нихуя не умею, только говорить по скрипту :)")
    knowledge = input("А ты знаешо что такое переменная?")
    if knowledge == "да":
        print("Да ты вообще кабан! Молодец!!!")
    else:
        print("Самое время узнать!")
else:
    print("Аааа, я то общаюсь только с тестерами! Давай пока тогда! Не проспи завод завтра! хи-хи-хи")