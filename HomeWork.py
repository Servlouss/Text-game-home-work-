# Герой и чудовища
import random
import sys

print('Привет,',input('Как тебя зовут?'),' ты в игре Герой и чудовища', 'Ты должен победить 10 чудищ, чтобы выиграть!', sep='\n')
Player_life = 10
Player_attack = 10
Monster = 10
print(f'Ваша жизнь: {Player_life}')
print(f'Сила атаки: {Player_attack}')

def funcs():
    for _ in range(1000):
        f = [war,eda,orujie]
        rand_func = random.choice(f)
        rand_func()

def war():

    global Player_life
    global Player_attack
    global Monster
    Monster_life = random.randint(5, 30)
    Monster_attack = random.randint(5, 30)

    print( f'Вы встретили чудовище с {Monster_life} жизнями и силой удара {Monster_attack}')
    print(f'Всего монстров: {Monster}')

    while Monster_life != 0 or Monster_life < 0:

        attack_run = int(input('1 - атаковать чудовище или 2 - убежать'))

        if attack_run == 1:
            if Player_attack>=Monster_life:
                Monster_life-=Player_attack
            if Player_attack<Monster_life:
                Monster_life -= Player_attack
                Player_life -= Monster_attack
                print('Вы атакуете')
                print(f'Жизни рыцаря: {Player_life}, Жизнь монстра: {Monster_life}')

        elif attack_run == 2:
            print('Вы убежали от чудища')
            print(f'Монстров осталось: {Monster}')
            break

        else:
            print('Введите заново')
            break

        if Monster_life <= 0 and Player_life > 0:
            print('Вы победили чудище')
            print(f'Жизни рыцаря: {Player_life}, Жизнь монстра: {Monster_life}')
            Monster -= 1

            if Monster == 0:
                print(f'Монстров осталось: {Monster}')
                print('ВЫ ПОБЕДИЛИ! СЛАВА УКРАИНЕ!!!')
                input('Нажмите Enter чтобы закрыть игру.')
                exit()
            return

        elif Monster_life > Player_life and Player_life <= 0:
            print('Вы умерли')
            print(f'Жизни рыцаря: {Player_life}, Жизнь монстра: {Monster_life}')
            print('Игра окончена!')
            input('Нажмите Enter чтобы закрыть игру.')
            exit()

def orujie():
    global Player_attack
    weapon = random.randint(5, 30)

    while True:
        print(f'Вы нашли меч! Его сила равна {weapon}')
        yes_or_not = int(input('1 - взять оружие, 2 - оставить'))

        if yes_or_not == 1:
            print(f'Вы взяли меч, теперь ваша сила равна {weapon}')
            Player_attack = weapon
            print(Player_attack)
            break

        elif yes_or_not == 2:
            print(f'Сила оружия остается {Player_attack}')
            print('Следующий ход')
            break
        else:
            print('Некорректный ввод')



def eda():
    global Player_life
    apple = random.randint(5, 30)

    while True:
        print(f'Вы нашли яблоко, оно добавит вам {apple} жизни')
        Player_life += apple
        print(f'Теперь у вас {Player_life} жизни')
        break
funcs()