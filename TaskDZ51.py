from random import randint


konf = 100
print('Игра "Конфеты". В вазе 2021 конфета, за раз вы можете взять не более 28 конфет, ')
print('выигрывает тот, кто возьмет последнюю конфету')
while konf >= 0:
    man = int(input('Сколько конфет возьмешь? '))
    if man > 28 or man > konf:
        print('Столько брать нельзя, начни сначала')
        break
    else:    
        konf -= man
        if konf == 0:
            print('Поздравляю! Вы выиграли!')
            break

    if konf >= 28:
        bot = randint(1, 29)
        print(f'Бот взял конфет: {bot}')
        konf -= bot
        print(f'Осталось конфет: {konf}')
    elif konf <= 28:
        bot = randint(1, konf)
        print(f'Бот взял конфет: {bot} ')
        konf -= bot
        print(f'Осталось конфет: {konf}')
    if konf == 0:
        print('Вы проиграли!')
        break