countBug = int(input("Напишиет сколько кейсов вы сделали за неделю : "))
avg = countBug // 7
if avg >= 10:
    print(f"Общее колличество кейсов за неделю : {countBug}")
    print("Отличная работа!")
else:
    print("Попробуйте улучшить результат.")
